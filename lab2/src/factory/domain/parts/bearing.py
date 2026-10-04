"""
Подшипник.

Module: factory.domain.parts.bearing
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from factory.domain.parts.part import Part

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_MAX_INNER_DIAMETER: float = 100.0
"""Максимальный внутренний диаметр для малых подшипников."""


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Bearing(Part):
    """Подшипник.

    Attributes:
        _inner_diameter: Внутренний диаметр.
        _outer_diameter: Внешний диаметр.
        _bearing_type: Тип подшипника.
    """

    def __init__(
        self,
        part: Part,
        inner_diameter: float,
        outer_diameter: float,
        bearing_type: str,
    ) -> None:
        """Создать подшипник.

        Args:
            part: Базовая деталь.
            inner_diameter: Внутренний диаметр.
            outer_diameter: Внешний диаметр.
            bearing_type: Тип подшипника.
        """
        super().__init__(
            name=part.name,
            part_type=part._type,
            weight=part.weight,
            specification=part._specification,
            material=part._material,
        )
        self._inner_diameter: float = inner_diameter
        self._outer_diameter: float = outer_diameter
        self._bearing_type: str = bearing_type

    def is_small(self) -> bool:
        """Проверить, малый ли подшипник.

        Returns:
            ``True``, если внутренний диаметр меньше 100 мм.
        """
        return self._inner_diameter < _MAX_INNER_DIAMETER

    def ring_thickness(self) -> float:
        """Рассчитать толщину кольца.

        Returns:
            Толщина в миллиметрах.
        """
        return (self._outer_diameter - self._inner_diameter) / 2
