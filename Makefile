.PHONY: build serve test

build:
	uv run build.py

serve:
	uv run python -m http.server 8080 --directory dist

test:
	TMPDIR=/tmp UV_CACHE_DIR=/tmp/uv-cache uv run python -m unittest discover -s tests -p 'test_*.py'
