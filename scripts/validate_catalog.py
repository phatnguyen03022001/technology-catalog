#!/usr/bin/env python3
"""Check provider-catalog structure and derive service evidence counts.

This validates catalog structure and deterministic evidence hygiene only. It does
not verify factual pricing or live source claims; source review remains necessary.
"""

from __future__ import annotations

import ipaddress
import re
import sys
from collections import Counter, defaultdict
from datetime import date, datetime, timezone, timedelta
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
PROVIDERS = ROOT / "providers"
PILLARS = ROOT / "pillars"
STATUSES = {"VERIFIED", "SOURCE_LINKED_SNAPSHOT", "UNVERIFIED", "STALE", "DISCONTINUED"}
FREE_KINDS = {
    "PERMANENT", "RECURRING_CREDIT", "ONE_TIME_CREDIT", "TIME_LIMITED_TRIAL",
    "PERMANENT_AFTER_TRIAL", "LIMITED_FREE", "NO_MONTHLY_BASE", "SELF_HOSTED",
    "NONE", "UNKNOWN",
}
EXPECTED_HEADERS = [
    "Service", "Primary pillar", "Free kind", "Free tier/credits", "Paid pricing",
    "Caveat", "Official source", "Evidence status", "Evidence checked",
]


# Deterministic evidence hygiene only: this does not authenticate a web page
# or establish that a source supports the stated price.
PLACEHOLDER = re.compile(r"\b(?:TODO|TBD|FIXME|PLACEHOLDER)\b", re.IGNORECASE)
NEGATIVE_PRICE = re.compile(
    r"(?:[$€£]\s*-\s*\d|-\s*[$€£]\s*\d|-\s*\d+(?:[.,]\d+)?\s*(?:USD|EUR|GBP)\b)",
    re.IGNORECASE,
)
RESERVED_HOSTS = {"localhost", "example.com", "example.net", "example.org"}


def source_url_error(url: str) -> str | None:
    """Reject malformed/obviously fake URLs; not a network or authority check."""
    try:
        parsed = urlsplit(url)
        host = parsed.hostname
        port = parsed.port  # Accessing this rejects invalid ports.
    except ValueError:
        return "malformed URL"
    if parsed.scheme != "https" or not host or parsed.username or parsed.password:
        return "source must be an HTTPS URL without credentials"
    if port is not None and port != 443:
        return "unexpected HTTPS source port"
    host = host.lower()
    if (host in RESERVED_HOSTS or
            host.endswith((".localhost", ".example", ".test", ".invalid"))):
        return "placeholder source domain"
    if not re.fullmatch(r"[a-z0-9.-]+", host) or "." not in host or ".." in host:
        return "invalid source hostname"
    try:
        addr = ipaddress.ip_address(host)
    except ValueError:
        pass
    else:
        if not addr.is_global:
            return "non-public source IP"
    return None


def evidence_hygiene_errors(row: list[str], path: Path) -> list[str]:
    service, _, free_kind, allowance, paid, caveat, source, status, checked = row
    prefix = f"{path.relative_to(ROOT)}: service {service}"
    errors = []
    for name, value in (("free allowance", allowance), ("paid pricing", paid),
                        ("caveat", caveat), ("official source", source)):
        if PLACEHOLDER.search(value):
            errors.append(f"{prefix}: {name} contains a placeholder")
    if NEGATIVE_PRICE.search(paid):
        errors.append(f"{prefix}: paid pricing contains a negative price")
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", source)
    if not links:
        errors.append(f"{prefix}: official source needs a Markdown HTTPS link")
    for url in links:
        problem = source_url_error(url)
        if problem:
            errors.append(f"{prefix}: {problem}: {url}")
    # VERIFIED is claim-level evidence, not proof that TCO is calculable.
    # No-digit prices must explicitly communicate their cost decision state.
    if (status.strip("`") == "VERIFIED" and
            free_kind.strip("`") != "SELF_HOSTED" and
            not re.search(r"\d", paid) and
            not re.search(r"\b(?:TCO_UNKNOWN|NO_DIRECT_FEE)\b", caveat)):
        errors.append(f"{prefix}: non-quantified VERIFIED pricing needs "
                      "TCO_UNKNOWN or NO_DIRECT_FEE in Caveat")
    return errors


def cells(line: str) -> list[str]:
    return [part.strip() for part in line.strip().strip("|").split("|")]


def service_rows(path: Path) -> list[list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        if line.startswith("| Service | Primary pillar |"):
            if cells(line) != EXPECTED_HEADERS:
                raise ValueError(f"{path.relative_to(ROOT)}: service table header does not match schema")
            rows = []
            for row in lines[i + 2:]:
                if not row.startswith("| "):
                    break
                parts = cells(row)
                if len(parts) != len(EXPECTED_HEADERS):
                    raise ValueError(f"{path.relative_to(ROOT)}: expected 9 cells, got {len(parts)}: {row}")
                rows.append(parts)
            return rows
    raise ValueError(f"{path.relative_to(ROOT)}: missing service table")


def local_links(markdown: Path) -> list[str]:
    errors = []
    text = markdown.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        if target.startswith(("https://", "http://", "mailto:", "#")):
            continue
        file_target, _, fragment = target.partition("#")
        if not file_target:
            continue
        candidate = (markdown.parent / file_target).resolve()
        if not candidate.exists():
            errors.append(f"{markdown.relative_to(ROOT)}: broken link {target}")
            continue
        if fragment and candidate.suffix == ".md":
            headings = set()
            for heading in re.findall(r"^#{1,6} +(.+?)\s*#*\s*$", candidate.read_text(encoding="utf-8"), re.MULTILINE):
                slug = re.sub(r"[^\w -]", "", heading.casefold(), flags=re.UNICODE).strip().replace(" ", "-")
                headings.add(slug)
            if fragment.casefold() not in headings:
                errors.append(f"{markdown.relative_to(ROOT)}: missing heading anchor {target}")
    return errors


def main() -> int:
    errors: list[str] = []
    files = sorted(p for p in PROVIDERS.glob("*.md") if p.name != "README.md")
    identities: set[str] = set()
    services: set[str] = set()
    evidence = Counter()
    free_kinds = Counter()
    pillar_counts = Counter()
    nonverified_pillars = Counter()
    expected_index_links = Counter()
    expected_index_services = Counter()
    provider_counts = {}
    provider_titles = {}
    service_lookup = {}
    provider_pillars = defaultdict(set)

    for path in files:
        text = path.read_text(encoding="utf-8")
        heading = re.search(r"^# (.+)$", text, re.MULTILINE)
        identity = heading.group(1).strip() if heading else ""
        if not identity or identity.casefold() in identities:
            errors.append(f"{path.relative_to(ROOT)}: missing or duplicate provider identity {identity!r}")
        identities.add(identity.casefold())
        provider_titles[path.stem] = identity
        try:
            rows = service_rows(path)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        provider_counts[path.stem] = len(rows)
        for row in rows:
            service, pillar, free_kind, allowance, paid, caveat, source, status, checked = row
            key = service.casefold()
            if key in services:
                errors.append(f"{path.relative_to(ROOT)}: duplicate service identity {service!r}")
            services.add(key)
            service_lookup[key] = (path.stem, pillar, status.strip("`"))
            if not re.fullmatch(r"0[1-9]|1[0-2]", pillar):
                errors.append(f"{path.relative_to(ROOT)}: invalid primary pillar {pillar!r} for {service}")
            else:
                pillar_counts[pillar] += 1
                expected_index_links[(path.stem, pillar)] += 1
                expected_index_services[(path.stem, pillar, service.casefold())] += 1
                provider_pillars[path.stem].add(pillar)
            kind = free_kind.strip("`")
            if kind not in FREE_KINDS:
                errors.append(f"{path.relative_to(ROOT)}: unsupported free kind {kind!r} for {service}")
            free_kinds[kind] += 1
            state = status.strip("`")
            if state not in STATUSES:
                errors.append(f"{path.relative_to(ROOT)}: unsupported evidence status {state!r} for {service}")
            evidence[state] += 1
            if state != "VERIFIED":
                nonverified_pillars[pillar] += 1
            errors.extend(evidence_hygiene_errors(row, path))
            if not re.search(r"https://", source):
                errors.append(f"{path.relative_to(ROOT)}: missing official HTTPS source for {service}")
            try:
                parsed_checked = date.fromisoformat(checked)
            except ValueError:
                parsed_checked = None
            if parsed_checked is None or parsed_checked.isoformat() != checked:
                errors.append(f"{path.relative_to(ROOT)}: service {service} needs an ISO evidence review date")
            elif parsed_checked > datetime.now(timezone.utc).date():
                errors.append(f"{path.relative_to(ROOT)}: service {service} has a future evidence review date {checked}")
            elif state == "VERIFIED" and datetime.now(timezone.utc).date() - parsed_checked > timedelta(days=180):
                errors.append(f"{path.relative_to(ROOT)}: service {service} has VERIFIED evidence older than 180 days; re-review or downgrade")
            if state in {"SOURCE_LINKED_SNAPSHOT", "UNVERIFIED", "STALE"}:
                if not re.search(r"\bRC[1-7]\b", caveat):
                    errors.append(f"{path.relative_to(ROOT)}: unresolved service {service} needs an RC1-RC7 cause in Caveat")
            if state == "VERIFIED":
                if not allowance.strip() or not paid.strip() or not caveat.strip():
                    errors.append(f"{path.relative_to(ROOT)}: VERIFIED service {service} has incomplete evidence fields")
            # Free-kind status is separate from price-evidence status. A verified
            # no-free-tier claim can coexist with unresolved SKU/region pricing.
            if kind == "NONE" and not re.search(r"\bno free (?:service )?(?:tier|allowance|quota)\b", allowance, re.I):
                errors.append(f"{path.relative_to(ROOT)}: {service} uses NONE without an explicit no-free-tier claim")

    for path in sorted(ROOT.rglob("*.md")):
        errors.extend(local_links(path))

    indexed_links = Counter()
    indexed_services = Counter()
    for number in range(1, 13):
        pillar = f"{number:02d}"
        matches = sorted(PILLARS.glob(f"{pillar}-*/README.md"))
        if len(matches) != 1:
            errors.append(f"pillars/: expected one index for pillar {pillar}, found {len(matches)}")
            continue
        body = matches[0].read_text(encoding="utf-8")
        table = body.split("| Service offering | Provider SSOT |", 1)
        count = 0
        if len(table) == 2:
            for line in table[1].splitlines()[2:]:
                if not line.startswith("| "):
                    break
                count += 1
                index_cells = cells(line)
                match = re.search(r"\]\((?:\.\./)+providers/([^)#]+\.md)(?:#[^)]*)?\)", line)
                if not match:
                    errors.append(f"{matches[0].relative_to(ROOT)}: service index row lacks a provider SSOT link: {line}")
                else:
                    provider = Path(match.group(1)).stem
                    indexed_links[(provider, pillar)] += 1
                    if len(index_cells) != 2:
                        errors.append(f"{matches[0].relative_to(ROOT)}: malformed service index row: {line}")
                    else:
                        indexed_services[(provider, pillar, index_cells[0].casefold())] += 1
        if count != pillar_counts[pillar]:
            errors.append(f"pillar {pillar}: index has {count} rows; provider records have {pillar_counts[pillar]}")
    for key in set(expected_index_links) | set(indexed_links):
        if expected_index_links[key] != indexed_links[key]:
            errors.append(f"primary-pillar index mapping mismatch for provider {key[0]} in pillar {key[1]}: provider rows={expected_index_links[key]}, index links={indexed_links[key]}")
    for key in set(expected_index_services) | set(indexed_services):
        if expected_index_services[key] != indexed_services[key]:
            errors.append(f"primary-pillar service index mismatch for {key[0]} in pillar {key[1]}: {key[2]!r}; provider rows={expected_index_services[key]}, index rows={indexed_services[key]}")

    watchlist_counts = {}
    for index_path in sorted(PILLARS.glob("[0-1][0-9]-*/README.md")):
        content = index_path.read_text(encoding="utf-8")
        match = re.search(r"^## Watchlist — (\d+)\b", content, re.MULTILINE)
        if not match:
            errors.append(f"{index_path.relative_to(ROOT)}: missing derived watchlist heading")
            continue
        section = content.split(match.group(0), 1)[1].split("\n## ", 1)[0]
        count = sum(1 for line in section.splitlines() if line.startswith("| ") and not line.startswith(("|---", "| Candidate |")))
        watchlist_counts[index_path.parent.name[:2]] = count
        if count != int(match.group(1)):
            errors.append(f"{index_path.relative_to(ROOT)}: watchlist heading says {match.group(1)} but section has {count} candidates")
    watchlist_total = sum(watchlist_counts.values())

    summary = {
        "providers": len(files),
        "services": len(services),
        "evidence": dict(sorted(evidence.items())),
        "free_kinds": dict(sorted(free_kinds.items())),
        "pillars": dict(sorted(pillar_counts.items())),
        "watchlist_candidates": watchlist_total,
    }
    if summary["providers"] != len(identities):
        errors.append("provider profile count does not match unique identities")
    provider_index = (PROVIDERS / "README.md").read_text(encoding="utf-8")
    if not re.search(rf"\*\*{summary['providers']} provider profiles\*\*", provider_index):
        errors.append("providers/README.md provider count does not match derived profiles")
    if not re.search(rf"\*\*{summary['services']} service offering records\*\*", provider_index):
        errors.append("providers/README.md service count does not match derived rows")
    provider_table = provider_index.split("| Provider | Offerings | Primary pillars |", 1)
    indexed_providers = {}
    if len(provider_table) == 2:
        for line in provider_table[1].splitlines()[2:]:
            if not line.startswith("| "):
                break
            match = re.search(r"\]\(\./([^)]+\.md)\)\s*\|\s*(\d+)\s*\|\s*([^|]+)\|", line)
            if not match:
                errors.append(f"providers/README.md malformed provider index row: {line}")
                continue
            filename, count, pillar_text = match.groups()
            stem = Path(filename).stem
            label_match = re.match(r"\|\s*\[([^\]]+)\]", line)
            label = label_match.group(1) if label_match else ""
            if label != provider_titles.get(stem):
                errors.append(f"providers/README.md provider title mismatch for {filename}: index {label!r}, SSOT {provider_titles.get(stem)!r}")
            if stem in indexed_providers:
                errors.append(f"providers/README.md duplicate provider entry: {filename}")
            indexed_providers[stem] = int(count)
            indexed_pillars = set(re.findall(r"\b(0[1-9]|1[0-2])\b", pillar_text))
            if int(count) != provider_counts.get(stem, -1):
                errors.append(f"providers/README.md offering count mismatch for {filename}")
            if indexed_pillars != provider_pillars.get(stem, set()):
                errors.append(f"providers/README.md primary pillar list mismatch for {filename}")
    if set(indexed_providers) != set(provider_counts):
        errors.append("providers/README.md provider index does not match provider profile files")
    root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if not re.search(rf"12 pillars; {summary['providers']} provider profiles; {summary['services']} service offerings; {summary['watchlist_candidates']} discovery-only watchlist candidate", root_readme):
        errors.append("README.md snapshot counts do not match derived catalog counts")
    if "| Evidence status | Service records |" in provider_index:
        table = provider_index.split("| Evidence status | Service records |", 1)[1].split("\n\n", 1)[0]
        displayed = {row[0].strip("`"): int(row[1]) for line in table.splitlines() if line.startswith("| `") for row in [cells(line)] if len(row) == 2 and row[1].isdigit()}
        for state in STATUSES:
            if displayed.get(state, 0) != evidence[state]:
                errors.append(f"providers/README.md {state} count differs from derived service rows")
    else:
        errors.append("providers/README.md missing evidence status count table")
    free_line = next((line for line in provider_index.splitlines() if line.startswith("Free-kind classifications")), "")
    displayed_kinds = {name: int(value) for name, value in re.findall(r"`([A-Z_]+)` (\d+)", free_line)}
    for kind in FREE_KINDS:
        if displayed_kinds.get(kind, 0) != free_kinds[kind]:
            errors.append(f"providers/README.md {kind} count differs from derived service rows")

    candidate_doc = (ROOT / "docs/provider-candidates.md").read_text(encoding="utf-8")
    accepted_section = candidate_doc.split("## Accepted market additions", 1)
    if len(accepted_section) != 2:
        errors.append("docs/provider-candidates.md missing accepted market additions section")
    else:
        accepted_section = accepted_section[1].split("## Product-name and lifecycle", 1)[0]
        accepted_rows = [line for line in accepted_section.splitlines() if re.match(r"\| (?:0[1-9]|1[0-2]) \|", line)]
        declared_additions = re.search(r"^(\d+) market-discovery service offerings are recorded", candidate_doc, re.MULTILINE)
        if not declared_additions:
            errors.append("docs/provider-candidates.md missing declared market-discovery count")
        elif int(declared_additions.group(1)) != len(accepted_rows):
            errors.append(f"docs/provider-candidates.md declares {declared_additions.group(1)} market-discovery additions but lists {len(accepted_rows)}")
        accepted_names = [cells(line)[1].casefold() for line in accepted_rows if len(cells(line)) == 5]
        if len(accepted_names) != len(accepted_rows):
            errors.append("docs/provider-candidates.md has malformed accepted market-addition rows")
        if len(accepted_names) != len(set(accepted_names)):
            errors.append("docs/provider-candidates.md has duplicate accepted market additions")
        # Discovery is a denormalized view of provider SSOT; validate the
        # offering identity, pillar, referenced provider and status.
        for line in accepted_rows:
            row = cells(line)
            if len(row) != 5:
                continue
            pillar, service, _, provider_link, status = row
            claim = service_lookup.get(service.casefold())
            link = re.fullmatch(r"\[([^\]]+)\]\(\.\./providers/([a-z0-9-]+)\.md\)", provider_link)
            if not claim:
                errors.append(f"docs/provider-candidates.md unknown offering {service!r}")
                continue
            provider, expected_pillar, expected_status = claim
            if pillar != expected_pillar:
                errors.append(f"docs/provider-candidates.md pillar mismatch for {service!r}: {pillar} != {expected_pillar}")
            if not link or link.group(2) != provider:
                errors.append(f"docs/provider-candidates.md provider reference mismatch for {service!r}")
            elif link.group(1) != provider_titles[provider]:
                errors.append(f"docs/provider-candidates.md provider identity mismatch for {service!r}")
            if status.strip("`") != expected_status:
                errors.append(f"docs/provider-candidates.md evidence status mismatch for {service!r}: {status} != {expected_status}")
    for line in candidate_doc.splitlines():
        match = re.match(r"\| \[([0-1][0-9]) — .*\| (\d+) \| (\d+) \|$", line)
        if match:
            pillar, documented, pending = match.groups()
            if int(documented) != pillar_counts[pillar] or int(pending) != nonverified_pillars[pillar]:
                errors.append(f"docs/provider-candidates.md pillar {pillar} counts do not match provider rows")
    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("STRUCTURE PASS (does not establish pricing accuracy)")
    print(f"Providers: {summary['providers']}; services: {summary['services']}; watchlist candidates: {summary['watchlist_candidates']}")
    print(f"Evidence status: {summary['evidence']}")
    print(f"Free kind: {summary['free_kinds']}")
    print(f"Pillar services: {summary['pillars']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
