import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import build


class BuildScriptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.output_dir = Path(cls.temp_dir.name) / "dist"

        with patch.dict(os.environ, {"BUILD_DIR": str(cls.output_dir)}, clear=False):
            build.build()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temp_dir.cleanup()

    def read_output(self, relative_path: str) -> str:
        return (self.output_dir / relative_path).read_text()

    def test_build_copies_static_site_assets(self) -> None:
        self.assertTrue((self.output_dir / "index.html").exists())
        self.assertTrue((self.output_dir / "root.css").exists())
        self.assertTrue((self.output_dir / "theme.js").exists())
        self.assertTrue((self.output_dir / "projects" / "index.html").exists())
        self.assertTrue((self.output_dir / "blog" / "index.css").exists())

    def test_build_generates_only_published_blog_posts(self) -> None:
        self.assertTrue(
            (self.output_dir / "blog" / "creating-alexa-replacement" / "index.html").exists()
        )
        self.assertTrue(
            (self.output_dir / "blog" / "doing-code-reviews" / "index.html").exists()
        )
        self.assertFalse(
            (self.output_dir / "blog" / "building-custom-llm" / "index.html").exists()
        )

    def test_blog_index_lists_posts_in_descending_date_order(self) -> None:
        blog_index = self.read_output("blog/index.html")

        ordered_titles = [
            "Creating and Alexa Replacement using Codex",
            "Building a Postman Replacement",
            "Self Hosting a Personal Photo/Video Storage System",
            "Learning Linux with Arch Linux",
            "Doing Good Code Reviews",
            "Setting up access for a personal AWS Account",
            "A self taught classical education",
            "Launching my Personal Website",
        ]

        positions = [blog_index.index(title) for title in ordered_titles]
        self.assertEqual(positions, sorted(positions))

    def test_homepage_and_shared_css_include_dark_mode_support(self) -> None:
        homepage = self.read_output("index.html")
        root_css = self.read_output("root.css")

        self.assertIn('data-theme-menu', homepage)
        self.assertIn('aria-label="Theme settings"', homepage)
        self.assertIn('data-theme-current-label', homepage)
        self.assertIn('<svg', homepage)
        self.assertIn('data-theme-option="auto"', homepage)
        self.assertIn('data-theme-option="light"', homepage)
        self.assertIn('data-theme-option="dark"', homepage)
        self.assertIn('class="github-social-icon"', homepage)
        self.assertIn('src="/theme.js"', homepage)
        self.assertNotIn("window.themePreference.initializeTheme()", homepage)
        self.assertIn(".theme-picker-menu", root_css)
        self.assertIn(".theme-picker summary::marker", root_css)
        self.assertIn("@media (max-width: 640px)", root_css)
        self.assertIn(".nav-bar-social-link img", root_css)
        self.assertIn("@media (prefers-color-scheme: dark)", root_css)
        self.assertIn(':root[data-theme="dark"]', root_css)
        self.assertIn("color-scheme: light dark;", root_css)
        self.assertIn("--color-background: #11161d;", root_css)

    def test_generated_post_page_contains_post_template_content(self) -> None:
        post_page = self.read_output("blog/doing-code-reviews/index.html")

        self.assertIn("<h1>Doing Good Code Reviews</h1>", post_page)
        self.assertIn('<div class="subtext">2025-07-13</div>', post_page)
        self.assertIn("hljs.highlightAll();", post_page)


if __name__ == "__main__":
    unittest.main()
