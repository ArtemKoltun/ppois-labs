"""
Тесты класса Mention.

Module: tests.social.domain.media.test_mention
"""

from __future__ import annotations

from social.domain.media.mention import Mention


class TestMention:
    """Проверки класса Mention."""

    def test_creates(self) -> None:
        """Упоминание создаётся."""
        m: Mention = Mention("post1", "petr")
        assert m.content_id == "post1"
        assert m.mentioned_user == "petr"
        assert not m.is_read

    def test_mark_read(self) -> None:
        """mark_read отмечает."""
        m: Mention = Mention("p", "petr")
        m.mark_read()
        assert m.is_read

    def test_equality(self) -> None:
        """Равные по контенту и пользователю."""
        a: Mention = Mention("p1", "petr")
        b: Mention = Mention("p1", "petr")
        assert a == b
        assert a != "not mention"

    def test_hash(self) -> None:
        """Хеш упоминания."""
        a: Mention = Mention("p1", "petr")
        b: Mention = Mention("p1", "petr")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        m: Mention = Mention("p1", "petr")
        text: str = str(m)
        assert "p1" in text
        assert "petr" in text

    def test_parse(self) -> None:
        """from_string разбирает упоминание."""
        m: Mention = Mention.from_string("p1; petr")
        assert m.content_id == "p1"
        assert m.mentioned_user == "petr"
