"""
Шестерня.

Module: factory.domain.parts.gear
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from factory.domain.parts.part import Part


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Gear(Part):
    """Зубчатое колесо.

    Attributes:
        _teeth_count: Число зубьев.
        _module: Модуль зацепления.
        _outer_diameter: Внешний диаметр.
    """

    def __init__(
        self,
        part: Part,
        teeth_count: int,
        module: float,
        outer_diameter: float,
    ) -> None:
        """Создать шестерню.

        Args:
            part: Базовая деталь.
            teeth_count: Число зубьев.
            module: Модуль зацепления.
            outer_diameter: Внешний диаметр.
        """
        super().__init__(
            name=part.name,
            part_type=part._type,
            weight=part.weight,
            specification=part._specification,
            material=part._material,
        )
        self._teeth_count: int = teeth_count
        self._module: float = module
        self._outer_diameter: float = outer_diameter

    def pitch_diameter(self) -> float:
        """Рассчитать делительный диаметр.

        Returns:
            Диаметр в миллиметрах.
        """
        return self._module * self._teeth_count

    def is_reduction_gear(self, other: "Gear") -> bool:
        """Проверить, является ли шестерня понижающей.

        Args:
            other: Парная шестерня.

        Returns:
            ``True``, если зубьев больше, чем у парной.
        """
        return self._teeth_count > other._teeth_count
