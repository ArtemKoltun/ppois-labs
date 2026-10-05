"""
Предупреждение пользователю.

Module: social.domain.moderation.warning
"""

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable


class Warning(Readable, Writable):
    """Предупреждение от модератора.

    Attributes:
        _username: Кому выдано.
        _moderator: Кем выдано.
        _reason: Причина.
        _is_acknowledged: Принято ли.
    """

    def __init__(
        self,
        username: str,
        moderator: str,
        reason: str,
    ) -> None:
        """Создать предупреждение.

        Args:
            username: Пользователь.
            moderator: Модератор.
            reason: Причина.
        """
        self._username: str = username
        self._moderator: str = moderator
        self._reason: str = reason
        self._is_acknowledged: bool = False

    @classmethod
    def _parse(cls, text: str) -> Warning:
        """Разобрать предупреждение из строки.

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
        )

    @property
    def username(self) -> str:
        """Пользователь.

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
    def is_acknowledged(self) -> bool:
        """Принято ли пользователем.

        Returns:
            ``True``, если принято.
        """
        return self._is_acknowledged

    def acknowledge(self) -> None:
        """Принять предупреждение.

        Returns:
            Ничего не возвращает.
        """
        self._is_acknowledged = True

    def is_serious(self) -> bool:
        """Проверить серьёзность.

        Returns:
            ``True``, если в причине есть слово «нарушение».
        """
        return "нарушени" in self._reason.lower()

    def __eq__(self, other: object) -> bool:
        """Сравнить два предупреждения.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении пользователя и причины.
        """
        if not isinstance(other, Warning):
            return NotImplemented
        return (
            self._username == other._username
            and self._reason == other._reason
        )

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash((self._username, self._reason))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return f"{self._username}; {self._moderator}; {self._reason}"
