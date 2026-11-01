"""Dynamic structural coverage for all framework and decision records.

These checks are not assessments of source truth, pricing, benchmark quality
or production approval. The catalog validator applies the stronger gates.
"""
from datetime import date, datetime, timezone
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
FRAMEWORK_SECTIONS = (
    "Fit", "Anti-fit", "Compatibility", "Maturity & maintenance", "Licensing",
    "Operational / test evidence needed", "Official evidence",
)
DECISION_SECTIONS = (
    "Workload & candidates", "Decision & falsification",
    "Verification / TCO / fallback", "Official evidence",
)


class TechnologyKnowledgeBaseTests(unittest.TestCase):
    def test_all_framework_profiles_are_indexed_and_have_sections(self):
        index = (ROOT / "frameworks" / "README.md").read_text()
        for language in ("TypeScript", "Python", "Go", "Rust", "Swift"):
            self.assertIn(language, index)
        records = sorted(p for p in (ROOT / "frameworks").glob("*.md")
                         if p.name != "README.md")
        self.assertTrue(records, "framework catalog must have profiles")
        for doc in records:
            with self.subTest(profile=doc.name):
                self.assertEqual(index.count(f"({doc.name})"), 1)
                text = doc.read_text()
                for heading in FRAMEWORK_SECTIONS:
                    self.assertIn(f"## {heading}", text)
                self.assertGreaterEqual(len(re.findall(r"\]\(https://", text)), 2)
                self.assert_valid_review_date(text)

    def test_all_decisions_are_indexed_and_have_sections(self):
        index = (ROOT / "decisions" / "README.md").read_text()
        records = sorted(p for p in (ROOT / "decisions").glob("*.md")
                         if p.name != "README.md")
        self.assertTrue(records, "decision catalog must have records")
        for doc in records:
            with self.subTest(decision=doc.name):
                self.assertEqual(index.count(f"({doc.name})"), 1)
                text = doc.read_text()
                self.assert_valid_review_date(text)
                for heading in DECISION_SECTIONS:
                    self.assertIn(f"## {heading}", text)
                self.assertIn("## Hard gates", text)
                status = re.findall(r"\*\*Status:\*\*\s+([A-Z_]+)", text)
                self.assertEqual(len(status), 1)
                self.assertIn(status[0], ("CONDITIONAL_NOT_PRODUCTION",
                                           "APPROVED_FOR_PRODUCTION"))
                if status[0] == "CONDITIONAL_NOT_PRODUCTION":
                    self.assertNotIn("APPROVED_FOR_PRODUCTION", text)

    def assert_valid_review_date(self, text):
        matches = re.findall(r"\*\*Reviewed:\*\*\s+(\S+)", text)
        self.assertEqual(len(matches), 1)
        self.assertRegex(matches[0], r"^\d{4}-\d{2}-\d{2}$")
        self.assertLessEqual(date.fromisoformat(matches[0]), datetime.now(timezone.utc).date())

    def test_navigation_is_present(self):
        index = (ROOT / "README.md").read_text()
        for path in ("languages/README.md", "frameworks/README.md",
                     "decisions/README.md"):
            self.assertIn(f"({path})", index)


if __name__ == "__main__":
    unittest.main()
