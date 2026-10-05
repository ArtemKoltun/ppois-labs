"""
Блокировка пользователя.

Module: social.domain.moderation.ban
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

class Ban(Readable, Writable):
    """Блокировка пользователя.

    Attributes:
        _username: Заблокированный.
        _moderator: Кто заблокировал.
        _reason: Причина.
        _is_permanent: Навсегда ли.
    """

    def __init__(
        self,
        username: str,
        moderator: str,
        reason: str,
        is_permanent: bool = False,
    ) -> None:
        """Создать блокировку.

        Args:
            username: Заблокированный.
            moderator: Модератор.
            reason: Причина.
            is_permanent: Навсегда.
        """
        self._username: str = username
        self._moderator: str = moderator
        self._reason: str = reason
        self._is_permanent: bool = is_permanent

    @classmethod
    def _parse(cls, text: str) -> Ban:
        """Разобрать блокировку из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            username=parts[0],
            moderator=parts[1],
            reason=parts[2],
            is_permanent=(
                parts[3].lower() == "true"
                if len(parts) > 3
                else False
            ),
        )

    @property
    def username(self) -> str:
        """Заблокированный.

        Returns:
            Строка.
        """
        return self._username

    @property
    def moderator(self) -> str:
        """Модератор.

        Returns:
            Строка.
        """
        return self._moderator

    @property
    def reason(self) -> str:
        """Причина.

        Returns:
            Строка.
        """
        return self._reason

    @property
    def is_permanent(self) -> bool:
        """Постоянная ли.

        Returns:
            ``True``, если навсегда.
        """
        return self._is_permanent

    def change_reason(self, reason: str) -> None:
        """Сменить причину.

        Args:
            reason: Новая причина.

        Returns:
            Ничего не возвращает.
        """
        self._reason = reason

    def make_permanent(self) -> None:
        """Сделать постоянной.

        Returns:
            Ничего не возвращает.
        """
        self._is_permanent = True

    def is_appealable(self) -> bool:
        """Можно ли обжаловать.

        Returns:
            ``True``, если не постоянная.
        """
        return not self._is_permanent

    def __eq__(self, other: object) -> bool:
        """Сравнить две блокировки.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении имени пользователя.
        """
        if not isinstance(other, Ban):
            return NotImplemented
        return self._username == other._username

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._username)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._username}; {self._moderator}; "
            f"{self._reason}; {self._is_permanent}"
        )
