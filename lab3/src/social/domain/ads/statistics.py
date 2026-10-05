"""
Статистика рекламной площадки.

Module: social.domain.ads.statistics
"""

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from social.domain.ads.advertisement import Advertisement


class Statistics(Readable, Writable):
    """Статистика рекламных показов.

    Attributes:
        _period: Период.
        _advertisements: Учтённые объявления.
        _total_impressions: Всего показов.
        _total_clicks: Всего кликов.
    """

    def __init__(self, period: str) -> None:
        """Создать статистику.

        Args:
            period: Период.
        """
        self._period: str = period
        self._advertisements: list[Advertisement] = []
        self._total_impressions: int = 0
        self._total_clicks: int = 0

    @classmethod
    def _parse(cls, text: str) -> Statistics:
        """Разобрать статистику из строки.

        Args:
            text: Период.

        Returns:
            Новый экземпляр.
        """
        return cls(period=text.strip())

    @property
    def period(self) -> str:
        """Период.

        Returns:
            Строка.
        """
        return self._period

    def add_advertisement(self, ad: Advertisement) -> None:
        """Учесть объявление.

        Args:
            ad: Объявление.

        Returns:
            Ничего не возвращает.
        """
        self._advertisements.append(ad)
        self._total_impressions += ad.impressions
        self._total_clicks += ad.clicks

    def advertisements_count(self) -> int:
        """Число объявлений.

        Returns:
            Целое число.
        """
        return len(self._advertisements)

    def total_ctr(self) -> float:
        """Общий CTR.

        Returns:
            Число от 0 до 1.
        """
        if self._total_impressions == 0:
            return 0.0
        return self._total_clicks / self._total_impressions

    def is_profitable(self) -> bool:
        """Проверить прибыльность.

        Returns:
            ``True``, если CTR больше 3%.
        """
        return self.total_ctr() > 0.03

    def best_advertisement(self) -> Advertisement | None:
        """Найти лучшую рекламу.

        Returns:
            Объявление или ``None``.
        """
        if not self._advertisements:
            return None
        return max(self._advertisements, key=lambda a: a.ctr())

    def __eq__(self, other: object) -> bool:
        """Сравнить две статистики.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении периода.
        """
        if not isinstance(other, Statistics):
            return NotImplemented
        return self._period == other._period

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._period)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка.
        """
        return self._period
