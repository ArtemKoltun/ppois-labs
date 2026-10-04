"""
Материал.

Module: factory.domain.materials.material
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.exceptions.material_exceptions import (
    InvalidMaterialError,
)

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Material(Readable, Writable):
    """Материал для изготовления деталей.

    Attributes:
        _name: Наименование.
        _material_type: Тип материала.
        _density: Плотность в кг/м³.
        _cost_per_kg: Стоимость за килограмм.
    """

    def __init__(
        self,
        name: str,
        material_type: str,
        density: float,
        cost_per_kg: float,
    ) -> None:
        """Создать материал.

        Args:
            name: Наименование.
            material_type: Тип материала.
            density: Плотность.
            cost_per_kg: Стоимость за килограмм.

        Raises:
            InvalidMaterialError: Если данные некорректны.
        """
        if not name:
            raise InvalidMaterialError("имя не может быть пустым")
        if density <= 0:
            raise InvalidMaterialError(
                "плотность должна быть положительной"
            )
        if cost_per_kg < 0:
            raise InvalidMaterialError(
                "стоимость не может быть отрицательной"
            )
        self._name: str = name
        self._material_type: str = material_type
        self._density: float = density
        self._cost_per_kg: float = cost_per_kg

    @classmethod
    def _parse(cls, text: str) -> Material:
        """Разобрать материал из строки.

        Args:
            text: Строка с полями через запятую.

        Returns:
            Новый экземпляр ``Material``.
        """
        parts: list[str] = [p.strip() for p in text.split(",")]
        return cls(
            name=parts[0],
            material_type=parts[1],
            density=float(parts[2]),
            cost_per_kg=float(parts[3]),
        )

    @property
    def name(self) -> str:
        """Наименование.

        Returns:
            Строка.
        """
        return self._name

    @property
    def material_type(self) -> str:
        """Тип материала.

        Returns:
            Строка.
        """
        return self._material_type

    @property
    def density(self) -> float:
        """Плотность.

        Returns:
            кг/м³.
        """
        return self._density

    @property
    def cost_per_kg(self) -> float:
        """Стоимость за килограмм.

        Returns:
            Рубли.
        """
        return self._cost_per_kg

    def calculate_cost(self, weight: float) -> float:
        """Рассчитать стоимость по весу.

        Args:
            weight: Вес в килограммах.

        Returns:
            Стоимость в рублях.
        """
        return weight * self._cost_per_kg

    def is_valid(self) -> bool:
        """Проверить корректность материала.

        Returns:
            ``True``, если поля валидны.
        """
        return (
            bool(self._name)
            and self._density > 0
            and self._cost_per_kg >= 0
        )

    def __eq__(self, other: object) -> bool:
        """Сравнить два материала.

        Args:
            other: Другой объект.

        Returns:
            ``True``, если совпадают имя и тип.
        """
        if not isinstance(other, Material):
            return NotImplemented
        return (
            self._name == other._name
            and self._material_type == other._material_type
        )

    def __hash__(self) -> int:
        """Вернуть хеш материала.

        Returns:
            Целое число.
        """
        return hash((self._name, self._material_type))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через запятую.
        """
        return (
            f"{self._name}, {self._material_type}, "
            f"{self._density}, {self._cost_per_kg}"
        )
