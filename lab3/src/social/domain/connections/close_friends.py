"""
Список близких друзей.

Module: social.domain.connections.close_friends
"""

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable


class CloseFriends(Readable, Writable):
    """Список близких друзей пользователя.

    Attributes:
        _owner: Владелец.
        _friends: Список близких друзей.
        _max_size: Максимальный размер.
    """

    def __init__(
        self,
        owner: str,
        max_size: int = 100,
    ) -> None:
        """Создать список.

        Args:
            owner: Владелец.
            max_size: Максимум.
        """
        self._owner: str = owner
        self._friends: list[str] = []
        self._max_size: int = max_size

    @classmethod
    def _parse(cls, text: str) -> CloseFriends:
        """Разобрать список из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            owner=parts[0],
            max_size=int(parts[1]),
        )

    @property
    def owner(self) -> str:
        """Владелец.

        Returns:
            Строка.
        """
        return self._owner

    def add(self, username: str) -> bool:
        """Добавить в близкие.

        Args:
            username: Имя.

        Returns:
            ``True``, если добавлен, ``False``, если уже был или лимит.
        """
        if username in self._friends:
            return False
        if len(self._friends) >= self._max_size:
            return False
        self._friends.append(username)
        return True

    def remove(self, username: str) -> None:
        """Убрать из близких.

        Args:
            username: Имя.

        Returns:
            Ничего не возвращает.
        """
        if username in self._friends:
            self._friends.remove(username)

    def contains(self, username: str) -> bool:
        """Проверить наличие.

        Args:
            username: Имя.

        Returns:
            ``True``, если в списке.
        """
        return username in self._friends

    def size(self) -> int:
        """Размер списка.

        Returns:
            Целое число.
        """
        return len(self._friends)

    def is_full(self) -> bool:
        """Проверить заполненность.

        Returns:
            ``True``, если достигнут максимум.
        """
        return len(self._friends) >= self._max_size

    def __eq__(self, other: object) -> bool:
        """Сравнить два списка.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении владельца.
        """
        if not isinstance(other, CloseFriends):
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
        return f"{self._owner}; {self._max_size}"
