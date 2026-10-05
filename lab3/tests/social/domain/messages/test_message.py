"""
Тесты класса Message.

Module: tests.social.domain.messages.test_message
"""

from __future__ import annotations

import pytest

from common.exceptions import MessageDeliveryError
from social.domain.messages.message import Message


class TestMessage:
    """Проверки класса Message."""

    def test_creates(self) -> None:
        """Сообщение создаётся."""
        m: Message = Message("ivan", "chat1", "Привет")
        assert m.sender == "ivan"
        assert m.chat_id == "chat1"
        assert m.text == "Привет"
        assert not m.is_read

    def test_empty_sender_raises(self) -> None:
        """Пустой отправитель недопустим."""
        with pytest.raises(MessageDeliveryError):
            Message("", "chat1", "x")

    def test_empty_text_raises(self) -> None:
        """Пустой текст недопустим."""
        with pytest.raises(MessageDeliveryError):
            Message("ivan", "chat1", "")

    def test_too_long_text_raises(self) -> None:
        """Слишком длинный текст недопустим."""
        with pytest.raises(MessageDeliveryError):
            Message("ivan", "chat1", "a" * 5000)

    def test_mark_read(self) -> None:
        """mark_read отмечает."""
        m: Message = Message("ivan", "chat1", "x")
        m.mark_read()
        assert m.is_read

    def test_delete_restore(self) -> None:
        """Удаление и восстановление."""
        m: Message = Message("ivan", "chat1", "x")
        m.delete()
        assert m.is_deleted()
        m.restore()
        assert not m.is_deleted()

    def test_edit(self) -> None:
        """edit меняет текст."""
        m: Message = Message("ivan", "chat1", "Старый")
        m.edit("Новый")
        assert m.text == "Новый"

    def test_edit_empty_raises(self) -> None:
        """Пустой новый текст недопустим."""
        m: Message = Message("ivan", "chat1", "x")
        with pytest.raises(MessageDeliveryError):
            m.edit("")

    def test_length(self) -> None:
        """length считает символы."""
        m: Message = Message("ivan", "chat1", "Привет")
        assert m.length() == 6

    def test_equality(self) -> None:
        """Равные по sender, chat_id, text."""
        a: Message = Message("ivan", "chat1", "x")
        b: Message = Message("ivan", "chat1", "x")
        assert a == b
        assert a != "not message"

    def test_hash(self) -> None:
        """Хеш сообщения."""
        a: Message = Message("ivan", "chat1", "x")
        b: Message = Message("ivan", "chat1", "x")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        m: Message = Message("ivan", "chat1", "Привет")
        assert "Привет" in str(m)

    def test_parse(self) -> None:
        """from_string разбирает сообщение."""
        m: Message = Message.from_string("ivan; chat1; Привет")
        assert m.sender == "ivan"
        assert m.text == "Привет"
