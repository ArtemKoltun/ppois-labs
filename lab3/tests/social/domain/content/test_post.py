"""
Тесты класса Post.

Module: tests.social.domain.content.test_post
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.enums.post_visibility import PostVisibility
from common.exceptions import InvalidPostError
from social.domain.content.post import Post

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestPost:
    """Проверки класса Post."""

    def test_creates(self) -> None:
        """Пост создаётся."""
        p: Post = Post(author="ivan", text="Привет")
        assert p.author == "ivan"
        assert p.text == "Привет"
        assert p.visibility is PostVisibility.PUBLIC
        assert p.likes_count == 0

    def test_empty_author_raises(self) -> None:
        """Пустой автор недопустим."""
        with pytest.raises(InvalidPostError):
            Post(author="", text="x")

    def test_empty_text_raises(self) -> None:
        """Пустой текст недопустим."""
        with pytest.raises(InvalidPostError):
            Post(author="ivan", text="")

    def test_too_long_text_raises(self) -> None:
        """Слишком длинный текст недопустим."""
        with pytest.raises(InvalidPostError):
            Post(author="ivan", text="a" * 6000)

    def test_like_unlike(self) -> None:
        """Лайки и антилайки."""
        p: Post = Post(author="ivan", text="x")
        p.like()
        p.like()
        assert p.likes_count == 2
        p.unlike()
        assert p.likes_count == 1
        p.unlike()
        p.unlike()
        assert p.likes_count == 0

    def test_add_comment(self) -> None:
        """add_comment увеличивает счётчик."""
        p: Post = Post(author="ivan", text="x")
        p.add_comment()
        assert p.comments_count == 1

    def test_edit(self) -> None:
        """edit меняет текст."""
        p: Post = Post(author="ivan", text="Старый")
        p.edit("Новый")
        assert p.text == "Новый"
        assert p.is_edited()

    def test_edit_empty_raises(self) -> None:
        """Пустой новый текст недопустим."""
        p: Post = Post(author="ivan", text="x")
        with pytest.raises(InvalidPostError):
            p.edit("")

    def test_change_visibility(self) -> None:
        """change_visibility меняет видимость."""
        p: Post = Post(author="ivan", text="x")
        p.change_visibility(PostVisibility.PRIVATE)
        assert p.visibility is PostVisibility.PRIVATE

    def test_is_popular(self) -> None:
        """is_popular проверяет лайки."""
        p: Post = Post(author="ivan", text="x")
        for _ in range(101):
            p.like()
        assert p.is_popular()

    def test_equality(self) -> None:
        """Равные по автору и тексту."""
        a: Post = Post(author="ivan", text="x")
        b: Post = Post(author="ivan", text="x")
        assert a == b
        assert a != "not post"

    def test_hash(self) -> None:
        """Хеш поста."""
        a: Post = Post(author="ivan", text="x")
        b: Post = Post(author="ivan", text="x")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        p: Post = Post(author="ivan", text="Привет")
        text: str = str(p)
        assert "ivan" in text
        assert "Привет" in text

    def test_parse(self) -> None:
        """from_string разбирает пост."""
        p: Post = Post.from_string("ivan; Привет; public")
        assert p.author == "ivan"
        assert p.visibility is PostVisibility.PUBLIC
