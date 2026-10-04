"""
Вал.

Module: factory.domain.parts.shaft
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from factory.domain.parts.part import Part


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Shaft(Part):
    """Вал.

    Attributes:
        _length: Длина в миллиметрах.
        _diameter: Диаметр.
        _material_grade: Марка материала.
    """

    def __init__(
        self,
        part: Part,
        length: float,
        diameter: float,
        material_grade: str,
    ) -> None:
        """Создать вал.

        Args:
            part: Базовая деталь.
            length: Длина.
            diameter: Диаметр.
            material_grade: Марка материала.
        """
        super().__init__(
            name=part.name,
            part_type=part._type,
            weight=part.weight,
            specification=part._specification,
            material=part._material,
        )
        self._length: float = length
        self._diameter: float = diameter
        self._material_grade: str = material_grade

    def aspect_ratio(self) -> float:
        """Рассчитать отношение длины к диаметру.

        Returns:
            Безразмерный коэффициент.
        """
        return self._length / self._diameter

    def is_flexible(self) -> bool:
        """Проверить, гибкий ли вал.

        Returns:
            ``True``, если отношение длины к диаметру больше 20.
        """
        return self.aspect_ratio() > 20
    