"""
Тип материала.

Module: common.enums.material_type
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from enum import Enum

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class MaterialType(Enum):
    """Категория материала.

    Attributes:
        STEEL: Сталь.
        ALUMINUM: Алюминий.
        PLASTIC: Пластик.
    """

    STEEL = "steel"
    ALUMINUM = "aluminum"
    PLASTIC = "plastic"

    def __str__(self) -> str:
        """Вернуть человекочитаемое название.

        Returns:
            Строка на русском.
        """
        names: dict[MaterialType, str] = {
            MaterialType.STEEL: "сталь",
            MaterialType.ALUMINUM: "алюминий",
            MaterialType.PLASTIC: "пластик",
        }
        return names[self]
