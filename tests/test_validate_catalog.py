"""Regression tests for deterministic catalog validation (stdlib only)."""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date, timedelta
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
FIELDS = {"free": 4, "paid": 5, "caveat": 6, "source": 7, "status": 8, "checked": 9}


class CatalogMutationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ("providers", "pillars", "docs", "scripts", "languages", "frameworks", "decisions", "libraries"):
            shutil.copytree(REPO / name, self.root / name)
        shutil.copy2(REPO / "README.md", self.root / "README.md")

    def validate(self, expected: int, message: str = "") -> None:
        result = subprocess.run(
            [sys.executable, str(self.root / "scripts" / "validate_catalog.py")],
            capture_output=True,
            text=True,
            timeout=15,
            check=False,
        )
        self.assertEqual(result.returncode, expected,
                         f"Expected {expected}: {result.stdout}\n{result.stderr}")
        if message:
            self.assertIn(message, result.stdout)

    def change(self, provider: str, service: str, field: str, replacement) -> None:
        path = self.root / "providers" / f"{provider}.md"
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        count = 0
        for i, line in enumerate(lines):
            if not line.startswith(f"| {service} |"):
                continue
            parts = line.rstrip("\n").split("|")
            self.assertEqual(len(parts), 11)
            idx = FIELDS[field]
            parts[idx] = " " + replacement(parts[idx].strip()) + " "
            lines[i] = "|".join(parts) + "\n"
            count += 1
        self.assertEqual(count, 1, f"Expected one row: {provider}/{service}")
        path.write_text("".join(lines), encoding="utf-8")

    def test_real_catalog_passes(self):
        self.validate(0, "STRUCTURE PASS")

    def test_future_review_date_fails(self):
        self.change("supabase", "Supabase Database", "checked", lambda _: "2099-01-01")
        self.validate(1, "future evidence review date")

    def test_placeholder_price_fails(self):
        self.change("supabase", "Supabase Database", "paid", lambda _: "TBD")
        self.validate(1, "paid pricing contains a placeholder")

    def test_placeholder_caveat_fails(self):
        self.change("supabase", "Supabase Database", "caveat", lambda s: s + " TODO")
        self.validate(1, "caveat contains a placeholder")

    def test_negative_dollar_price_fails(self):
        self.change("supabase", "Supabase Database", "paid", lambda _: "Pro $-25/month")
        self.validate(1, "negative price")

    def test_negative_prefix_price_fails(self):
        self.change("supabase", "Supabase Database", "paid", lambda _: "Pro -$25/month")
        self.validate(1, "negative price")

    def test_negative_numeric_usd_price_fails(self):
        self.change("supabase", "Supabase Database", "paid", lambda _: "Pro -25 USD/month")
        self.validate(1, "negative price")

    def test_placeholder_https_source_fails(self):
        self.change("supabase", "Supabase Database", "source",
                    lambda _: "[Pricing](https://example.com/pricing)")
        self.validate(1, "placeholder source domain")

    def test_reserved_test_domain_fails(self):
        self.change("supabase", "Supabase Database", "source",
                    lambda _: "[Pricing](https://billing.example.test/pricing)")
        self.validate(1, "placeholder source domain")

    def test_insecure_source_fails(self):
        self.change("supabase", "Supabase Database", "source",
                    lambda _: "[Pricing](http://supabase.com/pricing)")
        self.validate(1, "HTTPS URL")

    def test_local_source_fails(self):
        self.change("supabase", "Supabase Database", "source",
                    lambda _: "[Pricing](https://127.0.0.1/pricing)")
        self.validate(1, "non-public source IP")

    def test_source_with_credentials_fails(self):
        self.change("supabase", "Supabase Database", "source",
                    lambda _: "[Pricing](https://admin:pw@supabase.com/pricing)")
        self.validate(1, "without credentials")

    def test_nonquantified_verified_requires_cost_disposition(self):
        self.change("cloudflare", "Cloudflare Turnstile", "caveat",
                    lambda s: s.replace("NO_DIRECT_FEE", ""))
        self.validate(1, "non-quantified VERIFIED pricing")

    def test_explicit_zero_price_is_not_negative(self):
        self.change("supabase", "Supabase Database", "paid",
                    lambda _: "Pro $0/month under a synthetic test scenario")
        self.validate(0, "STRUCTURE PASS")

    def test_discovery_evidence_status_mismatch_fails(self):
        p = self.root / "docs" / "provider-candidates.md"
        original = "| 09 | GlitchTip Cloud | Adds a Sentry-compatible error monitoring option with self-host lineage. | [GlitchTip](../providers/glitchtip.md) | `VERIFIED` |"
        assert original in p.read_text()
        p.write_text(p.read_text().replace(original, original.replace("`VERIFIED`", "`UNVERIFIED`")))
        self.validate(1, "evidence status mismatch")

    def test_discovery_provider_link_to_existing_wrong_provider_fails(self):
        p = self.root / "docs" / "provider-candidates.md"
        original = "[GlitchTip](../providers/glitchtip.md) | `VERIFIED`"
        assert original in p.read_text()
        p.write_text(p.read_text().replace(original, "[Sentry](../providers/sentry.md) | `VERIFIED`"))
        self.validate(1, "provider reference mismatch")

    def test_discovery_provider_label_mismatch_fails(self):
        p = self.root / "docs" / "provider-candidates.md"
        original = "[GlitchTip](../providers/glitchtip.md) | `VERIFIED`"
        assert original in p.read_text()
        p.write_text(p.read_text().replace(original, "[Fake Brand](../providers/glitchtip.md) | `VERIFIED`"))
        self.validate(1, "provider identity mismatch")

    def test_discovery_pillar_mismatch_fails(self):
        p = self.root / "docs" / "provider-candidates.md"
        original = "| 09 | GlitchTip Cloud |"
        assert original in p.read_text()
        p.write_text(p.read_text().replace(original, "| 01 | GlitchTip Cloud |"))
        self.validate(1, "pillar mismatch")

    def test_provider_index_title_drift_fails(self):
        p = self.root / "providers" / "glitchtip.md"
        assert p.read_text().startswith("# GlitchTip\n")
        p.write_text(p.read_text().replace("# GlitchTip\n", "# GlitchTip Renamed`n", 1))
        self.validate(1, "provider title mismatch")

    def test_verified_claim_too_old_fails(self):
        self.change("glitchtip", "GlitchTip Cloud", "checked", lambda _: "2020-01-01")
        self.validate(1, "VERIFIED evidence older than 180 days")

    def test_unindexed_framework_rejected(self):
        (self.root / "frameworks" / "rogue.md").write_text("# Rogue\n\n**Reviewed:** 2026-11-01\n")
        self.validate(1, "unindexed framework profile")

    def test_indexed_framework_missing_evidence_rejected(self):
        index = self.root / "frameworks" / "README.md"
        index.write_text(index.read_text().replace(
            "| Swift | Vapor | Swift server-side HTTP APIs | [Vapor](vapor.md) |",
            "| Swift | Vapor | Swift server-side HTTP APIs | [Vapor](vapor.md) |\n"
            "| Go | Rogue | Bad candidate | [Rogue](rogue.md) |",
        ))
        (self.root / "frameworks" / "rogue.md").write_text(
            "# Rogue\n\n**Reviewed:** 2026-11-01\n\n## Fit\nNot evidenced.\n"
        )
        self.validate(1, "missing required section")

    def test_unindexed_decision_rejected(self):
        (self.root / "decisions" / "unsafe.md").write_text(
            "# Unsafe\n\n**Status:** APPROVED_FOR_PRODUCTION\n"
        )
        self.validate(1, "unindexed decision record")

    def test_indexed_fake_production_approval_rejected(self):
        index = self.root / "decisions" / "README.md"
        index.write_text(index.read_text().replace(
            "| [Native Apple app](apple-native.md) |",
            "| [Unsafe](unsafe.md) | fake | fake | APPROVED |\n"
            "| [Native Apple app](apple-native.md) |",
        ))
        (self.root / "decisions" / "unsafe.md").write_text(
            "# Unsafe\n\n**Status:** APPROVED_FOR_PRODUCTION · **Reviewed:** 2026-11-01 "
            "· **Workload:** magic.\n\n## Hard gates\n"
            "- Functional: **PASS**\n"
        )
        self.validate(1, "production approval")

    def test_decision_index_status_mismatch_rejected(self):
        index = self.root / "decisions" / "README.md"
        index.write_text(index.read_text().replace(
            "Next.js | CONDITIONAL; deploy/SSR workload test pending |",
            "Next.js | APPROVED; deploy/SSR workload test pending |",
        ))
        self.validate(1, "decision index status mismatch")

    def test_reference_decision_conflicting_approval_rejected(self):
        p = self.root / "decisions" / "web-fullstack.md"
        p.write_text(p.read_text() + "\nAPPROVED_FOR_PRODUCTION\n")
        self.validate(1, "contradictory approval")

    def test_review_date_valid_change_allowed(self):
        p = self.root / "frameworks" / "nextjs.md"
        p.write_text(p.read_text().replace("**Reviewed:** 2026-11-01",
                                            "**Reviewed:** 2026-10-31"))
        self.validate(0, "STRUCTURE PASS")

    def test_invalid_review_date_rejected(self):
        p = self.root / "frameworks" / "nextjs.md"
        p.write_text(p.read_text().replace("**Reviewed:** 2026-11-01",
                                            "**Reviewed:** next-week"))
        self.validate(1, "invalid review date")

    def test_future_review_date_rejected(self):
        p = self.root / "frameworks" / "nextjs.md"
        p.write_text(p.read_text().replace("**Reviewed:** 2026-11-01",
                                            "**Reviewed:** 2099-01-01"))
        self.validate(1, "future review date")

    def test_fragment_only_broken_anchor_rejected(self):
        p = self.root / "README.md"
        p.write_text(p.read_text() + "\n[broken](#nonexistent-anchor)\n")
        self.validate(1, "missing heading anchor")

    def test_fragment_only_valid_anchor_allowed(self):
        p = self.root / "README.md"
        p.write_text(p.read_text() + "\n[nav](#navigation)\n")
        self.validate(0, "STRUCTURE PASS")

    def make_approved_fixture(self):
        index = self.root / "decisions" / "README.md"
        index.write_text(index.read_text().replace(
            "| [Native Apple app](apple-native.md) |",
            "| [Measured test](measured-test.md) | real project | measured | APPROVED |\n"
            "| [Native Apple app](apple-native.md) |",
        ))
        proof = "[evidence](https://github.com/example/benchmark)"
        gates = ("Functional", "Security/privacy", "Legal/licensing",
                 "Cost/TCO", "Portability/recovery")
        lines = [
            "# Measured test",
            "**Status:** APPROVED_FOR_PRODUCTION · **Reviewed:** 2026-10-31 "
            "· **Workload:** measured production traffic.",
            "",
            "## Workload & candidates",
            "Named project service comparing real traffic and measured options.",
            "",
            "## Hard gates",
        ] + [f"- {gate}: **PASS** supported by {proof}." for gate in gates] + [
            "",
            "## Decision & falsification",
            "Choose based on reviewed measurements and an explicit rollback option.",
            "",
            "## Verification / TCO / fallback",
            "Reproduce the workload, measured resource use, billing and fallback.",
            "",
            "## Official evidence",
            "- [Docs one](https://go.dev/doc/)",
            "- [Docs two](https://docs.python.org/3/)",
            "",
            "## Approval evidence",
            "- Owner: Team infrastructure",
            "- Project: Actual production gateway",
            "- Workload ID: production-load-2026-10",
            "- Benchmark evidence: [benchmark](https://github.com/example/benchmarks)",
            "- TCO evidence: [invoice](https://github.com/example/costs)",
            "- Approval date: 2026-10-31",
        ]
        path = self.root / "decisions" / "measured-test.md"
        path.write_text("\n".join(lines) + "\n")
        return path

    def test_complete_production_approval_contract_allowed(self):
        self.make_approved_fixture()
        self.validate(0, "STRUCTURE PASS")

    def test_production_approval_missing_one_hard_gate_evidence_rejected(self):
        path = self.make_approved_fixture()
        path.write_text(path.read_text().replace(
            "- Security/privacy: **PASS** supported by [evidence](https://github.com/example/benchmark).",
            "- Security/privacy: **PASS** without evidence.",
        ))
        self.validate(1, "production approval missing PASS gate evidence: Security/privacy")

    def test_production_approval_placeholder_gate_source_rejected(self):
        path = self.make_approved_fixture()
        path.write_text(path.read_text().replace(
            "[evidence](https://github.com/example/benchmark)",
            "[evidence](https://example.com/benchmark)",
        ))
        self.validate(1, "production approval missing PASS gate evidence")

    def test_production_approval_unmeasured_rejected(self):
        path = self.make_approved_fixture()
        path.write_text(path.read_text() + "\nNOT_MEASURED\n")
        self.validate(1, "production approval contains unresolved")

    def test_broken_cross_document_anchor_rejected(self):
        p = self.root / "README.md"
        p.write_text(p.read_text() + "\n[bad](frameworks/nextjs.md#does-not-exist)\n")
        self.validate(1, "missing heading anchor")

    def test_valid_cross_document_anchor_allowed(self):
        p = self.root / "README.md"
        p.write_text(p.read_text() + "\n[good](frameworks/nextjs.md#compatibility)\n")
        self.validate(0, "STRUCTURE PASS")

    def test_original_schema_validation_still_fails_unknown_status(self):
        self.change("supabase", "Supabase Storage", "status",
                    lambda _: "FAKE_VERIFIED")
        self.validate(1, "unsupported evidence status")

    def library_doc(self):
        # Dynamic package choice: no hard-coded package names, versions or dates.
        return sorted(p for p in (self.root / "libraries").glob("*.md")
                      if p.name != "README.md")[0]

    def edit_library_field(self, field, transform):
        path = self.library_doc()
        body = path.read_text(encoding="utf-8")
        pattern = rf"(?m)^- \*\*{re.escape(field)}:\*\* (.*)$"
        match = re.search(pattern, body)
        self.assertIsNotNone(match, field)
        changed = body[:match.start(1)] + transform(match.group(1)) + body[match.end(1):]
        path.write_text(changed, encoding="utf-8")

    def test_library_missing_source_fails(self):
        self.edit_library_field("Official source", lambda _: "")
        self.validate(1, "required field Official source")

    def test_library_duplicate_identity_fails(self):
        doc = self.library_doc()
        body = doc.read_text()
        ids = re.findall(r"(?m)^- \*\*Package:\*\* (.+)$", body)
        self.assertGreaterEqual(len(ids), 2)
        body = body.replace("- **Package:** " + ids[1],
                            "- **Package:** " + ids[0], 1)
        doc.write_text(body)
        self.validate(1, "duplicate or empty package identity")

    def test_library_broken_reference_link_fails(self):
        doc = self.library_doc()
        doc.write_text(doc.read_text() + "\n[bad](missing-package-reference.md)\n")
        self.validate(1, "broken link")

    def test_library_invalid_date_fails(self):
        self.edit_library_field("Evidence reviewed", lambda _: "not-a-date")
        self.validate(1, "invalid evidence review date")

    def test_library_future_date_fails(self):
        future = (date.today() + timedelta(days=365)).isoformat()
        self.edit_library_field("Evidence reviewed", lambda _: future)
        self.validate(1, "future evidence review date")

    def test_library_missing_field_fails(self):
        doc = self.library_doc()
        body = doc.read_text()
        self.assertIn("- **Anti-fit:** ", body)
        doc.write_text(re.sub(r"(?m)^- \*\*Anti-fit:\*\* .*\n", "", body, count=1))
        self.validate(1, "required field Anti-fit")

    def test_library_unindexed_document_fails(self):
        (self.root / "libraries" / "other.md").write_text("# Other\n")
        self.validate(1, "unindexed or missing library document")

    def test_library_invalid_evidence_status_fails(self):
        self.edit_library_field("Evidence status", lambda _: "TRUST_ME")
        self.validate(1, "invalid evidence status")

    def test_library_unknown_compatibility_cannot_be_recommended(self):
        self.edit_library_field("Compatibility", lambda _: "UNKNOWN")
        self.validate(1, "unclear compatibility/license")

    def test_library_lowercase_unknown_cannot_be_recommended(self):
        self.edit_library_field("Compatibility", lambda _: "unknown")
        self.validate(1, "unclear compatibility/license")

    def test_library_stale_verified_review_fails(self):
        stale = (date.today() - timedelta(days=181)).isoformat()
        self.edit_library_field("Evidence reviewed", lambda _: stale)
        self.validate(1, "stale VERIFIED evidence review")

    def test_library_index_count_mismatch_fails(self):
        index = self.root / "libraries" / "README.md"
        content = index.read_text()
        match = re.search(r"(?m)^(\| [A-Za-z]+ \| )(\d+)( \|)", content)
        self.assertIsNotNone(match)
        value = int(match.group(2))
        content = content[:match.start(2)] + str(value + 1) + content[match.end(2):]
        index.write_text(content)
        self.validate(1, "index count mismatch")

    def test_library_syntactically_valid_wrong_source_fails(self):
        self.edit_library_field("Official source", lambda _: "[fake](https://github.com/unrelated/repo)")
        self.validate(1, "official source does not match package identity")

    def test_hyphenated_rustdoc_identity_is_strict(self):
        path = self.root / "libraries" / "rust.md"
        content = path.read_text(encoding="utf-8")
        good = "https://docs.rs/tower-http/latest/tower_http/"
        self.assertIn(good, content)
        path.write_text(content.replace(good, "https://docs.rs/tower-http/latest/other_http/", 1), encoding="utf-8")
        self.validate(1, "official source does not match package identity")

    def test_library_safe_partial_downgrade_passes(self):
        self.edit_library_field("Compatibility", lambda _: "UNKNOWN")
        self.edit_library_field("Evidence status", lambda _: "PARTIAL")
        self.edit_library_field("Selection", lambda _: "BLOCKED")
        self.validate(0, "STRUCTURE PASS")


    def test_library_taxonomy_inventory_and_selection_snapshot(self):
        index = (self.root / "libraries" / "README.md").read_text()
        section = index.split("## Canonical primary capabilities\n", 1)[1].split("\n## ", 1)[0]
        definitions = re.findall(r"(?m)^\| (C\d{2}) \| ([^|]+) \|$", section)
        self.assertEqual(len(definitions), 20)
        self.assertEqual([ident for ident, _ in definitions],
                         [f"C{i:02d}" for i in range(1, 21)])
        self.assertEqual(len({label.strip() for _, label in definitions}), 20)
        allowed = {f"{ident} — {label.strip()}" for ident, label in definitions}
        expected_packages = {
            "typescript": {"@modelcontextprotocol/client", "@modelcontextprotocol/server", "@opentelemetry/api", "@opentelemetry/sdk-trace", "@playwright/test", "@reduxjs/toolkit", "@tanstack/react-query", "@tanstack/react-table", "@tanstack/react-virtual", "@testing-library/react", "ai", "better-auth", "fuse.js", "jose", "jotai", "kysely", "motion", "next-intl", "openai", "pino", "radix-ui", "react-dropzone", "react-hook-form", "recharts", "swr", "undici", "valibot", "vitest", "zod", "zustand"},
            "swift": {"RevenueCat/purchases-ios", "airbnb/lottie-ios", "apple/swift-algorithms", "apple/swift-argument-parser", "apple/swift-async-algorithms", "apple/swift-collections", "apple/swift-crypto", "apple/swift-distributed-tracing", "apple/swift-log", "apple/swift-nio", "apple/swift-openapi-generator", "apple/swift-system", "groue/GRDB.swift", "kean/Nuke", "modelcontextprotocol/swift-sdk", "nicklockwood/SwiftFormat", "pointfreeco/swift-composable-architecture", "pointfreeco/swift-snapshot-testing", "realm/SwiftLint"},
            "rust": {"argon2", "axum-extra", "axum-test", "clap", "garde", "moka", "proptest", "rayon", "reqwest", "rmcp", "rustls", "serde", "sqlx", "thiserror", "tokio", "tonic", "tower-http", "tracing", "tracing-subscriber", "utoipa"},
            "go": {"github.com/cenkalti/backoff/v5", "github.com/gin-contrib/cors", "github.com/gin-contrib/sessions", "github.com/go-chi/chi/v5", "github.com/golang-jwt/jwt/v5", "github.com/google/go-cmp", "github.com/hibiken/asynq", "github.com/jackc/pgx/v5", "github.com/modelcontextprotocol/go-sdk", "github.com/openai/openai-go", "github.com/pressly/goose/v3", "github.com/redis/go-redis/v9", "github.com/rs/zerolog", "github.com/spf13/cobra", "github.com/stretchr/testify", "github.com/testcontainers/testcontainers-go", "go.opentelemetry.io/contrib/instrumentation/github.com/gin-gonic/gin/otelgin", "go.opentelemetry.io/otel/sdk", "golang.org/x/crypto", "golang.org/x/sync", "golang.org/x/time", "google.golang.org/grpc"},
            "python": {"celery", "cryptography", "httpx", "mcp", "numpy", "openai", "opentelemetry-sdk", "polars", "psycopg", "pydantic", "pytest", "SQLAlchemy", "structlog", "tenacity", "transformers", "typer", "uvicorn", "python-multipart", "pydantic-settings", "alembic", "Authlib", "pwdlib", "redis", "pytest-asyncio", "opentelemetry-instrumentation-fastapi", "ruff"},
        }
        expected_nondefault_gates = {
            "typescript/zod": "PARTIAL|BLOCKED",
            "typescript/pino": "PARTIAL|BLOCKED",
            "typescript/jose": "PARTIAL|BLOCKED",
            "typescript/better-auth": "PARTIAL|BLOCKED",
            "swift/modelcontextprotocol/swift-sdk": "PARTIAL|BLOCKED",
            "python/mcp": "PARTIAL|BLOCKED",
        }
        actual_nondefault_gates = {}
        for language, identities in expected_packages.items():
            body = (self.root / "libraries" / f"{language}.md").read_text()
            entries = body.split("## Entries\n", 1)[1].split("\n## ", 1)[0]
            chunks = re.split(r"(?m)^### `[^`\n]+`\s*$", entries)[1:]
            self.assertEqual(len(chunks), len(identities), language)
            actual = set()
            for chunk in chunks:
                def field(name):
                    return re.findall(rf"(?m)^- \*\*{re.escape(name)}:\*\* (.+)$", chunk)
                packages = field("Package")
                primary = field("Capability")
                status = field("Evidence status")
                choice = field("Selection")
                self.assertEqual(len(packages), 1)
                self.assertEqual(len(primary), 1)
                self.assertIn(primary[0], allowed)
                self.assertEqual(len(status), 1)
                self.assertEqual(len(choice), 1)
                package = packages[0].strip("`")
                actual.add(package)
                gate = f"{status[0]}|{choice[0]}"
                if gate != "VERIFIED|EVALUATE":
                    actual_nondefault_gates[f"{language}/{package}"] = gate
            self.assertEqual(actual, identities, language)
        self.assertEqual(actual_nondefault_gates, expected_nondefault_gates)

    def test_library_unknown_primary_capability_fails(self):
        self.edit_library_field("Capability", lambda _: "C99 — Unrecognized")
        self.validate(1, "invalid primary capability")

    def test_library_multiple_primary_capabilities_fail(self):
        self.edit_library_field("Capability", lambda value: value + ", C18 — Observability")
        self.validate(1, "invalid primary capability")

    def test_library_duplicate_canonical_id_fails(self):
        path = self.root / "libraries" / "README.md"
        body = path.read_text()
        self.assertIn("| C02 | Animation & Visualization |", body)
        path.write_text(body.replace("| C02 | Animation & Visualization |",
                                     "| C01 | Animation & Visualization |", 1))
        self.validate(1, "duplicate canonical capability ID")

    def test_library_missing_canonical_id_fails(self):
        path = self.root / "libraries" / "README.md"
        body = path.read_text()
        self.assertIn("| C20 | AI & Integrations |", body)
        path.write_text(body.replace("| C20 | AI & Integrations |\n", "", 1))
        self.validate(1, "exactly 20 canonical capability definitions")


if __name__ == "__main__":
    unittest.main()
