"""
Рекламное объявление.

Module: social.domain.ads.advertisement
"""

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.exceptions.connection_exceptions import AdCampaignError


class Advertisement(Readable, Writable):
    """Рекламное объявление.

    Attributes:
        _title: Заголовок.
        _advertiser: Рекламодатель.
        _budget: Бюджет.
        _impressions: Число показов.
        _clicks: Число кликов.
        _is_active: Активна ли.
    """

    def __init__(
        self,
        title: str,
        advertiser: str,
        budget: float,
    ) -> None:
        """Создать объявление.

        Args:
            title: Заголовок.
            advertiser: Рекламодатель.
            budget: Бюджет.

        Raises:
            AdCampaignError: Если данные некорректны.
        """
        if not title or not advertiser:
            raise AdCampaignError(
                "заголовок и рекламодатель обязательны"
            )
        if budget <= 0:
            raise AdCampaignError("бюджет должен быть положительным")
        self._title: str = title
        self._advertiser: str = advertiser
        self._budget: float = budget
        self._impressions: int = 0
        self._clicks: int = 0
        self._is_active: bool = True

    @classmethod
    def _parse(cls, text: str) -> Advertisement:
        """Разобрать объявление из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            title=parts[0],
            advertiser=parts[1],
            budget=float(parts[2]),
        )

    @property
    def title(self) -> str:
        """Заголовок.

        Returns:
            Строка.
        """
        return self._title

    @property
    def budget(self) -> float:
        """Бюджет.

        Returns:
            Число.
        """
        return self._budget

    @property
    def impressions(self) -> int:
        """Число показов.

        Returns:
            Целое число.
        """
        return self._impressions

    @property
    def clicks(self) -> int:
        """Число кликов.

        Returns:
            Целое число.
        """
        return self._clicks

    def show(self) -> None:
        """Отметить показ.

        Returns:
            Ничего не возвращает.
        """
        self._impressions += 1

    def click(self) -> None:
        """Отметить клик.

        Returns:
            Ничего не возвращает.
        """
        self._clicks += 1

    def pause(self) -> None:
        """Приостановить.

        Returns:
            Ничего не возвращает.
        """
        self._is_active = False

    def resume(self) -> None:
        """Возобновить.

        Returns:
            Ничего не возвращает.
        """
        self._is_active = True

    def ctr(self) -> float:
        """CTR — click-through rate.

        Returns:
            Число от 0 до 1.
        """
        if self._impressions == 0:
            return 0.0
        return self._clicks / self._impressions

    def cost_per_click(self) -> float:
        """Стоимость клика.

        Returns:
            Число.
        """
        if self._clicks == 0:
            return 0.0
        return self._budget / self._clicks

    def is_effective(self) -> bool:
        """Проверить эффективность.

        Returns:
            ``True``, если CTR больше 2%.
        """
        return self.ctr() > 0.02

    def __eq__(self, other: object) -> bool:
        """Сравнить два объявления.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении заголовка.
        """
        if not isinstance(other, Advertisement):
            return NotImplemented
        return self._title == other._title

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._title)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._title}; {self._advertiser}; {self._budget}"
        )
