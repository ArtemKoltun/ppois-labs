"""
Сообщение.

Module: social.domain.messages.message
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.constants import MAX_MESSAGE_LENGTH
from common.exceptions.connection_exceptions import MessageDeliveryError

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Message(Readable, Writable):
    """Сообщение в чате.

    Attributes:
        _sender: Отправитель.
        _chat_id: Идентификатор чата.
        _text: Текст.
        _is_read: Прочитано ли.
        _is_deleted: Удалено ли.
    """

    def __init__(
        self,
        sender: str,
        chat_id: str,
        text: str,
    ) -> None:
        """Создать сообщение.

        Args:
            sender: Отправитель.
            chat_id: Чат.
            text: Текст.

        Raises:
            MessageDeliveryError: Если данные некорректны.
        """
        if not sender or not chat_id:
            raise MessageDeliveryError(
                "отправитель и чат не могут быть пустыми"
            )
        if not text:
            raise MessageDeliveryError("текст не может быть пустым")
        if len(text) > MAX_MESSAGE_LENGTH:
            raise MessageDeliveryError(
                f"сообщение не должно превышать "
                f"{MAX_MESSAGE_LENGTH} символов"
            )
        self._sender: str = sender
        self._chat_id: str = chat_id
        self._text: str = text
        self._is_read: bool = False
        self._is_deleted: bool = False

    @classmethod
    def _parse(cls, text: str) -> Message:
        """Разобрать сообщение из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            sender=parts[0],
            chat_id=parts[1],
            text=parts[2],
        )

    @property
    def sender(self) -> str:
        """Отправитель.

        Returns:
            Строка.
        """
        return self._sender

    @property
    def chat_id(self) -> str:
        """Чат.

        Returns:
            Строка.
        """
        return self._chat_id

    @property
    def text(self) -> str:
        """Текст.

        Returns:
            Строка.
        """
        return self._text

    @property
    def is_read(self) -> bool:
        """Прочитано ли.

        Returns:
            ``True``, если прочитано.
        """
        return self._is_read

    def mark_read(self) -> None:
        """Отметить как прочитанное.

        Returns:
            Ничего не возвращает.
        """
        self._is_read = True

    def delete(self) -> None:
        """Удалить сообщение.

        Returns:
            Ничего не возвращает.
        """
        self._is_deleted = True

    def restore(self) -> None:
        """Восстановить сообщение.

        Returns:
            Ничего не возвращает.
        """
        self._is_deleted = False

    def is_deleted(self) -> bool:
        """Проверить удаление.

        Returns:
            ``True``, если удалено.
        """
        return self._is_deleted

    def edit(self, new_text: str) -> None:
        """Отредактировать текст.

        Args:
            new_text: Новый текст.

        Returns:
            Ничего не возвращает.

        Raises:
            MessageDeliveryError: Если текст некорректен.
        """
        if not new_text:
            raise MessageDeliveryError("текст не может быть пустым")
        if len(new_text) > MAX_MESSAGE_LENGTH:
            raise MessageDeliveryError(
                f"сообщение не должно превышать "
                f"{MAX_MESSAGE_LENGTH} символов"
            )
        self._text = new_text

    def length(self) -> int:
        """Длина текста.

        Returns:
            Число символов.
        """
        return len(self._text)

    def __eq__(self, other: object) -> bool:
        """Сравнить два сообщения.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении отправителя, чата и текста.
        """
        if not isinstance(other, Message):
            return NotImplemented
        return (
            self._sender == other._sender
            and self._chat_id == other._chat_id
            and self._text == other._text
        )

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash((self._sender, self._chat_id, self._text))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return f"{self._sender}; {self._chat_id}; {self._text}"
