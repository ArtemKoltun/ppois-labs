"""
Тесты класса Chat.

Module: tests.social.domain.messages.test_chat
"""

from __future__ import annotations

import pytest

from common.exceptions import MessageDeliveryError
from social.domain.messages.chat import Chat


class TestChat:
    """Проверки класса Chat."""

    def test_creates(self) -> None:
        """Чат создаётся."""
        c: Chat = Chat("ivan", "petr")
        assert c.first_user == "ivan"
        assert c.second_user == "petr"
        assert c.messages_count == 0
        assert not c.is_muted

    def test_same_users_raises(self) -> None:
        """Одинаковые пользователи недопустимы."""
        with pytest.raises(MessageDeliveryError):
            Chat("ivan", "ivan")

    def test_send(self) -> None:
        """send увеличивает счётчик."""
        c: Chat = Chat("ivan", "petr")
        c.send()
        assert c.messages_count == 1

    def test_mute_unmute(self) -> None:
        """Отключение и включение уведомлений."""
        c: Chat = Chat("ivan", "petr")
        c.mute()
        assert c.is_muted
        c.unmute()
        assert not c.is_muted

    def test_archive_unarchive(self) -> None:
        """Архивация и разархивация."""
        c: Chat = Chat("ivan", "petr")
        c.archive()
        assert c.is_archived()
        c.unarchive()
        assert not c.is_archived()

    def test_has_participant(self) -> None:
        """has_participant проверяет участника."""
        c: Chat = Chat("ivan", "petr")
        assert c.has_participant("ivan")
        assert c.has_participant("petr")
        assert not c.has_participant("other")

    def test_is_active(self) -> None:
        """is_active только при наличии сообщений."""
        c: Chat = Chat("ivan", "petr")
        assert not c.is_active()
        c.send()
        assert c.is_active()
        c.archive()
        assert not c.is_active()

    def test_equality_symmetric(self) -> None:
        """Чат симметричен по участникам."""
        a: Chat = Chat("ivan", "petr")
        b: Chat = Chat("petr", "ivan")
        assert a == b
        assert a != "not chat"

    def test_hash_symmetric(self) -> None:
        """Хеш одинаков для симметричных чатов."""
        a: Chat = Chat("ivan", "petr")
        b: Chat = Chat("petr", "ivan")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает участников."""
        c: Chat = Chat("ivan", "petr")
        text: str = str(c)
        assert "ivan" in text
        assert "petr" in text

    def test_parse(self) -> None:
        """from_string разбирает чат."""
        c: Chat = Chat.from_string("ivan; petr")
        assert c.first_user == "ivan"
