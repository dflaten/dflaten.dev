import os
import re
import shutil
import subprocess
from datetime import date
from html import escape, unescape
from pathlib import Path
from typing import Any, cast

from frontmatter import Frontmatter

SITE_URL = "https://www.dflaten.dev"
SUMMARY_LENGTH = 160


def markdown_to_html(source: str) -> str:
    """Convert a Markdown document body to HTML using the pandoc CLI."""
    result = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "html"],
        input=source,
        capture_output=True,
        encoding="utf-8",
        check=True,
    )
    return result.stdout


def summarize(html_content: str, limit: int = SUMMARY_LENGTH) -> str:
    """Build a plain-text summary of rendered HTML for meta descriptions."""
    text = " ".join(unescape(re.sub(r"<[^>]+>", " ", html_content)).split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def read_post(file: Path) -> tuple[dict[str, Any], str]:
    """Read a post's frontmatter, validating the fields the build requires."""
    post = Frontmatter.read_file(file)
    attributes = cast(dict[str, Any], post["attributes"])
    for field in ("title", "date", "published"):
        if field not in attributes:
            raise ValueError(f"{file}: frontmatter is missing required field {field!r}")
    body = post["body"]
    if not isinstance(body, str):
        raise TypeError(f"{file}: no Markdown body found after the frontmatter")
    return attributes, body


def format_date(value: date) -> str:
    """Format a date as e.g. 'July 13, 2025' without platform-specific strftime flags."""
    return f"{value:%B} {value.day}, {value.year}"


def write_sitemap(
    output_directory: str, posts: list[tuple[str, date]]
) -> None:
    """Write sitemap.xml covering the static pages and published posts."""
    entries: list[tuple[str, date | None]] = [
        (f"{SITE_URL}/", None),
        (f"{SITE_URL}/blog/", None),
        (f"{SITE_URL}/projects/", None),
    ]
    entries.extend((f"{SITE_URL}/blog/{slug}/", published) for slug, published in posts)

    urls = []
    for loc, lastmod in entries:
        if lastmod is None:
            urls.append(f"    <url><loc>{loc}</loc></url>")
        else:
            urls.append(
                f"    <url><loc>{loc}</loc>"
                f"<lastmod>{lastmod.isoformat()}</lastmod></url>"
            )

    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    sitemap_path = os.path.join(output_directory, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as file:
        file.write(sitemap)


def build() -> None:
    # This script writes output to the dist/ directory. If the directory exists,
    # delete it.
    output_directory: str = os.getenv("BUILD_DIR", "dist/")
    if os.path.exists(output_directory):
        shutil.rmtree(output_directory)

    # Copy src/static to dist/.
    shutil.copytree("src/static/", output_directory)

    # Load post template.
    post_template = Path("src/lib/blog/post-template.html").read_text(encoding="utf-8")

    posts_directory: Path = Path("src/lib/blog/posts")
    post_dates: list[date] = []
    post_html_snippets: list[str] = []
    published_posts: list[tuple[str, date]] = []
    for file in sorted(posts_directory.glob("*.md")):
        slug = file.stem

        # Read the frontmatter to get the title, date, and publish status.
        attributes, body = read_post(file)

        # If the post isn't published, skip it before doing any conversion work.
        if not attributes["published"]:
            continue

        title = cast(str, attributes["title"])
        post_date = cast(date, attributes["date"])
        date_string: str = format_date(post_date)

        # Convert the doc to HTML with Pandoc.
        formatted_content = markdown_to_html(body)
        post_url = f"{SITE_URL}/blog/{slug}/"
        post_html = post_template.format(
            title=escape(title),
            date=date_string,
            description=escape(summarize(formatted_content)),
            url=post_url,
            content=formatted_content,
        )

        # Generate the HTML snippet for this post's link on the blog index.
        post_html_snippets.append(f"""
<div class="post">
    <a href="/blog/{slug}/"><h3>{escape(title)}</h3></a>
    <div class="subtext">{date_string}</div>
</div>
""")
        post_dates.append(post_date)
        published_posts.append((slug, post_date))

        # Write the formatted post to the output directory.
        post_path = os.path.join(output_directory, "blog", slug)
        os.makedirs(post_path, exist_ok=True)
        with open(
            os.path.join(post_path, "index.html"), "w", encoding="utf-8"
        ) as file:
            file.write(post_html)

    # Sort the post snippets by descending date.
    sorted_pairs = sorted(
        zip(post_dates, post_html_snippets), key=lambda pair: pair[0], reverse=True
    )
    sorted_snippets = [pair[1] for pair in sorted_pairs]

    # Write the blog index HTML.
    index_template = Path("src/lib/blog/index-template.html").read_text(encoding="utf-8")
    index_html = index_template.format(
        posts="\n".join(sorted_snippets), url=f"{SITE_URL}/blog/"
    )
    with open(
        os.path.join(output_directory, "blog", "index.html"), "w", encoding="utf-8"
    ) as file:
        file.write(index_html)

    write_sitemap(output_directory, published_posts)


if __name__ == "__main__":
    build()
