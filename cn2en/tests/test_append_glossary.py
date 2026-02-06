import json
import subprocess
from pathlib import Path


def test_append_glossary_appends_and_restores():
    repo_root = Path(__file__).resolve().parents[2]
    script = repo_root / "cn2en" / "scripts" / "append_glossary.py"
    glossary = repo_root / "cn2en" / "references" / "glossary.jsonl"

    original = glossary.read_text(encoding="utf-8") if glossary.exists() else ""
    try:
        subprocess.check_call(
            [
                "python3",
                str(script),
                "--zh",
                "term_zh",
                "--en",
                "Term",
                "--source",
                "cn2en/tests/input.zh.md",
                "--context",
                "short snippet",
            ]
        )

        lines = glossary.read_text(encoding="utf-8").splitlines()
        assert lines, "glossary.jsonl should contain at least one entry"
        last = json.loads(lines[-1])
        assert last["zh"] == "term_zh"
        assert last["en"] == "Term"
        assert last["source"] == "cn2en/tests/input.zh.md"
    finally:
        glossary.write_text(original, encoding="utf-8")
