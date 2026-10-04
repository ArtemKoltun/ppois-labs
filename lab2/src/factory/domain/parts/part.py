"""
Деталь автомобиля.

Module: factory.domain.parts.part
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.enums.part_type import PartType
from common.exceptions.part_exceptions import InvalidPartException
from factory.domain.materials.material import Material
from factory.domain.parts.specification import Specification


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Part(Readable, Writable):
    """Базовая автомобильная деталь.

    Attributes:
        _name: Наименование детали.
        _type: Тип детали.
        _weight: Вес в килограммах.
        _specification: Спецификация.
        _material: Материал изготовления.
    """

    def __init__(
        self,
        name: str,
        part_type: PartType,
        weight: float,
        specification: Specification,
        material: Material,
    ) -> None:
        """Создать деталь.

        Args:
            name: Наименование детали.
            part_type: Тип детали.
            weight: Вес в килограммах.
            specification: Спецификация.
            material: Материал изготовления.

        Raises:
            InvalidPartException: Если данные некорректны.
        """
        if not name:
            raise InvalidPartException("имя детали не может быть пустым")
        if weight <= 0:
            raise InvalidPartException("вес должен быть положительным")
        self._name: str = name
        self._type: PartType = part_type
        self._weight: float = weight
        self._specification: Specification = specification
        self._material: Material = material

    @classmethod
    def _parse(cls, text: str) -> "Part":
        """Разобрать деталь из строки.

        Args:
            text: Строка с полями через запятую.

        Returns:
            Новый экземпляр ``Part``.
        """
        parts: list[str] = [p.strip() for p in text.split(",")]
        material: Material = Material(
            name=parts[4], material_type=parts[5],
            density=float(parts[6]), cost_per_kg=float(parts[7]),
        )
        spec: Specification = Specification(
            part_name=parts[0], tolerance=float(parts[8]),
            surface_finish=parts[9], material_type=parts[5],
        )
        return cls(
            name=parts[0],
            part_type=PartType(parts[1]),
            weight=float(parts[2]),
            specification=spec,
            material=material,
        )

    @property
    def name(self) -> str:
        """Наименование детали.

        Returns:
            Строка.
        """
        return self._name

    @property
    def weight(self) -> float:
        """Вес детали.

        Returns:
            Килограммы.
        """
        return self._weight

    def calculate_cost(self) -> float:
        """Рассчитать стоимость детали по материалу.

        Returns:
            Стоимость в рублях.
        """
        return self._material.calculate_cost(self._weight)

    def get_full_name(self) -> str:
        """Вернуть полное название с типом.

        Returns:
            Строка вида ``"Поршень (piston)"``.
        """
        return f"{self._name} ({self._type})"

    def is_valid(self) -> bool:
        """Проверить корректность детали.

        Returns:
            ``True``, если спецификация и материал валидны.
        """
        return self._specification.is_valid() and self._material.is_valid()

    def __eq__(self, other: object) -> bool:
        """Сравнить две детали.

        Args:
            other: Другой объект.

        Returns:
            ``True``, если совпадают имя, тип и вес.
        """
        if not isinstance(other, Part):
            return NotImplemented
        return (
            self._name == other._name
            and self._type == other._type
            and self._weight == other._weight
        )

    def __hash__(self) -> int:
        """Вернуть хеш детали.

        Returns:
            Целое число.
        """
        return hash((self._name, self._type, self._weight))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через запятую.
        """
        return (
            f"{self._name}, {self._type.value}, {self._weight}, "
            f"{self._specification}, {self._material.name}, "
            f"{self._material.material_type}, "
            f"{self._material.density}, "
            f"{self._material.cost_per_kg}, "
            f"{self._specification.tolerance}, "
            f"{self._specification.surface_finish}"
        )
