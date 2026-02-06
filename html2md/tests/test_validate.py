from __future__ import annotations

import pytest

from validate import validate_document


def test_validate_document_accepts_required_structure() -> None:
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
            "Short summary text.",
            "",
            "## Keywords",
            "alpha, beta, gamma, delta, epsilon",
            "",
            "## Content",
            "Body content here.",
            "",
        ]
    )
    validate_document(markdown)


def test_validate_document_rejects_bad_order() -> None:
    markdown = "\n".join(
        [
            "# Sample Title",
            "",
            "## Summary",
            "Short summary text.",
            "",
            "## Sources",
            "- Title: Sample Title",
            "- Source URL: https://example.com",
            "- Publish Date: 2026-02-01",
            "- Generated Date: 2026-02-05",
            "",
            "## Keywords",
            "alpha, beta, gamma, delta, epsilon",
            "",
            "## Content",
            "Body content here.",
            "",
        ]
    )
    with pytest.raises(ValueError):
        validate_document(markdown)


def test_validate_document_rejects_keyword_count() -> None:
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
            "Short summary text.",
            "",
            "## Keywords",
            "alpha, beta, gamma, delta",
            "",
            "## Content",
            "Body content here.",
            "",
        ]
    )
    with pytest.raises(ValueError):
        validate_document(markdown)
