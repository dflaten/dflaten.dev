.PHONY: build serve deploy

build:
	uv run build.py

serve:
	uv run python -m http.server 8080 --directory dist

deploy:
	npm install @cloudflare/uv
	uv run build.py
