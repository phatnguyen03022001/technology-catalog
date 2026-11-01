"""Structural contract only: semantics, versions, prices and benchmarks need review."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
FRAMEWORKS = ("nextjs", "nestjs", "fastapi", "django", "gin", "axum", "swiftui", "vapor")
DECISIONS = ("web-fullstack", "python-ai-api", "network-service", "apple-native")


class TechnologyKnowledgeBaseTests(unittest.TestCase):
    def test_five_languages_have_framework_coverage(self):
        index = (ROOT / "frameworks" / "README.md").read_text()
        for language in ("TypeScript", "Python", "Go", "Rust", "Swift"):
            self.assertIn(language, index)
        for name in FRAMEWORKS:
            with self.subTest(framework=name):
                doc = ROOT / "frameworks" / (name + ".md")
                self.assertIn(f"({name}.md)", index)
                text = doc.read_text()
                for heading in ("## Fit", "## Anti-fit", "## Compatibility",
                                "## Maturity & maintenance", "## Licensing",
                                "## Operational / test evidence needed", "## Official evidence"):
                    self.assertIn(heading, text)
                self.assertGreaterEqual(len(re.findall(r"\]\(https://", text)), 2)
                self.assertIn("2026-11-01", text)

    def test_reference_decisions_state_unmeasured_limits(self):
        index = (ROOT / "decisions" / "README.md").read_text()
        for name in DECISIONS:
            with self.subTest(decision=name):
                doc = ROOT / "decisions" / (name + ".md")
                self.assertIn(f"({name}.md)", index)
                text = doc.read_text()
                self.assertIn("CONDITIONAL_NOT_PRODUCTION", text)
                self.assertIn("REFERENCE_SCENARIO_NOT_MEASURED", text)
                self.assertIn("NOT_MEASURED", text)
                for heading in ("## Workload & candidates", "## Hard gates",
                                "## Decision & falsification", "## Verification / TCO / fallback",
                                "## Official evidence"):
                    self.assertIn(heading, text)
                self.assertIn("UNKNOWN", text)
                self.assertGreaterEqual(len(re.findall(r"\]\(https://", text)), 2)

    def test_navigation_is_present(self):
        index = (ROOT / "README.md").read_text()
        for path in ("languages/README.md", "frameworks/README.md", "decisions/README.md"):
            self.assertIn(f"({path})", index)


if __name__ == "__main__":
    unittest.main()
