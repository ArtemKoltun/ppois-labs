"""
Журнал действий пользователя.

Module: social.domain.technical.activity_log
"""

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable


class ActivityLog(Readable, Writable):
    """Журнал действий пользователя.

    Attributes:
        _user: Пользователь.
        _entries: Список записей.
        _max_size: Максимум записей.
    """

    def __init__(
        self,
        user: str,
        max_size: int = 1000,
    ) -> None:
        """Создать журнал.

        Args:
            user: Пользователь.
            max_size: Максимум.
        """
        self._user: str = user
        self._entries: list[str] = []
        self._max_size: int = max_size

    @classmethod
    def _parse(cls, text: str) -> ActivityLog:
        """Разобрать журнал из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            user=parts[0],
            max_size=int(parts[1]) if len(parts) > 1 else 1000,
        )

    @property
    def user(self) -> str:
        """Пользователь.

        Returns:
            Строка.
        """
        return self._user

    def record(self, action: str) -> None:
        """Записать действие.

        Args:
            action: Описание.

        Returns:
            Ничего не возвращает.
        """
        if len(self._entries) >= self._max_size:
            self._entries.pop(0)
        self._entries.append(action)

    def entries_count(self) -> int:
        """Число записей.

        Returns:
            Целое число.
        """
        return len(self._entries)

    def last(self) -> str:
        """Последняя запись.

        Returns:
            Строка или пустая.
        """
        if not self._entries:
            return ""
        return self._entries[-1]

    def contains(self, keyword: str) -> bool:
        """Проверить наличие ключевого слова.

        Args:
            keyword: Ключевое слово.

        Returns:
            ``True``, если встречается.
        """
        return any(keyword in entry for entry in self._entries)

    def clear(self) -> None:
        """Очистить журнал.

        Returns:
            Ничего не возвращает.
        """
        self._entries.clear()

    def __eq__(self, other: object) -> bool:
        """Сравнить два журнала.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении пользователя.
        """
        if not isinstance(other, ActivityLog):
            return NotImplemented
        return self._user == other._user

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._user)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return f"{self._user}; {self._max_size}"
