"""
Тесты класса Comment.

Module: tests.social.domain.content.test_comment
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.exceptions import InvalidPostError
from social.domain.content.comment import Comment

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestComment:
    """Проверки класса Comment."""

    def test_creates(self) -> None:
        """Комментарий создаётся."""
        c: Comment = Comment("ivan", "post1", "Класс!")
        assert c.author == "ivan"
        assert c.post_id == "post1"
        assert c.text == "Класс!"

    def test_empty_author_raises(self) -> None:
        """Пустой автор недопустим."""
        with pytest.raises(InvalidPostError):
            Comment("", "post1", "x")

    def test_empty_post_id_raises(self) -> None:
        """Пустой id поста недопустим."""
        with pytest.raises(InvalidPostError):
            Comment("ivan", "", "x")

    def test_empty_text_raises(self) -> None:
        """Пустой текст недопустим."""
        with pytest.raises(InvalidPostError):
            Comment("ivan", "post1", "")

    def test_like_unlike(self) -> None:
        """Лайки и антилайки."""
        c: Comment = Comment("ivan", "p", "x")
        c.like()
        c.like()
        assert c._likes_count == 2
        c.unlike()
        assert c._likes_count == 1

    def test_length(self) -> None:
        """length считает символы."""
        c: Comment = Comment("ivan", "p", "Привет")
        assert c.length() == 6

    def test_equality(self) -> None:
        """Равные по автору и тексту."""
        a: Comment = Comment("ivan", "p1", "x")
        b: Comment = Comment("ivan", "p2", "x")
        assert a == b
        assert a != "not comment"

    def test_hash(self) -> None:
        """Хеш комментария."""
        a: Comment = Comment("ivan", "p1", "x")
        b: Comment = Comment("ivan", "p2", "x")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        c: Comment = Comment("ivan", "post1", "Привет")
        text: str = str(c)
        assert "ivan" in text
        assert "Привет" in text

    def test_parse(self) -> None:
        """from_string разбирает комментарий."""
        c: Comment = Comment.from_string("ivan; post1; Привет")
        assert c.author == "ivan"
        assert c.text == "Привет"
