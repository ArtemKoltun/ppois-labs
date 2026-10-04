"""
Тип детали.

Module: common.enums.part_type
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from enum import Enum


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class PartType(Enum):
    """Категория автомобильной детали.

    Attributes:
        PISTON: Поршень.
        CYLINDER: Цилиндр.
        SHAFT: Вал.
        GEAR: Шестерня.
        BEARING: Подшипник.
    """

    PISTON = "piston"
    CYLINDER = "cylinder"
    SHAFT = "shaft"
    GEAR = "gear"
    BEARING = "bearing"

    def __str__(self) -> str:
        """Вернуть человекочитаемое название.

        Returns:
            Строка на русском.
        """
        names: dict[PartType, str] = {
            PartType.PISTON: "поршень",
            PartType.CYLINDER: "цилиндр",
            PartType.SHAFT: "вал",
            PartType.GEAR: "шестерня",
            PartType.BEARING: "подшипник",
        }
        return names[self]
