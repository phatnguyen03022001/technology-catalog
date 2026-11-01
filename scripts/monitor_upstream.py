#!/usr/bin/env python3
"""Read-only evidence freshness and upstream release/advisory signals (stdlib)."""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path

from validate_catalog import ROOT, service_rows

LINK = re.compile(r"\[[^]]+\]\((https://[^)]+)\)")
FIELD = re.compile(r"(?m)^- \*\*([^:]+):\*\*[ \t]*(.*)$")
VERSIONS = {"rust": r"crates\.io stable (\S+)", "go": r"Go module (\S+)",
            "typescript": r"npm latest (\S+)", "python": r"PyPI latest (\S+)",
            "swift": r"GitHub tag (\S+)"}
OSV_ECOSYSTEM = {"rust": "crates.io", "go": "Go", "typescript": "npm", "python": "PyPI"}

def parse_date(value: str) -> date:
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError(f"invalid evidence date {value!r}")
    result = date.fromisoformat(value)
    if result.isoformat() != value:
        raise ValueError(f"invalid evidence date {value!r}")
    return result

def sources(value: str) -> list[str]:
    return LINK.findall(value)

def inventory(root: Path = ROOT) -> list[dict]:
    rows: list[dict] = []
    def add(layer, path, name, scope, reviewed, status, source, **extra):
        rows.append(dict(layer=layer, path=path.relative_to(root).as_posix(),
                         name=name, scope=scope, reviewed=reviewed, status=status,
                         source=source, **extra))
    for path in sorted((root / "languages").glob("*.md")):
        if path.stem == "README":
            continue
        content = path.read_text(encoding="utf-8")
        match = re.search(r"\*\*Evidence review:\*\* ([^\s]+)", content)
        urls = sources(content.split("## Official evidence", 1)[-1])
        add("languages", path, path.stem, "language/toolchain",
            match.group(1) if match else "", "UNSPECIFIED", urls[0] if urls else "")
    for layer in ("frameworks", "decisions"):
        for path in sorted((root / layer).glob("*.md")):
            if path.stem == "README":
                continue
            content = path.read_text(encoding="utf-8")
            match = re.search(r"\*\*Reviewed:\*\* ([^\s]+)", content)
            status = re.search(r"\*\*Status:\*\* ([A-Z_]+)", content)
            urls = sources(content.split("## Official evidence", 1)[-1])
            repos = [m.group(1).removesuffix(".git") for u in urls
                     if (m := re.fullmatch(r"https://github\.com/([^/#?]+/[^/#?]+)", u))]
            add(layer, path, path.stem, "framework compatibility/license" if layer == "frameworks"
                else "conditional workload gates", match.group(1) if match else "",
                status.group(1) if status else "UNSPECIFIED", urls[0] if urls else "",
                github_repo=repos[0] if repos and layer == "frameworks" else None)
    for path in sorted((root / "libraries").glob("*.md")):
        if path.stem == "README":
            continue
        content = path.read_text(encoding="utf-8")
        if "## Entries\n" not in content:
            raise ValueError(f"missing library entries: {path}")
        data = content.split("## Entries\n", 1)[1].split("\n## ", 1)[0]
        bt = chr(96)
        blocks = re.split(r"(?m)^### " + bt + r"([^" + bt + r"\n]+)" + bt + r"\s*$", data)
        for heading, block in zip(blocks[1::2], blocks[2::2]):
            fields = dict(FIELD.findall(block))
            identity = fields.get("Package", "").strip(bt)
            version = re.search(VERSIONS[path.stem], fields.get("Maintenance", ""))
            urls = sources(fields.get("Official source", ""))
            add("libraries", path, identity, fields.get("Capability", "UNKNOWN"),
                fields.get("Evidence reviewed", ""), fields.get("Evidence status", "UNKNOWN"),
                urls[0] if urls else "", ecosystem=path.stem,
                baseline=version.group(1).rstrip(";,.") if version else None,
                compatibility=fields.get("Compatibility", "UNKNOWN"),
                license=fields.get("License", "UNKNOWN"),
                selection=fields.get("Selection", "BLOCKED"))
    for path in sorted((root / "providers").glob("*.md")):
        if path.stem == "README":
            continue
        for name, _, _, _, _, _, source, status, reviewed in service_rows(path):
            urls = sources(source)
            add("providers", path, name, "price/free tier/quota/ToS",
                reviewed, status.strip(chr(96)), urls[0] if urls else "")
    seen = set()
    for r in rows:
        key = (r["layer"], r.get("ecosystem"), r["name"].casefold())
        if not r["name"] or key in seen:
            raise ValueError(f"duplicate/empty monitored package identity {key}")
        seen.add(key)
    return rows

def freshness(row: dict, now: date) -> tuple[str, int | None]:
    if not row["reviewed"]:
        return "UNKNOWN", None
    age = (now - parse_date(row["reviewed"])).days
    if age < 0:
        raise ValueError(f"future evidence review date: {row['path']} {row['name']}")
    if row["status"] == "STALE":
        return "STALE", age
    return ("REVERIFY_REQUIRED" if age > 30 else "CURRENT"), age

def fetch_json(url: str, body: dict | None = None) -> dict:
    headers = {"User-Agent": "technology-catalog-monitor/1.0", "Accept": "application/json"}
    if url.startswith("https://api.github.com/") and os.getenv("GITHUB_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    data = json.dumps(body).encode() if body is not None else None
    if data:
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=data, headers=headers)
    with urllib.request.urlopen(request, timeout=12) as response:
        result = json.loads(response.read(10_000_000))
    if not isinstance(result, dict):
        raise ValueError("Expected JSON object")
    return result

def release(row: dict, fetch=fetch_json) -> tuple[str | None, str, str | None, str]:
    if row["layer"] == "frameworks" and row.get("github_repo"):
        url = f"https://api.github.com/repos/{row['github_repo']}/releases/latest"
        data = fetch(url)
        return data.get("tag_name"), url, data.get("published_at"), data.get("body") or ""
    if row["layer"] != "libraries" or not row.get("baseline"):
        return None, row["source"], None, ""
    eco, name = row["ecosystem"], row["name"]
    if eco == "rust":
        url = "https://crates.io/api/v1/crates/" + urllib.parse.quote(name, safe="")
        return fetch(url)["crate"].get("max_stable_version"), url, None, ""
    if eco == "go":
        escaped = "".join("!" + c.lower() if c.isupper() else c for c in name)
        url = "https://proxy.golang.org/" + escaped + "/@latest"
        return fetch(url).get("Version"), url, None, ""
    if eco == "typescript":
        url = "https://registry.npmjs.org/" + urllib.parse.quote(name, safe="@/") + "/latest"
        return fetch(url).get("version"), url, None, ""
    if eco == "python":
        url = "https://pypi.org/pypi/" + urllib.parse.quote(name, safe="") + "/json"
        return fetch(url).get("info", {}).get("version"), url, None, ""
    if eco == "swift":
        url = f"https://api.github.com/repos/{name}/releases/latest"
        return fetch(url).get("tag_name"), url, None, ""
    return None, row["source"], None, ""

def advisories(row: dict, fetch=fetch_json) -> tuple[str, str, bool]:
    if row["layer"] != "libraries" or not row.get("baseline"):
        return "UNKNOWN", "No reference version", False
    ecosystem = OSV_ECOSYSTEM.get(row["ecosystem"])
    if not ecosystem:
        return "UNKNOWN", "No verified OSV ecosystem mapping", False
    payload = {"version": row["baseline"].removeprefix("v"),
               "package": {"name": row["name"], "ecosystem": ecosystem}}
    data = fetch("https://api.osv.dev/v1/query", payload)
    if data.get("next_page_token"):
        return "CHECK_FAILED", "OSV pagination requires manual follow-up", False
    vulns = data.get("vulns", [])
    if not isinstance(vulns, list):
        raise ValueError("Invalid OSV response")
    if vulns:
        recent = any(
            date.fromisoformat(v["published"][:10]) > parse_date(row["reviewed"])
            for v in vulns if v.get("published") and row["reviewed"]
        )
        return "ADVISORY_FOUND", ", ".join("https://osv.dev/vulnerability/" + v["id"] for v in vulns[:4]), recent
    return "NO_ADVISORY_RETURNED", "No advisory returned (not a safety guarantee)", False

def probe(row: dict, fetch=fetch_json, security=False) -> dict:
    signal, detail, endpoint = "UNKNOWN", "No stable monitored release endpoint", row["source"]
    sec_signal, sec_detail = "UNKNOWN", "Not queried"
    monitored = (row["layer"] == "libraries" and row.get("baseline")
                 or row["layer"] == "frameworks" and row.get("github_repo"))
    if monitored:
        try:
            version, endpoint, published, notes = release(row, fetch)
            if not version:
                detail = "Upstream release has no comparable identifier"
            elif row["layer"] == "frameworks":
                # No baseline version: release after review DAY is a conservative signal.
                when = date.fromisoformat(published[:10]) if published else None
                if when is None:
                    detail = "Release publication date unavailable"
                elif when > parse_date(row["reviewed"]):
                    signal, detail = "UPSTREAM_CHANGED", f"Release {version} published {when} after review"
                else:
                    signal, detail = "NO_CHANGE_DETECTED", f"Latest release {version} predates review"
            elif version.removeprefix("v") != row["baseline"].removeprefix("v"):
                signal, detail = "UPSTREAM_CHANGED", f"Recorded {row['baseline']} versus upstream {version}"
            else:
                signal, detail = "NO_CHANGE_DETECTED", f"Release {version} matches recorded baseline"
            # Explicit upstream release-note heading, not inferred from semver/stars.
            if signal == "UPSTREAM_CHANGED" and re.search(
                r"(?im)^#{1,5}[ \t]*breaking changes?\b", notes
            ):
                detail += "; upstream release notes flag BREAKING_CHANGE"
        except (OSError, ValueError, KeyError, TypeError) as exc:
            signal, detail = "CHECK_FAILED", f"Release probe: {type(exc).__name__}"
    if security and row["layer"] == "libraries":
        try:
            sec_signal, sec_detail, advisory_newer = advisories(row, fetch)
        except (OSError, ValueError, KeyError, TypeError) as exc:
            sec_signal, sec_detail = "CHECK_FAILED", f"Advisory probe: {type(exc).__name__}"
        if sec_signal == "ADVISORY_FOUND":
            # A preexisting advisory is not a newly changed upstream release.
            if advisory_newer and signal != "CHECK_FAILED":
                signal = "UPSTREAM_CHANGED"
            elif signal not in ("UPSTREAM_CHANGED", "CHECK_FAILED"):
                signal = "SECURITY_REVIEW_REQUIRED"
            detail += "; advisory (check affected subpackage/symbol): " + sec_detail
        elif sec_signal == "CHECK_FAILED" and signal == "NO_CHANGE_DETECTED":
            signal, detail = "CHECK_FAILED", detail + "; advisory lookup failed"
    return {"signal": signal, "detail": detail, "probe_source": endpoint,
            "security": sec_signal, "security_detail": sec_detail}

def evaluate(rows: list[dict], now: date, live=False, security=False, fetch=fetch_json) -> list[dict]:
    results = []
    for row in rows:
        state, age = freshness(row, now)
        signal = probe(row, fetch, security) if live else dict(
            signal="NOT_CHECKED", detail="Upstream check not run in deterministic mode",
            probe_source=row["source"], security="UNKNOWN", security_detail="Not checked")
        entry = {**row, **signal, "freshness": state, "age": age}
        # An unrun probe is not evidence of staleness; actual UNKNOWN/CHECK_FAILED signals remain gated.
        entry["production_use"] = "BLOCK_REVERIFY" if (
            state != "CURRENT" or signal["signal"] in ("UPSTREAM_CHANGED", "CHECK_FAILED", "SECURITY_REVIEW_REQUIRED")
            or signal["signal"] == "UNKNOWN"
            or row["status"] in ("UNSPECIFIED", "STALE", "PARTIAL", "UNKNOWN", "UNVERIFIED",
                                  "SOURCE_LINKED_SNAPSHOT", "CONDITIONAL_NOT_PRODUCTION")
            or (row["layer"] == "libraries" and row.get("selection") == "BLOCKED")
        ) else "PROJECT_HARD_GATES_REQUIRED"
        results.append(entry)
    return results

def render(rows: list[dict], now: date, live=False, include_unknown=False) -> str:
    ages, signals, layers = [Counter(r[k] for r in rows) for k in ("freshness", "signal", "layer")]
    lines = [f"## Evidence monitor — {now.isoformat()} UTC", "",
             f"Mode: {'read-only upstream queries' if live else 'deterministic freshness'}. "
             "Never changes a verification timestamp, package or recommendation.",
             "", f"Records: {len(rows)}; " +
             ", ".join(f"{k}={v}" for k, v in sorted(layers.items())), "",
             "### Freshness (not claim status)", "",
             "| CURRENT | REVERIFY_REQUIRED | STALE | UNKNOWN |",
             "|---:|---:|---:|---:|",
             f"| {ages['CURRENT']} | {ages['REVERIFY_REQUIRED']} | {ages['STALE']} | {ages['UNKNOWN']} |",
             "", "### Upstream signals", "",
             "| NO_CHANGE_DETECTED | UPSTREAM_CHANGED | SECURITY_REVIEW_REQUIRED | CHECK_FAILED | UNKNOWN | NOT_CHECKED |",
             "|---:|---:|---:|---:|---:|---:|",
             f"| {signals['NO_CHANGE_DETECTED']} | {signals['UPSTREAM_CHANGED']} | {signals['SECURITY_REVIEW_REQUIRED']} | "
             f"{signals['CHECK_FAILED']} | {signals['UNKNOWN']} | {signals['NOT_CHECKED']} |",
             "", "### Actionable alerts", "",
             "| Record / evidence scope | Evidence status / freshness / signal | Source | Verified / age | Change signal and next action |",
             "|---|---|---|---|---|"]
    flagged = [r for r in rows if r["freshness"] != "CURRENT"
               or r["signal"] in ("UPSTREAM_CHANGED", "CHECK_FAILED", "SECURITY_REVIEW_REQUIRED")
               or include_unknown and r["signal"] in ("UNKNOWN", "NOT_CHECKED")]
    for r in flagged:
        action = ("Upstream check not run; freshness comes from the recorded evidence date"
                  if r["signal"] == "NOT_CHECKED" else
                  "Reverify affected claims before production use" if r["freshness"] == "REVERIFY_REQUIRED"
                  else "Assess release, security, compatibility and trade-offs; no auto bump"
                  if r["signal"] == "UPSTREAM_CHANGED" else
                  "Review affected package/symbol and advisory applicability; do not infer unsafe installation"
                  if r["signal"] == "SECURITY_REVIEW_REQUIRED" else
                  "Retry or verify manually; never infer no change" if r["signal"] == "CHECK_FAILED"
                  else "Manual evidence review required")
        detail = str(r["detail"]).replace("|", "/").replace("\n", " ")[:150]
        lines.append(f"| {r['path']} / {r['name']} ({r['scope']}) | {r['status']} / {r['freshness']} / {r['signal']} "
                     f"| {r['probe_source']} | {r['reviewed'] or 'UNKNOWN'} / "
                     f"{r['age'] if r['age'] is not None else 'UNKNOWN'}d | {detail}; **{action}** |")
    if not flagged:
        note = ("No evidence-freshness alerts; upstream checks not run in deterministic mode"
                if signals["NOT_CHECKED"] and not live else
                "No alerts detected; UNKNOWN monitoring coverage still applies")
        lines.append(f"| None | — | — | — | {note} |")
    lines += ["", "### Coverage limits", "",
              "- Providers pricing/quotas/ToS, language docs, conditional decisions and frameworks without release APIs are manual-review only. UNKNOWN is never evidence of no change; NOT_CHECKED means no upstream query ran and is not a freshness state.",
              "- An advisory published on/before the last review date is SECURITY_REVIEW_REQUIRED (applicability unknown), not a confirmed upstream change. Only newer advisory publications signal UPSTREAM_CHANGED.",
              "- NO_CHANGE_DETECTED checks only release identifiers or release publication dates. It does not detect every breaking change, deprecation, platform, license or security notice.",
              "- OSV checks use a referenced version for Rust/Go/npm/PyPI only when --security is enabled. No result does not prove safe. Swift mapping remains UNKNOWN.",
              "- This workflow does not certify production readiness; project-specific security, licensing, compatibility and cost hard gates still apply.", ""]
    return "\n".join(lines)

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-upstream", action="store_true")
    parser.add_argument("--security", action="store_true")
    parser.add_argument("--as-of", help="UTC frozen date for tests and manual simulation")
    parser.add_argument("--all-unknown", action="store_true",
                        help="also list every unsupported/unprobed source individually")
    args = parser.parse_args(argv)
    if args.security and not args.check_upstream:
        parser.error("--security requires --check-upstream")
    try:
        now = parse_date(args.as_of) if args.as_of else datetime.now(timezone.utc).date()
        report = render(evaluate(inventory(), now, args.check_upstream, args.security),
                        now, args.check_upstream, args.all_unknown)
    except ValueError as exc:
        print(f"INVALID EVIDENCE: {exc}", file=sys.stderr)
        return 1
    print(report)
    if os.getenv("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as file:
            file.write(report + "\n")
    return 0

if __name__ == "__main__":
    sys.exit(main())
