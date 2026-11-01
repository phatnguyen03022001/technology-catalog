"""Navigation and source-link hygiene for language knowledge-base profiles."""
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = ("rust", "go", "typescript", "python", "swift")
LINKS = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


class LanguageCatalogTests(unittest.TestCase):
    def test_five_profiles_linked_and_sourced(self):
        index = (ROOT / "languages" / "README.md").read_text()
        self.assertIn("(languages/README.md)", (ROOT / "README.md").read_text())
        for slug in LANGUAGES:
            with self.subTest(language=slug):
                self.assertIn(f"({slug}.md)", index)
                profile = ROOT / "languages" / f"{slug}.md"
                content = profile.read_text()
                for heading in ("## Fit & trade-offs", "## Ecosystem", "## Official evidence"):
                    self.assertIn(heading, content)
                links = [
                    uri for uri in LINKS.findall(content)
                    if urlparse(uri).scheme == "https"
                ]
                self.assertGreaterEqual(len(links), 3)

    def test_local_markdown_links_resolve(self):
        documents = [ROOT / "README.md", ROOT / "docs" / "00-taxonomy.md"]
        documents.extend((ROOT / "languages").glob("*.md"))
        for source in documents:
            for link in LINKS.findall(source.read_text()):
                local_path = unquote(link.split("#", 1)[0])
                if not local_path or urlparse(local_path).scheme or link.startswith("mailto:"):
                    continue
                with self.subTest(source=source.relative_to(ROOT).as_posix(), link=link):
                    self.assertTrue((source.parent / local_path).exists())


if __name__ == "__main__":
    unittest.main()
