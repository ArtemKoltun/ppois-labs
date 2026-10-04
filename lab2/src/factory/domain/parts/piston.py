"""
Поршень.

Module: factory.domain.parts.piston
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from factory.domain.parts.part import Part


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Piston(Part):
    """Поршень двигателя.

    Attributes:
        _diameter: Диаметр в миллиметрах.
        _height: Высота в миллиметрах.
        _compression_ratio: Степень сжатия.
    """

    def __init__(
        self,
        part: Part,
        diameter: float,
        height: float,
        compression_ratio: float,
    ) -> None:
        """Создать поршень на основе детали.

        Args:
            part: Базовая деталь.
            diameter: Диаметр.
            height: Высота.
            compression_ratio: Степень сжатия.
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
        self._compression_ratio: float = compression_ratio

    def volume(self) -> float:
        """Рассчитать объём поршня.

        Returns:
            Объём в кубических миллиметрах.
        """
        import math

        radius: float = self._diameter / 2
        return math.pi * radius * radius * self._height

    def is_high_compression(self) -> bool:
        """Проверить, высокофорсированный ли поршень.

        Returns:
            ``True``, если степень сжатия больше 10.
        """
        return self._compression_ratio > 10
