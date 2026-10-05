"""
Реакция на сообщение.

Module: social.domain.messages.message_reaction
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class MessageReaction(Readable, Writable):
    """Реакция пользователя на сообщение.

    Attributes:
        _user: Пользователь.
        _message_id: Идентификатор сообщения.
        _emoji: Эмодзи-реакция.
    """

    def __init__(
        self,
        user: str,
        message_id: str,
        emoji: str = "👍",
    ) -> None:
        """Создать реакцию.

        Args:
            user: Пользователь.
            message_id: Сообщение.
            emoji: Эмодзи.
        """
        self._user: str = user
        self._message_id: str = message_id
        self._emoji: str = emoji

    @classmethod
    def _parse(cls, text: str) -> MessageReaction:
        """Разобрать реакцию из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            user=parts[0],
            message_id=parts[1],
            emoji=parts[2] if len(parts) > 2 else "👍",
        )

    @property
    def user(self) -> str:
        """Пользователь.

        Returns:
            Строка.
        """
        return self._user

    @property
    def emoji(self) -> str:
        """Эмодзи.

        Returns:
            Строка.
        """
        return self._emoji

    def change_emoji(self, emoji: str) -> None:
        """Сменить эмодзи.

        Args:
            emoji: Новое эмодзи.

        Returns:
            Ничего не возвращает.
        """
        self._emoji = emoji

    def is_positive(self) -> bool:
        """Проверить положительная ли реакция.

        Returns:
            ``True``, если эмодзи в положительных.
        """
        positive: set[str] = {"👍", "❤️", "😂", "🔥", "🎉"}
        return self._emoji in positive

    def __eq__(self, other: object) -> bool:
        """Сравнить две реакции.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении пользователя и сообщения.
        """
        if not isinstance(other, MessageReaction):
            return NotImplemented
        return (
            self._user == other._user
            and self._message_id == other._message_id
        )

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash((self._user, self._message_id))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return f"{self._user}; {self._message_id}; {self._emoji}"
