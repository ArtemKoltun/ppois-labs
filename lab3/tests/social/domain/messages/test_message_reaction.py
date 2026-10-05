"""
Тесты класса MessageReaction.

Module: tests.social.domain.messages.test_message_reaction
"""

from __future__ import annotations

from social.domain.messages.message_reaction import MessageReaction


class TestMessageReaction:
    """Проверки класса MessageReaction."""

    def test_creates_default(self) -> None:
        """Реакция создаётся с дефолтным эмодзи."""
        r: MessageReaction = MessageReaction("ivan", "msg1")
        assert r.user == "ivan"
        assert r.emoji == "👍"

    def test_change_emoji(self) -> None:
        """change_emoji меняет эмодзи."""
        r: MessageReaction = MessageReaction("ivan", "msg1")
        r.change_emoji("❤️")
        assert r.emoji == "❤️"

    def test_is_positive(self) -> None:
        """is_positive для позитивных эмодзи."""
        pos: MessageReaction = MessageReaction("ivan", "m", "👍")
        neg: MessageReaction = MessageReaction("ivan", "m", "👎")
        assert pos.is_positive()
        assert not neg.is_positive()

    def test_equality(self) -> None:
        """Равные по пользователю и сообщению."""
        a: MessageReaction = MessageReaction("ivan", "m1")
        b: MessageReaction = MessageReaction("ivan", "m1", "❤️")
        assert a == b
        assert a != "not reaction"

    def test_hash(self) -> None:
        """Хеш реакции."""
        a: MessageReaction = MessageReaction("ivan", "m1")
        b: MessageReaction = MessageReaction("ivan", "m1", "❤️")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        r: MessageReaction = MessageReaction("ivan", "m1")
        assert "ivan" in str(r)

    def test_parse(self) -> None:
        """from_string разбирает реакцию."""
        r: MessageReaction = MessageReaction.from_string("ivan; m1; ❤️")
        assert r.emoji == "❤️"
