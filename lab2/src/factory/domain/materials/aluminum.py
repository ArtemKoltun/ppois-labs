"""
Алюминий.

Module: factory.domain.materials.aluminum
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from factory.domain.materials.material import Material

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Aluminum(Material):
    """Алюминиевый сплав.

    Attributes:
        _alloy: Марка сплава.
        _temper: Состояние поставки.
    """

    def __init__(
        self,
        material: Material,
        alloy: str,
        temper: str,
    ) -> None:
        """Создать алюминий.

        Args:
            material: Базовый материал.
            alloy: Марка сплава.
            temper: Состояние.
        """
        super().__init__(
            name=material.name,
            material_type=material.material_type,
            density=material.density,
            cost_per_kg=material.cost_per_kg,
        )
        self._alloy: str = alloy
        self._temper: str = temper

    def is_heat_treated(self) -> bool:
        """Проверить, термообработан ли сплав.

        Returns:
            ``True``, если состояние содержит "T".
        """
        return "T" in self._temper

    def is_lightweight(self) -> bool:
        """Проверить, лёгкий ли сплав.

        Returns:
            ``True``, если плотность меньше 2800 кг/м³.
        """
        return self._density < 2800
