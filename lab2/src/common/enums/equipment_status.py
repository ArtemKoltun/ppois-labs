"""
Статус оборудования.

Module: common.enums.equipment_status
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from enum import Enum


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class EquipmentStatus(Enum):
    """Состояние единицы оборудования.

    Attributes:
        WORKING: Работает.
        IDLE: Простаивает.
        BROKEN: Сломано.
        MAINTENANCE: На обслуживании.
    """

    WORKING = "working"
    IDLE = "idle"
    BROKEN = "broken"
    MAINTENANCE = "maintenance"

    def __str__(self) -> str:
        """Вернуть человекочитаемое название.

        Returns:
            Строка на русском.
        """
        names: dict[EquipmentStatus, str] = {
            EquipmentStatus.WORKING: "работает",
            EquipmentStatus.IDLE: "простаивает",
            EquipmentStatus.BROKEN: "сломано",
            EquipmentStatus.MAINTENANCE: "на обслуживании",
        }
        return names[self]
