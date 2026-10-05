"""
Тесты класса MediaFile.

Module: tests.social.domain.media.test_media_file
"""

from __future__ import annotations

import pytest

from common.exceptions import InvalidPostError
from social.domain.media.media_file import MediaFile


class TestMediaFile:
    """Проверки класса MediaFile."""

    def test_creates(self) -> None:
        """Медиафайл создаётся."""
        m: MediaFile = MediaFile("a.jpg", "https://x", 5.0)
        assert m.filename == "a.jpg"
        assert m.size_mb == 5.0
        assert m.media_type == "photo"
        assert m.owner == ""

    def test_empty_filename_raises(self) -> None:
        """Пустое имя недопустимо."""
        with pytest.raises(InvalidPostError):
            MediaFile("", "https://x", 5.0)

    def test_zero_size_raises(self) -> None:
        """Нулевой размер недопустим."""
        with pytest.raises(InvalidPostError):
            MediaFile("a.jpg", "https://x", 0.0)

    def test_too_large_raises(self) -> None:
        """Превышение лимита недопустимо."""
        with pytest.raises(InvalidPostError):
            MediaFile("a.jpg", "https://x", 100.0)

    def test_is_image(self) -> None:
        """is_image для photo."""
        img: MediaFile = MediaFile("a.jpg", "https://x", 5.0, "photo")
        vid: MediaFile = MediaFile("v.mp4", "https://x", 5.0, "video")
        assert img.is_image()
        assert not vid.is_image()

    def test_is_video(self) -> None:
        """is_video для video."""
        vid: MediaFile = MediaFile("v.mp4", "https://x", 5.0, "video")
        assert vid.is_video()

    def test_is_large(self) -> None:
        """is_large при >10 МБ."""
        big: MediaFile = MediaFile("a", "https://x", 15.0)
        small: MediaFile = MediaFile("a", "https://x", 5.0)
        assert big.is_large()
        assert not small.is_large()

    def test_transfer_to(self) -> None:
        """transfer_to меняет владельца."""
        m: MediaFile = MediaFile("a.jpg", "https://x", 5.0, owner="ivan")
        m.transfer_to("petr")
        assert m.owner == "petr"

    def test_equality(self) -> None:
        """Равные по URL."""
        a: MediaFile = MediaFile("a.jpg", "https://x", 5.0)
        b: MediaFile = MediaFile("b.jpg", "https://x", 3.0)
        assert a == b
        assert a != "not media"

    def test_hash(self) -> None:
        """Хеш по URL."""
        a: MediaFile = MediaFile("a.jpg", "https://x", 5.0)
        b: MediaFile = MediaFile("b.jpg", "https://x", 3.0)
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        m: MediaFile = MediaFile("a.jpg", "https://x", 5.0, owner="ivan")
        text: str = str(m)
        assert "a.jpg" in text
        assert "ivan" in text

    def test_parse(self) -> None:
        """from_string разбирает медиафайл."""
        m: MediaFile = MediaFile.from_string(
            "a.jpg; https://x; 5.0; photo; ivan"
        )
        assert m.filename == "a.jpg"
        assert m.owner == "ivan"
