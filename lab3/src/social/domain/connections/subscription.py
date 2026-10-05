"""
Платная подписка на автора.

Module: social.domain.connections.subscription
"""

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.exceptions.connection_exceptions import FriendshipError


class Subscription(Readable, Writable):
    """Платная подписка на автора.

    Attributes:
        _subscriber: Подписчик.
        _author: Автор.
        _price_per_month: Цена в месяц.
        _months: Длительность.
    """

    def __init__(
        self,
        subscriber: str,
        author: str,
        price_per_month: float,
        months: int = 1,
    ) -> None:
        """Создать подписку.

        Args:
            subscriber: Подписчик.
            author: Автор.
            price_per_month: Цена.
            months: Длительность.

        Raises:
            FriendshipError: Если данные некорректны.
        """
        if subscriber == author:
            raise FriendshipError(
                "нельзя подписаться на себя"
            )
        if price_per_month <= 0 or months <= 0:
            raise FriendshipError(
                "цена и длительность должны быть положительными"
            )
        self._subscriber: str = subscriber
        self._author: str = author
        self._price_per_month: float = price_per_month
        self._months: int = months

    @classmethod
    def _parse(cls, text: str) -> Subscription:
        """Разобрать подписку из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            subscriber=parts[0],
            author=parts[1],
            price_per_month=float(parts[2]),
            months=int(parts[3]),
        )

    @property
    def subscriber(self) -> str:
        """Подписчик.

        Returns:
            Строка.
        """
        return self._subscriber

    @property
    def author(self) -> str:
        """Автор.

        Returns:
            Строка.
        """
        return self._author

    @property
    def months(self) -> int:
        """Длительность.

        Returns:
            Месяцы.
        """
        return self._months

    def total_price(self) -> float:
        """Полная стоимость.

        Returns:
            Сумма.
        """
        return self._price_per_month * self._months

    def extend(self, months: int) -> None:
        """Продлить.

        Args:
            months: На сколько месяцев.

        Returns:
            Ничего не возвращает.
        """
        self._months += months

    def is_annual(self) -> bool:
        """Проверить годовую подписку.

        Returns:
            ``True``, если 12 месяцев и больше.
        """
        return self._months >= 12

    def __eq__(self, other: object) -> bool:
        """Сравнить две подписки.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении пары.
        """
        if not isinstance(other, Subscription):
            return NotImplemented
        return (
            self._subscriber == other._subscriber
            and self._author == other._author
        )

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash((self._subscriber, self._author))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._subscriber}; {self._author}; "
            f"{self._price_per_month}; {self._months}"
        )
