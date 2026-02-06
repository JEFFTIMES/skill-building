#!/usr/bin/env python3
"""Append a term entry to references/glossary.jsonl.

Usage:
  python scripts/append_glossary.py --zh "term_zh" --en "Term" --source "path.md" --context "short snippet"
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Append a glossary term to glossary.jsonl")
    parser.add_argument("--zh", required=True, help="Chinese term")
    parser.add_argument("--en", required=True, help="English term")
    parser.add_argument("--source", required=True, help="Source file path or origin")
    parser.add_argument("--context", required=True, help="Short context snippet")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    entry = {
        "zh": args.zh,
        "en": args.en,
        "source": args.source,
        "context": args.context,
        "added_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }

    glossary_path = Path(__file__).resolve().parents[1] / "references" / "glossary.jsonl"
    glossary_path.parent.mkdir(parents=True, exist_ok=True)

    with glossary_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
