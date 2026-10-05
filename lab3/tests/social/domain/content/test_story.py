"""
Тесты класса Story.

Module: tests.social.domain.content.test_story
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.exceptions import InvalidPostError
from social.domain.content.story import Story

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestStory:
    """Проверки класса Story."""

    def test_creates(self) -> None:
        """История создаётся."""
        s: Story = Story("ivan", "https://x.jpg")
        assert s.author == "ivan"
        assert s.media_url == "https://x.jpg"
        assert s.views_count == 0

    def test_empty_author_raises(self) -> None:
        """Пустой автор недопустим."""
        with pytest.raises(InvalidPostError):
            Story("", "https://x.jpg")

    def test_empty_media_raises(self) -> None:
        """Пустое медиа недопустимо."""
        with pytest.raises(InvalidPostError):
            Story("ivan", "")

    def test_zero_hours_raises(self) -> None:
        """Нулевое время жизни недопустимо."""
        with pytest.raises(InvalidPostError):
            Story("ivan", "https://x.jpg", hours_to_live=0)

    def test_view(self) -> None:
        """view увеличивает просмотры."""
        s: Story = Story("ivan", "https://x.jpg")
        s.view()
        assert s.views_count == 1

    def test_is_expired(self) -> None:
        """is_expired проверяет срок."""
        s: Story = Story("ivan", "https://x.jpg", hours_to_live=24)
        assert not s.is_expired(23)
        assert s.is_expired(24)
        assert s.is_expired(48)

    def test_equality(self) -> None:
        """Равные по автору и медиа."""
        a: Story = Story("ivan", "https://x.jpg")
        b: Story = Story("ivan", "https://x.jpg")
        assert a == b
        assert a != "not story"

    def test_hash(self) -> None:
        """Хеш по автору и медиа."""
        a: Story = Story("ivan", "https://x.jpg")
        b: Story = Story("ivan", "https://x.jpg")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        s: Story = Story("ivan", "https://x.jpg", hours_to_live=12)
        text: str = str(s)
        assert "ivan" in text
        assert "12" in text

    def test_parse(self) -> None:
        """from_string разбирает историю."""
        s: Story = Story.from_string("ivan; https://x.jpg; 12")
        assert s.author == "ivan"
        assert s._hours_to_live == 12
