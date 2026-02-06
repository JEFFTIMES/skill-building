from __future__ import annotations

from update_summary_and_keywords import update_markdown


def test_update_markdown_replaces_summary_and_keywords() -> None:
    markdown = "\n".join(
        [
            "# Sample Title",
            "",
            "## Sources",
            "- Title: Sample Title",
            "- Source URL: https://example.com",
            "- Publish Date: 2026-02-01",
            "- Generated Date: 2026-02-05",
            "",
            "## Summary",
            "Old summary.",
            "",
            "## Keywords",
            "old, keywords",
            "",
            "## Content",
            "Body content here.",
            "",
        ]
    )

    updated = update_markdown(
        markdown,
        "New summary text.",
        ["alpha", "beta", "gamma", "delta", "epsilon"],
    )

    assert "## Summary\nNew summary text." in updated
    assert "## Keywords\nalpha, beta, gamma, delta, epsilon" in updated
