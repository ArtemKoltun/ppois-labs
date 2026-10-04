"""
Токарный станок.

Module: factory.domain.equipment.lathe
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from factory.domain.equipment.machine import Machine

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Lathe(Machine):
    """Токарный станок.

    Attributes:
        _max_diameter: Максимальный диаметр заготовки.
        _max_length: Максимальная длина заготовки.
    """

    def __init__(
        self,
        machine: Machine,
        max_diameter: float,
        max_length: float,
    ) -> None:
        """Создать токарный станок.

        Args:
            machine: Базовый станок.
            max_diameter: Максимальный диаметр.
            max_length: Максимальная длина.
        """
        super().__init__(
            equipment=machine,
            power_kw=machine._power_kw,
            max_rpm=machine._max_rpm,
            accuracy_class=machine._accuracy_class,
        )
        self._max_diameter: float = max_diameter
        self._max_length: float = max_length

    def can_process(self, diameter: float, length: float) -> bool:
        """Проверить, можно ли обработать заготовку.

        Args:
            diameter: Диаметр заготовки.
            length: Длина заготовки.

        Returns:
            ``True``, если заготовка помещается.
        """
        return (
            diameter <= self._max_diameter
            and length <= self._max_length
        )

    def is_large_lathe(self) -> bool:
        """Проверить, крупный ли станок.

        Returns:
            ``True``, если диаметр больше 400 мм.
        """
        return self._max_diameter > 400
