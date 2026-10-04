"""
Пластик.

Module: factory.domain.materials.plastic
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from factory.domain.materials.material import Material

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Plastic(Material):
    """Полимерный материал.

    Attributes:
        _polymer_type: Тип полимера.
        _melting_point: Температура плавления.
    """

    def __init__(
        self,
        material: Material,
        polymer_type: str,
        melting_point: float,
    ) -> None:
        """Создать пластик.

        Args:
            material: Базовый материал.
            polymer_type: Тип полимера.
            melting_point: Температура плавления.
        """
        super().__init__(
            name=material.name,
            material_type=material.material_type,
            density=material.density,
            cost_per_kg=material.cost_per_kg,
        )
        self._polymer_type: str = polymer_type
        self._melting_point: float = melting_point

    def is_thermoplastic(self) -> bool:
        """Проверить, термопластичен ли материал.

        Returns:
            ``True``, если температура плавления ниже 250 °C.
        """
        return self._melting_point < 250

    def is_recyclable(self) -> bool:
        """Проверить, перерабатываем ли материал.

        Returns:
            ``True``, если тип полимера в списке перерабатываемых.
        """
        recyclable: set[str] = {"PET", "HDPE", "PP", "PS"}
        return self._polymer_type in recyclable
