import json
import subprocess
from pathlib import Path


def test_extract_then_insert(tmp_path: Path):
    input_md = tmp_path / "sample.md"
    input_md.write_text(
        "---\n"
        "title: 示例\n"
        "---\n\n"
        "# 标题\n\n"
        "这是一个段落。\n\n"
        "- 列表项\n\n"
        "```python\n"
        "print(\"hello\")\n"
        "```\n",
        encoding="utf-8",
    )

    repo_root = Path(__file__).resolve().parents[2]
    extract = repo_root / "cn2en" / "scripts" / "extract_cn_blocks.py"
    insert = repo_root / "cn2en" / "scripts" / "insert_en_blocks.py"

    subprocess.check_call(["python3", str(extract), "--input", str(input_md)])

    output_md = tmp_path / "sample.en.md"
    blocks_path = tmp_path / "sample.en.blocks.json"

    assert output_md.exists()
    assert blocks_path.exists()

    blocks = json.loads(blocks_path.read_text(encoding="utf-8"))
    translations = [{"index": b["index"], "text": f"EN_{b['index']}"} for b in blocks]

    translations_path = tmp_path / "translations.json"
    translations_path.write_text(json.dumps(translations), encoding="utf-8")

    subprocess.check_call(
        ["python3", str(insert), "--input", str(output_md), "--translations", str(translations_path)]
    )

    final_text = output_md.read_text(encoding="utf-8")
    assert "EN_1" in final_text
    assert "EN_2" in final_text
