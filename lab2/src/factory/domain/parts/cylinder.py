"""
Цилиндр.

Module: factory.domain.parts.cylinder
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from factory.domain.parts.part import Part


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Cylinder(Part):
    """Цилиндр двигателя.

    Attributes:
        _diameter: Внутренний диаметр.
        _height: Высота.
        _wall_thickness: Толщина стенки.
    """

    def __init__(
        self,
        part: Part,
        diameter: float,
        height: float,
        wall_thickness: float,
    ) -> None:
        """Создать цилиндр.

        Args:
            part: Базовая деталь.
            diameter: Внутренний диаметр.
            height: Высота.
            wall_thickness: Толщина стенки.
        """
        super().__init__(
            name=part.name,
            part_type=part._type,
            weight=part.weight,
            specification=part._specification,
            material=part._material,
        )
        self._diameter: float = diameter
        self._height: float = height
        self._wall_thickness: float = wall_thickness

    def internal_volume(self) -> float:
        """Рассчитать внутренний объём.

        Returns:
            Объём в кубических миллиметрах.
        """
        import math

        radius: float = self._diameter / 2
        return math.pi * radius * radius * self._height

    def is_thin_walled(self) -> bool:
        """Проверить, тонкостенный ли цилиндр.

        Returns:
            ``True``, если толщина стенки меньше 5 мм.
        """
        return self._wall_thickness < 5
