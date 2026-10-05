"""
Чёрный список пользователя.

Module: social.domain.connections.block_list
"""

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable


class BlockList(Readable, Writable):
    """Чёрный список пользователя.

    Attributes:
        _owner: Владелец списка.
        _blocked: Список заблокированных.
        _reason: Причина блокировки.
    """

    def __init__(
        self,
        owner: str,
        reason: str = "",
    ) -> None:
        """Создать чёрный список.

        Args:
            owner: Владелец.
            reason: Причина.
        """
        self._owner: str = owner
        self._blocked: list[str] = []
        self._reason: str = reason

    @classmethod
    def _parse(cls, text: str) -> BlockList:
        """Разобрать чёрный список из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(owner=parts[0], reason=parts[1])

    @property
    def owner(self) -> str:
        """Владелец.

        Returns:
            Строка.
        """
        return self._owner

    def add(self, username: str) -> None:
        """Добавить в чёрный список.

        Args:
            username: Имя пользователя.

        Returns:
            Ничего не возвращает.
        """
        if username not in self._blocked:
            self._blocked.append(username)

    def remove(self, username: str) -> None:
        """Убрать из чёрного списка.

        Args:
            username: Имя пользователя.

        Returns:
            Ничего не возвращает.
        """
        if username in self._blocked:
            self._blocked.remove(username)

    def contains(self, username: str) -> bool:
        """Проверить наличие.

        Args:
            username: Имя пользователя.

        Returns:
            ``True``, если в списке.
        """
        return username in self._blocked

    def blocked_count(self) -> int:
        """Число заблокированных.

        Returns:
            Целое число.
        """
        return len(self._blocked)

    def clear(self) -> None:
        """Очистить список.

        Returns:
            Ничего не возвращает.
        """
        self._blocked.clear()

    def __eq__(self, other: object) -> bool:
        """Сравнить два списка.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении владельца.
        """
        if not isinstance(other, BlockList):
            return NotImplemented
        return self._owner == other._owner

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._owner)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return f"{self._owner}; {self._reason}"
