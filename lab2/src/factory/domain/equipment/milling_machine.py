"""
Фрезерный станок.

Module: factory.domain.equipment.milling_machine
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from factory.domain.equipment.machine import Machine


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class MillingMachine(Machine):
    """Фрезерный станок.

    Attributes:
        _axes_count: Число осей.
        _table_size: Размер стола в мм.
    """

    def __init__(
        self,
        machine: Machine,
        axes_count: int,
        table_size: float,
    ) -> None:
        """Создать фрезерный станок.

        Args:
            machine: Базовый станок.
            axes_count: Число осей.
            table_size: Размер стола.
        """
        super().__init__(
            equipment=machine,
            power_kw=machine._power_kw,
            max_rpm=machine._max_rpm,
            accuracy_class=machine._accuracy_class,
        )
        self._axes_count: int = axes_count
        self._table_size: float = table_size

    def is_multiaxis(self) -> bool:
        """Проверить, многоосевой ли станок.

        Returns:
            ``True``, если осей больше трёх.
        """
        return self._axes_count > 3

    def can_process_part(self, size: float) -> bool:
        """Проверить, помещается ли деталь на стол.

        Args:
            size: Размер детали.

        Returns:
            ``True``, если размер не превышает стол.
        """
        return size <= self._table_size
