from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CASES = sorted((ROOT / "cases").glob("*/case.json"))


def load_catalog() -> list[dict[str, Any]]:
    return [json.loads(path.read_text(encoding="utf-8")) for path in CASES]


def render_markdown(items: list[dict[str, Any]]) -> str:
    lines = ["# Audit catalog", "", "| Case | Risk | Invariant |", "| --- | --- | --- |"]
    for item in items:
        lines.append(f"| {item['title']} | {item['severity']} | {item['invariant']} |")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="List the independent security audit cases.")
    parser.add_argument("--format", choices=("text", "json", "markdown"), default="text")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    items = load_catalog()
    if args.format == "json":
        output = json.dumps(items, indent=2) + "\n"
    elif args.format == "markdown":
        output = render_markdown(items)
    else:
        output = "\n".join(f"{item['id']}: {item['title']} [{item['severity']}]" for item in items) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
