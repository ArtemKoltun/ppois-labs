"""
Модератор.

Module: social.domain.moderation.moderator
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

class Moderator(Readable, Writable):
    """Модератор социальной сети.

    Attributes:
        _username: Имя.
        _level: Уровень от 1 до 5.
        _processed_reports: Обработано жалоб.
        _is_active: Активен ли.
    """

    def __init__(
        self,
        username: str,
        level: int = 1,
    ) -> None:
        """Создать модератора.

        Args:
            username: Имя.
            level: Уровень.

        Raises:
            ValueError: Если уровень вне диапазона.
        """
        if not 1 <= level <= 5:
            raise ValueError("уровень должен быть от 1 до 5")
        self._username: str = username
        self._level: int = level
        self._processed_reports: int = 0
        self._is_active: bool = True

    @classmethod
    def _parse(cls, text: str) -> Moderator:
        """Разобрать модератора из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            username=parts[0],
            level=int(parts[1]) if len(parts) > 1 else 1,
        )

    @property
    def username(self) -> str:
        """Имя.

        Returns:
            Строка.
        """
        return self._username

    @property
    def level(self) -> int:
        """Уровень.

        Returns:
            Целое число.
        """
        return self._level

    @property
    def processed_reports(self) -> int:
        """Обработано жалоб.

        Returns:
            Целое число.
        """
        return self._processed_reports

    def process_report(self) -> None:
        """Обработать жалобу.

        Returns:
            Ничего не возвращает.
        """
        self._processed_reports += 1

    def promote(self) -> None:
        """Повысить уровень.

        Returns:
            Ничего не возвращает.
        """
        self._level = min(5, self._level + 1)

    def demote(self) -> None:
        """Понизить уровень.

        Returns:
            Ничего не возвращает.
        """
        self._level = max(1, self._level - 1)

    def deactivate(self) -> None:
        """Деактивировать.

        Returns:
            Ничего не возвращает.
        """
        self._is_active = False

    def can_ban(self) -> bool:
        """Проверить право банить.

        Returns:
            ``True``, если уровень >= 3.
        """
        return self._level >= 3

    def __eq__(self, other: object) -> bool:
        """Сравнить двух модераторов.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении имени.
        """
        if not isinstance(other, Moderator):
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
        return f"{self._username}; {self._level}"
