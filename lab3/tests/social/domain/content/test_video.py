"""
Тесты класса Video.

Module: tests.social.domain.content.test_video
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.exceptions import InvalidPostError
from social.domain.content.video import Video

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestVideo:
    """Проверки класса Video."""

    def test_creates(self) -> None:
        """Видео создаётся."""
        v: Video = Video("https://x.mp4", 120)
        assert v.url == "https://x.mp4"
        assert v.duration_seconds == 120

    def test_empty_url_raises(self) -> None:
        """Пустой URL недопустим."""
        with pytest.raises(InvalidPostError):
            Video("", 100)

    def test_zero_duration_raises(self) -> None:
        """Нулевая длительность недопустима."""
        with pytest.raises(InvalidPostError):
            Video("https://x.mp4", 0)

    def test_watch(self) -> None:
        """watch увеличивает просмотры."""
        v: Video = Video("https://x.mp4", 60)
        v.watch()
        v.watch()
        assert v.views_count == 2

    def test_duration_minutes(self) -> None:
        """duration_minutes считает."""
        v: Video = Video("https://x.mp4", 120)
        assert v.duration_minutes() == 2.0

    def test_is_short(self) -> None:
        """is_short для видео до 60 секунд."""
        short: Video = Video("https://s.mp4", 30)
        long_: Video = Video("https://l.mp4", 120)
        assert short.is_short()
        assert not long_.is_short()

    def test_equality(self) -> None:
        """Равные по URL."""
        a: Video = Video("https://x.mp4", 60)
        b: Video = Video("https://x.mp4", 120)
        assert a == b
        assert a != "not video"

    def test_hash(self) -> None:
        """Хеш по URL."""
        a: Video = Video("https://x.mp4", 60)
        b: Video = Video("https://x.mp4", 120)
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        v: Video = Video("https://x.mp4", 60, "Заголовок")
        text: str = str(v)
        assert "https://x.mp4" in text
        assert "Заголовок" in text

    def test_parse(self) -> None:
        """from_string разбирает видео."""
        v: Video = Video.from_string("https://x.mp4; 60; Заголовок")
        assert v.url == "https://x.mp4"
        assert v.duration_seconds == 60
