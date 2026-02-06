import json
import subprocess
from pathlib import Path


def test_append_glossary_appends_and_restores(tmp_path: Path):
    repo_root = Path(__file__).resolve().parents[2]
    script = repo_root / "cn2en" / "scripts" / "append_glossary.py"
    glossary = repo_root / "cn2en" / "references" / "glossary.jsonl"

    payload = {"term_zh": "Term", "科研": "research"}
    payload_path = tmp_path / "glossary.json"
    payload_path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

    original = glossary.read_text(encoding="utf-8") if glossary.exists() else ""
    try:
        subprocess.check_call(
            [
                "python3",
                str(script),
                "--input",
                str(payload_path),
                "--source",
                "cn2en/tests/input.zh.md",
                "--context",
                "short snippet",
            ]
        )

        lines = glossary.read_text(encoding="utf-8").splitlines()
        assert lines, "glossary.jsonl should contain at least one entry"
        last = json.loads(lines[-1])
        assert last["zh"] in payload
        assert last["en"] == payload[last["zh"]]
        assert last["source"] == "cn2en/tests/input.zh.md"
    finally:
        glossary.write_text(original, encoding="utf-8")
