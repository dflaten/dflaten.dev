# dflaten.dev

This is the repo for my personal website, [dflaten.dev](https://www.dflaten.dev). It's plain
HTML and CSS with a small amount of JavaScript (the theme picker and syntax highlighting), plus a
single Python build script that converts blog posts from Markdown to HTML and generates the blog
index. I forked this from [@vijayp](https://github.com/arnath/vijayp.dev) as I
appreciated its minimal html/javascript and its ability to easily add new entries to a blog — two
things I had been looking for when trying to create my own site.

## Requirements

- [uv](https://docs.astral.sh/uv/) — fetches Python and the Python dependencies automatically.
- `make`
- [pandoc](https://pandoc.org/installing.html) — the build shells out to it to render Markdown.
  CI installs **3.1.11.1**; use the same version locally, since rendering can change between
  pandoc releases.

## Commands

| Command | What it does |
| --- | --- |
| `make build` | Builds the site into `dist/`. |
| `make serve` | Serves `dist/` at `http://localhost:8080` with Python's `http.server`. |
| `make test` | Runs the build's unit tests. |
| `make lint` | Runs `ruff` (via `uv run`). |
| `make typecheck` | Runs `pyrefly` (via `uv run`). |
| `make check` | Runs lint, typecheck, and tests — the same checks CI runs. |

## Development

Run `uv sync` after cloning to create the virtualenv. Typing is checked with
[pyrefly](https://pyrefly.org/) and linting with [ruff](https://docs.astral.sh/ruff/); both are
development dependencies.

## CI and deployment

`.github/workflows/ci.yaml` runs lint, typecheck, tests, and the build on every push to `main` and
on pull requests. Pushes to `main` (and manual dispatches) then deploy `dist/` to Cloudflare Pages
with `wrangler pages deploy`. Pull requests get the checks without the deploy.

## Search engines and AI crawlers

Search engines are welcome: `src/static/robots.txt` allows all crawlers and points at the
generated `sitemap.xml`.

AI crawlers, training bots, and agents are not. `robots.txt` disallows `GPTBot`, `OAI-SearchBot`,
`ChatGPT-User`, `ClaudeBot`, `Google-Extended`, `CCBot`, `PerplexityBot`, `Bytespider`, and a
number of others by name. To block another bot, add its user agent to that block.

`robots.txt` is voluntary, so this only stops crawlers that respect it. For enforcement at the
edge, enable Cloudflare's "Block AI bots" setting (WAF → Bots) for the zone as well.
