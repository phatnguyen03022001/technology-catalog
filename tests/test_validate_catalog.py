"""Regression tests for deterministic catalog validation (stdlib only)."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
FIELDS = {"free": 4, "paid": 5, "caveat": 6, "source": 7, "status": 8, "checked": 9}


class CatalogMutationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ("providers", "pillars", "docs", "scripts", "languages", "frameworks", "decisions"):
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


if __name__ == "__main__":
    unittest.main()
