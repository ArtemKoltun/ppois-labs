"""
Рекламная кампания.

Module: social.domain.ads.ad_campaign
"""

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.exceptions.connection_exceptions import AdCampaignError
from social.domain.ads.advertisement import Advertisement


class AdCampaign(Readable, Writable):
    """Рекламная кампания.

    Attributes:
        _name: Название.
        _advertisements: Список объявлений.
        _total_budget: Общий бюджет.
        _is_running: Запущена ли.
        _target_age_min: Минимальный возраст аудитории.
    """

    def __init__(
        self,
        name: str,
        total_budget: float,
        target_age_min: int = 18,
    ) -> None:
        """Создать кампанию.

        Args:
            name: Название.
            total_budget: Бюджет.
            target_age_min: Мин. возраст.

        Raises:
            AdCampaignError: Если данные некорректны.
        """
        if not name:
            raise AdCampaignError("название не может быть пустым")
        if total_budget <= 0:
            raise AdCampaignError(
                "бюджет должен быть положительным"
            )
        if target_age_min < 0:
            raise AdCampaignError(
                "минимальный возраст не может быть отрицательным"
            )
        self._name: str = name
        self._advertisements: list[Advertisement] = []
        self._total_budget: float = total_budget
        self._is_running: bool = False
        self._target_age_min: int = target_age_min

    @classmethod
    def _parse(cls, text: str) -> AdCampaign:
        """Разобрать кампанию из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            name=parts[0],
            total_budget=float(parts[1]),
            target_age_min=int(parts[2]),
        )

    @property
    def name(self) -> str:
        """Название.

        Returns:
            Строка.
        """
        return self._name

    @property
    def total_budget(self) -> float:
        """Общий бюджет.

        Returns:
            Число.
        """
        return self._total_budget

    def add_advertisement(self, ad: Advertisement) -> None:
        """Добавить объявление.

        Args:
            ad: Объявление.

        Returns:
            Ничего не возвращает.
        """
        self._advertisements.append(ad)

    def advertisements_count(self) -> int:
        """Число объявлений.

        Returns:
            Целое число.
        """
        return len(self._advertisements)

    def start(self) -> None:
        """Запустить кампанию.

        Returns:
            Ничего не возвращает.

        Raises:
            AdCampaignError: Если нет объявлений.
        """
        if not self._advertisements:
            raise AdCampaignError(
                "нельзя запустить кампанию без объявлений"
            )
        self._is_running = True

    def stop(self) -> None:
        """Остановить кампанию.

        Returns:
            Ничего не возвращает.
        """
        self._is_running = False

    def is_running(self) -> bool:
        """Проверить активность.

        Returns:
            ``True``, если запущена.
        """
        return self._is_running

    def total_clicks(self) -> int:
        """Суммарные клики.

        Returns:
            Целое число.
        """
        return sum(ad.clicks for ad in self._advertisements)

    def __eq__(self, other: object) -> bool:
        """Сравнить две кампании.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении названия.
        """
        if not isinstance(other, AdCampaign):
            return NotImplemented
        return self._name == other._name

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._name)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._name}; {self._total_budget}; "
            f"{self._target_age_min}"
        )
