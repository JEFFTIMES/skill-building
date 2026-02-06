from __future__ import annotations

from models import ContentBlock
from topic_filter import filter_by_topic


def test_filter_by_topic_matches_keywords() -> None:
    blocks = [
        ContentBlock(text="This is about climate policy."),
        ContentBlock(text="Sports update and scores."),
    ]

    filtered = filter_by_topic(blocks, "climate policy")
    assert len(filtered) == 1
    assert "climate" in filtered[0].text.lower()


def test_filter_by_topic_falls_back_when_empty() -> None:
    blocks = [
        ContentBlock(text="This is about finance."),
        ContentBlock(text="Sports update and scores."),
    ]

    filtered = filter_by_topic(blocks, "biology")
    assert filtered == blocks
