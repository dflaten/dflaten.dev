import os
import shutil
from pathlib import Path

import pandoc
from frontmatter import Frontmatter
from typing import Any, cast
from datetime import datetime


def build() -> None:
    # This script writes output to the dist/ directory. If the directory exists,
    # delete it.
    output_directory: str = os.getenv("BUILD_DIR", "dist/")
    if os.path.exists(output_directory):
        shutil.rmtree(output_directory)

    # Copy src/static to dist/.
    shutil.copytree("src/static/", output_directory)

    # Load post template.
    with open("src/lib/blog/post-template.html", "r") as file:
        post_template: str = file.read()

    posts_directory: Path = Path("src/lib/blog/posts")
    post_dates: list[datetime] = []
    post_html_snippets: list[str] = []
    for file in posts_directory.glob("*.md"):
        slug = Path(file).stem

        # Read the frontmatter to get the title, date, and publish status.
        post: dict[str, str | Any | None] = Frontmatter.read_file(file)
        attributes: dict[str, Any] = cast(dict[str, Any], post["attributes"])
        title: str = attributes["title"]
        date: datetime = attributes["date"]
        date_string: str = date.strftime("%B %-d, %Y")

        # Convert the doc to HTML with Pandoc.
        doc = pandoc.read(source=post["body"], format="markdown")
        formatted_content = pandoc.write(doc, format="html")
        post_html = post_template.format(
            title=title,
            date=date,
            content=formatted_content,
        )

        # If the post isn't published, skip it.
        if not attributes["published"]:
            continue

        # Generate the HTML snippet for this post's link on the blog index.
        post_html_snippets.append(f"""
<div class="post">
    <a href="/blog/{slug}/"><h3>{title}</h3></a>
    <div class="subtext">{date_string}</div>
</div>
""")
        post_dates.append(date)

        # Write the formatted post to the output directory.
        post_path = os.path.join(output_directory, "blog", slug)
        os.makedirs(post_path, exist_ok=True)
        with open(os.path.join(post_path, "index.html"), "w") as file:
            file.write(post_html)

    # Sort the post snippets by descending date.
    sorted_pairs = sorted(zip(post_dates, post_html_snippets), reverse=True)
    sorted_snippets = [pair[1] for pair in sorted_pairs]

    # Write the blog index HTML.
    with open("src/lib/blog/index-template.html", "r") as file:
        index_template = file.read()
    index_html = index_template.format(posts=str.join("\n", sorted_snippets))
    with open(os.path.join(output_directory, "blog", "index.html"), "w") as file:
        file.write(index_html)


if __name__ == "__main__":
    build()
