"""Frozen-clock, mock-network regression for read-only upstream monitoring."""
from __future__ import annotations

import shutil
import re
import tempfile
import unittest
from copy import deepcopy
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "monitor_upstream.py"
import sys
sys.path.insert(0, str(ROOT / "scripts"))
import monitor_upstream as m


class MonitorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = m.inventory()
        cls.library = next(r for r in cls.records if r["layer"] == "libraries"
                           and r["ecosystem"] == "typescript"
                           and r["baseline"])
        cls.provider = next(r for r in cls.records if r["layer"] == "providers"
                            and r["status"] == "VERIFIED")

    def test_inventory_covers_every_layer_and_dynamic_library_count(self):
        from collections import Counter
        counts = Counter(r["layer"] for r in self.records)
        expected = {
            layer: len([p for p in (ROOT / layer).glob("*.md")
                        if p.name != "README.md"])
            for layer in ("languages", "frameworks", "decisions")
        }
        expected["libraries"] = sum(
            len(re.findall(r"(?m)^### ", p.read_text()))
            for p in (ROOT / "libraries").glob("*.md") if p.name != "README.md"
        )
        expected["providers"] = sum(
            len(m.service_rows(p)) for p in (ROOT / "providers").glob("*.md")
            if p.name != "README.md"
        )
        self.assertEqual(counts, expected)
        self.assertEqual(len({(r["layer"], r.get("ecosystem"), r["name"])
                              for r in self.records}), len(self.records))

    def test_frozen_day29_day30_day31(self):
        day = date(2026, 4, 30)
        row = {"reviewed": day.isoformat(), "status": "VERIFIED"}
        for days, expected in [(29, "CURRENT"), (30, "CURRENT"),
                               (31, "REVERIFY_REQUIRED")]:
            with self.subTest(days=days):
                self.assertEqual(m.freshness(row, day + timedelta(days=days)),
                                 (expected, days))

    def test_age_warns_without_downgrading_verified(self):
        old = deepcopy(self.provider)
        old["reviewed"] = "2020-01-01"
        result = m.evaluate([old], date(2026, 4, 1))[0]
        self.assertEqual(result["freshness"], "REVERIFY_REQUIRED")
        self.assertEqual(result["status"], "VERIFIED")
        self.assertEqual(result["production_use"], "BLOCK_REVERIFY")

    def test_invalid_future_and_non_iso_date_fail(self):
        row = deepcopy(self.provider)
        for bad in ["2026-02-30", "not-a-date", "2026-1-02", "2026-13-01"]:
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                row["reviewed"] = bad
                m.freshness(row, date(2026, 3, 1))
        row["reviewed"] = "2026-04-01"
        with self.assertRaisesRegex(ValueError, "future"):
            m.freshness(row, date(2026, 3, 1))

    def test_missing_date_is_unknown_not_current(self):
        row = deepcopy(self.library)
        row["reviewed"] = ""
        self.assertEqual(m.freshness(row, m.parse_date(self.library["reviewed"])), ("UNKNOWN", None))
        self.assertEqual(m.evaluate([row], m.parse_date(self.library["reviewed"]))[0]["production_use"],
                         "BLOCK_REVERIFY")

    def test_new_release_is_signal_not_automatic_update(self):
        row = deepcopy(self.library)
        original = deepcopy(row)
        def mock(url, body=None):
            return {"version": "999.0.0"}
        result = m.evaluate([row], m.parse_date(self.library["reviewed"]), live=True, fetch=mock)[0]
        self.assertEqual(result["signal"], "UPSTREAM_CHANGED")
        self.assertEqual(result["production_use"], "BLOCK_REVERIFY")
        self.assertEqual(row, original)
        self.assertIn("Recorded", result["detail"])

    def test_existing_version_is_no_change_signal_not_certification(self):
        row = deepcopy(self.library)
        result = m.evaluate([row], m.parse_date(self.library["reviewed"]), live=True,
                            fetch=lambda u, body=None: {"version": row["baseline"]})[0]
        self.assertEqual(result["signal"], "NO_CHANGE_DETECTED")
        self.assertEqual(result["status"], row["status"])
        self.assertEqual(result["reviewed"], row["reviewed"])

    def test_network_failure_never_means_unchanged(self):
        row = deepcopy(self.library)
        def failed(url, body=None):
            raise OSError("offline")
        result = m.evaluate([row], m.parse_date(self.library["reviewed"]), live=True, fetch=failed)[0]
        self.assertEqual(result["signal"], "CHECK_FAILED")
        self.assertEqual(result["production_use"], "BLOCK_REVERIFY")

    def test_confirmed_breaking_release_blocks_current_evidence(self):
        framework = next(r for r in self.records if r["layer"] == "frameworks"
                         and r.get("github_repo"))
        when = (m.parse_date(framework["reviewed"]) + timedelta(days=1)).isoformat()
        def fake(url, body=None):
            return {"tag_name": "v99.0.0", "published_at": when + "T00:00:00Z",
                    "body": "## Breaking Changes\nRemoved deprecated API"}
        result = m.evaluate([framework], m.parse_date(framework["reviewed"]),
                            live=True, fetch=fake)[0]
        self.assertEqual(result["freshness"], "CURRENT")
        self.assertEqual(result["signal"], "UPSTREAM_CHANGED")
        self.assertEqual(result["production_use"], "BLOCK_REVERIFY")
        self.assertIn("Release", result["detail"])
        self.assertIn("BREAKING_CHANGE", result["detail"])

    def test_old_framework_release_no_false_positive(self):
        framework = next(r for r in self.records if r["layer"] == "frameworks"
                         and r.get("github_repo"))
        def fake(url, body=None):
            return {"tag_name": "v1", "published_at": "2020-01-01T00:00:00Z"}
        result = m.probe(framework, fake)
        self.assertEqual(result["signal"], "NO_CHANGE_DETECTED")

    def test_version_scoped_advisory_triggers_review(self):
        row = deepcopy(self.library)
        def fake(url, body=None):
            if "osv.dev" in url:
                self.assertEqual(body["version"], row["baseline"].removeprefix("v"))
                return {"vulns": [{"id": "GHSA-test-123"}]}
            return {"version": row["baseline"]}
        result = m.probe(row, fake, security=True)
        self.assertEqual(result["signal"], "SECURITY_REVIEW_REQUIRED")
        self.assertEqual(result["security"], "ADVISORY_FOUND")
        self.assertIn("GHSA-test-123", result["detail"])

    def test_newer_published_advisory_is_change_signal(self):
        row = deepcopy(self.library)
        future = (m.parse_date(row["reviewed"]) + timedelta(days=1)).isoformat()
        def fake(url, body=None):
            if "osv.dev" in url:
                return {"vulns": [{"id": "GHSA-test", "published": future + "T00:00:00Z"}]}
            return {"version": row["baseline"]}
        result = m.probe(row, fake, security=True)
        self.assertEqual(result["signal"], "UPSTREAM_CHANGED")

    def test_release_failure_and_advisory_keep_check_failed(self):
        row = deepcopy(self.library)
        def fake(url, body=None):
            if "osv.dev" in url:
                return {"vulns": [{"id": "GHSA-test"}]}
            raise OSError("unreachable")
        result = m.probe(row, fake, security=True)
        self.assertEqual(result["signal"], "CHECK_FAILED")
        self.assertEqual(result["security"], "ADVISORY_FOUND")
        self.assertIn("https://osv.dev/vulnerability/GHSA-test", result["detail"])

    def test_security_query_failure_and_pagination_not_silent(self):
        row = deepcopy(self.library)
        for response in [{"next_page_token": "next", "vulns": []},
                         {"vulns": "wrong type"}]:
            def fake(url, body=None):
                return response if "osv.dev" in url else {"version": row["baseline"]}
            signal = m.probe(row, fake, security=True)
            self.assertEqual(signal["signal"], "CHECK_FAILED")

    def test_swift_advisory_coverage_is_explicit_unknown(self):
        swift = next(r for r in self.records if r.get("ecosystem") == "swift")
        self.assertEqual(m.advisories(swift, lambda *_: self.fail("no call"))[0],
                         "UNKNOWN")

    def test_manual_only_provider_does_not_fetch_arbitrary_prices(self):
        def unexpected(*args):
            self.fail("must not probe opaque provider pricing endpoint")
        result = m.probe(self.provider, unexpected)
        self.assertEqual(result["signal"], "UNKNOWN")

    def test_partial_library_never_production_ready(self):
        row = deepcopy(self.library)
        row["status"], row["selection"] = "PARTIAL", "BLOCKED"
        result = m.evaluate([row], m.parse_date(row["reviewed"]))[0]
        self.assertEqual(result["production_use"], "BLOCK_REVERIFY")

    def test_confirmation_never_writes_or_fakes_date(self):
        text_before = SCRIPT.read_bytes()
        path = ROOT / self.library["path"]
        content_before = path.read_bytes()
        m.evaluate([self.library], m.parse_date(self.library["reviewed"]), live=True,
                   fetch=lambda url, body=None: {"version": "2027.0.0"})
        self.assertEqual(SCRIPT.read_bytes(), text_before)
        self.assertEqual(path.read_bytes(), content_before)

    def test_rerun_idempotent_and_no_git_or_storage_mutation(self):
        frozen = m.parse_date(self.library["reviewed"])
        before = m.render(m.evaluate(self.records, frozen), frozen)
        after = m.render(m.evaluate(self.records, frozen), frozen)
        self.assertEqual(before, after)
        self.assertNotIn("git commit", before)

    def test_new_library_identity_in_existing_doc_auto_discovered(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for name in ("languages", "frameworks", "libraries", "decisions", "providers"):
                shutil.copytree(ROOT / name, root / name)
            target = root / "libraries" / "rust.md"
            content = target.read_text()
            start = content.index("### ")
            stop = content.find("\n### ", start + 4)
            block = content[start:stop]
            original = next(r for r in self.records if r["layer"] == "libraries"
                            and r["ecosystem"] == "rust")
            changed = block.replace(original["name"], "synthetic-library-for-test")
            target.write_text(content[:stop] + "\n" + changed + content[stop:])
            # New entry is deliberately not published. Parser must pick it up.
            rows = m.inventory(root)
            libs = [r for r in rows if r["layer"] == "libraries"]
            self.assertEqual(len(libs), sum(r['layer'] == 'libraries' for r in self.records) + 1)
            new = next(r for r in libs if r["name"] == "synthetic-library-for-test")
            self.assertEqual(m.freshness(new, m.parse_date(new["reviewed"]))[0], "CURRENT")

    def test_duplicate_package_rejected_dynamically(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for name in ("languages", "frameworks", "libraries", "decisions", "providers"):
                shutil.copytree(ROOT / name, root / name)
            target = root / "libraries" / "rust.md"
            content = target.read_text()
            start = content.index("### ")
            stop = content.find("\n### ", start + 4)
            target.write_text(content[:stop] + "\n" + content[start:stop] + content[stop:])
            with self.assertRaisesRegex(ValueError, "duplicate"):
                m.inventory(root)


if __name__ == "__main__":
    unittest.main()
