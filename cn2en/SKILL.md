---
name: cn2en
description: Translate Chinese Markdown (.md) files into English while preserving Markdown structure. Use when asked to translate Chinese Markdown to English, create a sibling .en.md file, keep YAML front matter untouched, and maintain a term glossary/translation memory.
---

# cn2en

## Workflow

1) Confirm input .md file path and desired output name (default: `foo.md` -> `foo.en.md`).
2) Parse Markdown into blocks; translate only text nodes.
   - Preserve code blocks, inline code, links, and images.
   - Keep YAML front matter unchanged.
3) Apply glossary replacements before/after translation to enforce term consistency.
4) Write the sibling output file in the same directory.
5) Append new terms to `references/glossary.jsonl` when confident.

## Resources

- `references/output-conventions.md`: naming rules and file placement.
- `references/ignore-rules.md`: what to preserve and never translate.
- `references/glossary.jsonl`: append-only term base.

## Term Base Format

Each line in `references/glossary.jsonl` is a JSON object:

- `zh`: Chinese term
- `en`: English term
- `source`: where the term came from (file path or context)
- `context`: short snippet to clarify meaning
- `added_at`: ISO 8601 timestamp

Append only when the translation is stable and unambiguous.
