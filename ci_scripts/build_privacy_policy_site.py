#!/usr/bin/env python3

from __future__ import annotations

import argparse
import html
from pathlib import Path

import markdown


def parse_front_matter(content: str) -> tuple[dict[str, str], str]:
    if not content.startswith("---\n"):
        return {}, content

    end = content.find("\n---\n", 4)
    if end == -1:
        return {}, content

    header = content[4:end]
    body = content[end + 5:]
    meta: dict[str, str] = {}
    for line in header.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip()
    return meta, body


def build_html(markdown_text: str, meta: dict[str, str]) -> str:
    title = meta.get("title", "midiccio Privacy Policy")
    description = meta.get(
        "description",
        "midiccio プライバシーポリシー",
    )
    last_updated = meta.get("lastUpdated", "")
    lang = meta.get("lang", "ja")
    updated_label = meta.get("updatedLabel", "最終更新")

    rendered = markdown.markdown(
        markdown_text,
        extensions=["tables", "fenced_code", "sane_lists", "nl2br"],
    )

    updated_text = (
        f"<p class=\"updated\">{html.escape(updated_label)}: "
        f"{html.escape(last_updated)}</p>"
        if last_updated
        else ""
    )
    csp_content = (
        "default-src 'none'; style-src 'unsafe-inline'; "
        "img-src https: data:; base-uri 'none'; "
        "form-action 'none'; frame-ancestors 'none';"
    )

    return f"""<!doctype html>
<html lang=\"{html.escape(lang)}\">
  <head>
    <meta charset=\"utf-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
    <meta
      http-equiv=\"Content-Security-Policy\"
      content=\"{html.escape(csp_content)}\"
    />
    <title>{html.escape(title)}</title>
    <meta name=\"description\" content=\"{html.escape(description)}\" />
    <style>
      :root {{
        color-scheme: light dark;
      }}
      body {{
        margin: 0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
          sans-serif;
        line-height: 1.7;
      }}
      main {{
        max-width: 860px;
        margin: 0 auto;
        padding: 2rem 1.25rem 4rem;
      }}
      h1, h2, h3 {{
        line-height: 1.35;
      }}
      table {{
        width: 100%;
        border-collapse: collapse;
        margin: 1rem 0 1.5rem;
      }}
      th, td {{
        border: 1px solid #8884;
        padding: 0.5rem 0.625rem;
        text-align: left;
        vertical-align: top;
      }}
      code {{
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas,
          "Liberation Mono", monospace;
      }}
      pre {{
        overflow-x: auto;
        padding: 0.75rem;
        border-radius: 8px;
        background: #8882;
      }}
      .updated {{
        color: #666;
        font-size: 0.95rem;
      }}
    </style>
  </head>
  <body>
    <main>
      {updated_text}
      {rendered}
    </main>
  </body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build privacy policy HTML from Markdown"
    )
    parser.add_argument(
        "--input", required=True, help="Input markdown file path"
    )
    parser.add_argument(
        "--output", required=True, help="Output html file path"
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    raw = input_path.read_text(encoding="utf-8")
    meta, markdown_body = parse_front_matter(raw)
    html_doc = build_html(markdown_body, meta)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html_doc, encoding="utf-8")


if __name__ == "__main__":
    main()
