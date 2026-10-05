"""
Дружба между пользователями.

Module: social.domain.connections.friendship
"""

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.exceptions.connection_exceptions import FriendshipError


class Friendship(Readable, Writable):
    """Двусторонняя дружба.

    Attributes:
        _first_user: Первый друг.
        _second_user: Второй друг.
        _is_confirmed: Подтверждена ли.
        _days_friends: Сколько дней дружат.
    """

    def __init__(
        self,
        first_user: str,
        second_user: str,
    ) -> None:
        """Создать дружбу.

        Args:
            first_user: Первый.
            second_user: Второй.

        Raises:
            FriendshipError: Если пользователи совпадают.
        """
        if first_user == second_user:
            raise FriendshipError("нельзя дружить с собой")
        self._first_user: str = first_user
        self._second_user: str = second_user
        self._is_confirmed: bool = False
        self._days_friends: int = 0

    @classmethod
    def _parse(cls, text: str) -> Friendship:
        """Разобрать дружбу из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            first_user=parts[0],
            second_user=parts[1],
        )

    @property
    def first_user(self) -> str:
        """Первый друг.

        Returns:
            Строка.
        """
        return self._first_user

    @property
    def second_user(self) -> str:
        """Второй друг.

        Returns:
            Строка.
        """
        return self._second_user

    @property
    def is_confirmed(self) -> bool:
        """Подтверждена ли.

        Returns:
            ``True``, если подтверждена.
        """
        return self._is_confirmed

    def confirm(self) -> None:
        """Подтвердить дружбу.

        Returns:
            Ничего не возвращает.
        """
        self._is_confirmed = True

    def increment_days(self, days: int = 1) -> None:
        """Увеличить счётчик дней.

        Args:
            days: Сколько дней добавить.

        Returns:
            Ничего не возвращает.
        """
        self._days_friends += days

    def has_user(self, username: str) -> bool:
        """Проверить участие пользователя.

        Args:
            username: Имя пользователя.

        Returns:
            ``True``, если участвует.
        """
        return username in (self._first_user, self._second_user)

    def is_long_term(self) -> bool:
        """Проверить долгую дружбу.

        Returns:
            ``True``, если больше 365 дней.
        """
        return self._days_friends > 365

    def __eq__(self, other: object) -> bool:
        """Сравнить две дружбы.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении пары.
        """
        if not isinstance(other, Friendship):
            return NotImplemented
        pair_self: tuple[str, str] = (
            self._first_user,
            self._second_user,
        )
        pair_other: tuple[str, str] = (
            other._first_user,
            other._second_user,
        )
        return pair_self == pair_other or pair_self == pair_other[::-1]

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        first: str
        second: str
        first, second = sorted(
            (self._first_user, self._second_user)
        )
        return hash((first, second))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return f"{self._first_user}; {self._second_user}"
