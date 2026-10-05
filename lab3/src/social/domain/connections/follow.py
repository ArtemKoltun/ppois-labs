"""
Подписка (односторонняя).

Module: social.domain.connections.follow
"""

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.exceptions.connection_exceptions import FriendshipError


class Follow(Readable, Writable):
    """Односторонняя подписка.

    Attributes:
        _follower: Кто подписан.
        _following: На кого подписан.
        _is_active: Активна ли.
    """

    def __init__(
        self,
        follower: str,
        following: str,
    ) -> None:
        """Создать подписку.

        Args:
            follower: Подписчик.
            following: На кого.

        Raises:
            FriendshipError: Если пользователи совпадают.
        """
        if follower == following:
            raise FriendshipError(
                "нельзя подписаться на самого себя"
            )
        self._follower: str = follower
        self._following: str = following
        self._is_active: bool = True

    @classmethod
    def _parse(cls, text: str) -> Follow:
        """Разобрать подписку из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            follower=parts[0],
            following=parts[1],
        )

    @property
    def follower(self) -> str:
        """Подписчик.

        Returns:
            Строка.
        """
        return self._follower

    @property
    def following(self) -> str:
        """На кого подписан.

        Returns:
            Строка.
        """
        return self._following

    @property
    def is_active(self) -> bool:
        """Активна ли.

        Returns:
            ``True``, если активна.
        """
        return self._is_active

    def unfollow(self) -> None:
        """Отписаться.

        Returns:
            Ничего не возвращает.
        """
        self._is_active = False

    def reactivate(self) -> None:
        """Восстановить подписку.

        Returns:
            Ничего не возвращает.
        """
        self._is_active = True

    def is_mutual(self, other: Follow) -> bool:
        """Проверить взаимность.

        Args:
            other: Другая подписка.

        Returns:
            ``True``, если взаимная.
        """
        return (
            self._follower == other.following
            and self._following == other.follower
        )

    def __eq__(self, other: object) -> bool:
        """Сравнить две подписки.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении пары.
        """
        if not isinstance(other, Follow):
            return NotImplemented
        return (
            self._follower == other._follower
            and self._following == other._following
        )

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash((self._follower, self._following))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return f"{self._follower}; {self._following}"
