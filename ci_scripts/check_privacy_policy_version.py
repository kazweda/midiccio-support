#!/usr/bin/env python3
"""Validate privacy policy version metadata.

Checks that each policy file's front matter `version`/`lastUpdated`
match the top row of its "9. Policy Version History" table, and that
the Japanese and English policies agree on the current version.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

JA_PATH = Path("PRIVACY_POLICY.md")
EN_PATH = Path("PRIVACY_POLICY_EN.md")

HISTORY_TOP_ROW_RE = re.compile(
    r"^## 9\..*?\n\n\|.*\|\n\|[-| ]+\|\n\| *([^|]+?) *\| *([^|]+?) *\|",
    re.MULTILINE | re.DOTALL,
)


def parse_front_matter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    meta: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip()
    return meta


def top_history_row(text: str) -> tuple[str, str]:
    match = HISTORY_TOP_ROW_RE.search(text)
    if not match:
        raise ValueError("could not find the '9. Version History' table")
    return match.group(1).strip(), match.group(2).strip()


def check(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    meta = parse_front_matter(text)

    fm_version = meta.get("version")
    fm_last_updated = meta.get("lastUpdated")
    if not fm_version:
        raise ValueError(f"{path}: missing 'version' in front matter")
    if not fm_last_updated:
        raise ValueError(f"{path}: missing 'lastUpdated' in front matter")

    table_version, table_date = top_history_row(text)

    errors = []
    if fm_version != table_version:
        errors.append(
            f"{path}: front matter version '{fm_version}' does not match "
            f"the top version history row '{table_version}'"
        )
    if fm_last_updated != table_date:
        errors.append(
            f"{path}: front matter lastUpdated '{fm_last_updated}' does not "
            f"match the top version history date '{table_date}'"
        )
    if errors:
        raise ValueError("\n".join(errors))

    return fm_version


def main() -> int:
    errors: list[str] = []
    versions: dict[Path, str] = {}

    for path in (JA_PATH, EN_PATH):
        try:
            versions[path] = check(path)
        except ValueError as exc:
            errors.append(str(exc))

    if JA_PATH in versions and EN_PATH in versions and versions[JA_PATH] != versions[EN_PATH]:
        errors.append(
            f"version mismatch between policies: {JA_PATH} is "
            f"{versions[JA_PATH]}, {EN_PATH} is {versions[EN_PATH]}"
        )

    if errors:
        for err in errors:
            print(f"::error::{err}", file=sys.stderr)
        return 1

    print(f"OK: privacy policy version {versions[JA_PATH]} is consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
