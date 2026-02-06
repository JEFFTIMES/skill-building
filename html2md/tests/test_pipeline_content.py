from __future__ import annotations

from models import MediaItem
from pipeline import _build_content_markdown


def test_build_content_markdown_adds_media_and_links() -> None:
    blocks = ["Main content paragraph."]
    images = [
        MediaItem(type="image", url="https://example.com/a.jpg", local_path="media/a.jpg")
    ]
    videos = [
        MediaItem(
            type="video",
            url="https://example.com/v.mp4",
            snapshot_path="media/v.jpg",
        )
    ]
    links = ["https://example.com", "javascript:void(0);", "https://example.com/about"]

    content = _build_content_markdown(blocks, images, videos, links)

    assert "### Media" in content
    assert "![image](media/a.jpg)" in content
    assert "![video snapshot 1](media/v.jpg)" in content
    assert "### Links" in content
    assert "- https://example.com" in content
    assert "javascript:void(0);" not in content
