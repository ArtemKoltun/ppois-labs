"""
Станок.

Module: factory.domain.equipment.machine
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.enums.equipment_status import EquipmentStatus
from factory.domain.equipment.equipment import Equipment


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Machine(Equipment):
    """Станок.

    Attributes:
        _power_kw: Мощность в кВт.
        _max_rpm: Максимальные обороты.
        _accuracy_class: Класс точности.
    """

    def __init__(
        self,
        equipment: Equipment,
        power_kw: float,
        max_rpm: int,
        accuracy_class: str,
    ) -> None:
        """Создать станок.

        Args:
            equipment: Базовая единица оборудования.
            power_kw: Мощность.
            max_rpm: Максимальные обороты.
            accuracy_class: Класс точности.
        """
        super().__init__(
            name=equipment.name,
            inventory_number=equipment._inventory_number,
            purchase_year=equipment._purchase_year,
            status=equipment.status,
        )
        self._power_kw: float = power_kw
        self._max_rpm: int = max_rpm
        self._accuracy_class: str = accuracy_class

    def is_high_power(self) -> bool:
        """Проверить, мощный ли станок.

        Returns:
            ``True``, если мощность больше 15 кВт.
        """
        return self._power_kw > 15

    def calculate_output(self, minutes: float) -> int:
        """Рассчитать число операций за указанное время.

        Args:
            minutes: Длительность работы в минутах.

        Returns:
            Число операций.
        """
        return int(minutes * self._max_rpm / 1000)

    def needs_maintenance(self) -> bool:
        """Проверить, нужно ли ТО.

        Returns:
            ``True``, если отработано больше 1000 часов.
        """
        return self._hours_worked > 1000
