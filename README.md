# dflaten.dev

This is the repo for my personal website, [dflaten.dev](https://www.dflaten.dev). It's written using
plain HTML and CSS (there's actually no Javascript at all), along with a single Python build script
that converts my blog posts from Markdown to HTML and creates the blog index page. I forked this
from [@vijayp](https://github.com/arnath/vijayp.dev) as I appreciated its minimal html/javascript and
its ability to easily add new entries to a blog two things I had been looking for when trying to 
create my own site.

## Usage

This repo uses make and [uv](https://docs.astral.sh/uv/) as build tools. Any other tools (including
Python) will be automatically fetched by the commands below. Once you have those, there are only two
commands:

- `make build` - Builds the site and outputs it into the `dist/` folder.
- `make serve` - Uses Python's `http.server` to serve the website at `http://localhost:8080`.

## Changes
For python development (build script) use `uv sync` to setup your venv after cloning the repo. 

For typing I'm using [pyrefly](https://pyrefly.org/), check typing with `uv run pyrefly check`.