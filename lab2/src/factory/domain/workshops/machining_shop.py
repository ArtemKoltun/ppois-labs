"""
Механический цех.

Module: factory.domain.workshops.machining_shop
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from factory.domain.workshops.workshop import Workshop


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class MachiningShop(Workshop):
    """Механический цех — обработка деталей резанием.

    Attributes:
        _machine_count: Число станков.
        _shifts: Число смен в сутки.
    """

    def __init__(
        self,
        workshop: Workshop,
        machine_count: int,
        shifts: int,
    ) -> None:
        """Создать механический цех.

        Args:
            workshop: Базовый цех.
            machine_count: Число станков.
            shifts: Число смен.
        """
        super().__init__(
            name=workshop.name,
            number=workshop.number,
            area=workshop._area,
            workshop_head=workshop._workshop_head,
        )
        self._machine_count: int = machine_count
        self._shifts: int = shifts

    def daily_capacity(self) -> int:
        """Рассчитать дневную производительность.

        Returns:
            Число операций.
        """
        return self._machine_count * self._shifts * 8

    def is_round_the_clock(self) -> bool:
        """Проверить, работает ли цех круглосуточно.

        Returns:
            ``True``, если смен три.
        """
        return self._shifts == 3

    def is_highly_automated(self) -> bool:
        """Проверить уровень автоматизации.

        Returns:
            ``True``, если станков больше 20.
        """
        return self._machine_count > 20
