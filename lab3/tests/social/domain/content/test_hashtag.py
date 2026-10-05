"""
Тесты класса Hashtag.

Module: tests.social.domain.content.test_hashtag
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.exceptions import InvalidPostError
from social.domain.content.hashtag import Hashtag

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestHashtag:
    """Проверки класса Hashtag."""

    def test_creates(self) -> None:
        """Хэштег создаётся."""
        h: Hashtag = Hashtag("python")
        assert h.tag == "python"
        assert h.posts_count == 0
        assert not h.is_trending()

    def test_creates_with_hash(self) -> None:
        """Хэштег удаляет #."""
        h: Hashtag = Hashtag("#python")
        assert h.tag == "python"

    def test_empty_raises(self) -> None:
        """Пустой тег недопустим."""
        with pytest.raises(InvalidPostError):
            Hashtag("")

    def test_only_hash_raises(self) -> None:
        """Только # недопустим."""
        with pytest.raises(InvalidPostError):
            Hashtag("#")

    def test_non_alnum_raises(self) -> None:
        """Неалфанумерический тег недопустим."""
        with pytest.raises(InvalidPostError):
            Hashtag("python!")

    def test_add_post(self) -> None:
        """add_post увеличивает счётчик."""
        h: Hashtag = Hashtag("python")
        h.add_post()
        assert h.posts_count == 1

    def test_mark_trending(self) -> None:
        """mark_trending помечает."""
        h: Hashtag = Hashtag("python")
        h.mark_trending()
        assert h.is_trending()

    def test_auto_trending(self) -> None:
        """После 1000 постов становится трендом."""
        h: Hashtag = Hashtag("python")
        for _ in range(1001):
            h.add_post()
        assert h.is_trending()

    def test_full(self) -> None:
        """full возвращает тег с #."""
        h: Hashtag = Hashtag("python")
        assert h.full() == "#python"

    def test_equality(self) -> None:
        """Равные по тегу."""
        a: Hashtag = Hashtag("python")
        b: Hashtag = Hashtag("#python")
        assert a == b
        assert a != "not hashtag"

    def test_hash(self) -> None:
        """Хеш по тегу."""
        a: Hashtag = Hashtag("python")
        b: Hashtag = Hashtag("#python")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает тег."""
        h: Hashtag = Hashtag("python")
        assert str(h) == "python"

    def test_parse(self) -> None:
        """from_string разбирает хэштег."""
        h: Hashtag = Hashtag.from_string("#python")
        assert h.tag == "python"
