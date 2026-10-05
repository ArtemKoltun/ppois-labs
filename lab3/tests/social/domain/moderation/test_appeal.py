"""
Тесты класса Appeal.

Module: tests.social.domain.moderation.test_appeal
"""

from __future__ import annotations

from social.domain.moderation.appeal import Appeal


class TestAppeal:
    """Проверки класса Appeal."""

    def test_creates(self) -> None:
        """Апелляция создаётся."""
        a: Appeal = Appeal("ivan", "ivan", "прошу разблокировать")
        assert a.username == "ivan"
        assert a.text == "прошу разблокировать"
        assert not a.is_reviewed

    def test_review(self) -> None:
        """review отмечает рассмотрение."""
        a: Appeal = Appeal("ivan", "ivan", "x")
        a.review()
        assert a.is_reviewed

    def test_update_text(self) -> None:
        """update_text меняет текст."""
        a: Appeal = Appeal("ivan", "ivan", "x")
        a.update_text("y")
        assert a.text == "y"

    def test_is_long(self) -> None:
        """is_long при тексте >1000."""
        short: Appeal = Appeal("ivan", "ivan", "x")
        long_: Appeal = Appeal("ivan", "ivan", "y" * 1001)
        assert not short.is_long()
        assert long_.is_long()

    def test_equality(self) -> None:
        """Равные по автору и цели."""
        a: Appeal = Appeal("ivan", "ivan", "x")
        b: Appeal = Appeal("ivan", "ivan", "y")
        assert a == b
        assert a != "not appeal"

    def test_hash(self) -> None:
        """Хеш апелляции."""
        a: Appeal = Appeal("ivan", "ivan", "x")
        b: Appeal = Appeal("ivan", "ivan", "y")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        a: Appeal = Appeal("ivan", "ivan", "x")
        assert "ivan" in str(a)

    def test_parse(self) -> None:
        """from_string разбирает апелляцию."""
        a: Appeal = Appeal.from_string("ivan; ivan; текст")
        assert a.username == "ivan"
        assert a.text == "текст"
