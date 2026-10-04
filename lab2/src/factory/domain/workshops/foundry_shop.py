"""
Литейный цех.

Module: factory.domain.workshops.foundry_shop
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from factory.domain.workshops.workshop import Workshop

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class FoundryShop(Workshop):
    """Литейный цех.

    Attributes:
        _furnace_count: Число печей.
        _max_temperature: Максимальная температура.
        _daily_capacity: Дневная производительность.
    """

    def __init__(
        self,
        workshop: Workshop,
        furnace_count: int,
        max_temperature: float,
        daily_capacity: float,
    ) -> None:
        """Создать литейный цех.

        Args:
            workshop: Базовый цех.
            furnace_count: Число печей.
            max_temperature: Максимальная температура.
            daily_capacity: Производительность.
        """
        super().__init__(
            name=workshop.name,
            number=workshop.number,
            area=workshop._area,
            workshop_head=workshop._workshop_head,
        )
        self._furnace_count: int = furnace_count
        self._max_temperature: float = max_temperature
        self._daily_capacity: float = daily_capacity

    def can_melt_steel(self) -> bool:
        """Проверить, плавит ли цех сталь.

        Returns:
            ``True``, если температура выше 1500 °C.
        """
        return self._max_temperature > 1500

    def produce(self, days: int) -> float:
        """Рассчитать выпуск за период.

        Args:
            days: Число дней.

        Returns:
            Объём производства.
        """
        return self._daily_capacity * days

    def is_large(self) -> bool:
        """Проверить, крупный ли цех.

        Returns:
            ``True``, если печей больше трёх.
        """
        return self._furnace_count > 3
