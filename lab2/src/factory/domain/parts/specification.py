"""
Спецификация детали.

Module: factory.domain.parts.specification
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.exceptions.part_exceptions import InvalidSpecificationError

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_DEFAULT_TOLERANCE: float = 0.1
"""Допуск по умолчанию в миллиметрах."""


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Specification(Readable, Writable):
    """Техническая спецификация детали.

    Attributes:
        _part_name: Наименование детали.
        _tolerance: Допуск.
        _surface_finish: Чистота поверхности.
        _material_type: Тип материала.
        _notes: Примечания.
    """

    def __init__(
        self,
        part_name: str,
        tolerance: float = _DEFAULT_TOLERANCE,
        surface_finish: str = "Ra 1.6",
        material_type: str = "steel",
        notes: str = "",
    ) -> None:
        """Создать спецификацию.

        Args:
            part_name: Наименование детали.
            tolerance: Допуск.
            surface_finish: Чистота поверхности.
            material_type: Тип материала.
            notes: Примечания.

        Raises:
            InvalidSpecificationError: Если данные некорректны.
        """
        if not part_name:
            raise InvalidSpecificationError(
                "имя детали не может быть пустым"
            )
        if tolerance <= 0:
            raise InvalidSpecificationError(
                "допуск должен быть положительным"
            )
        self._part_name: str = part_name
        self._tolerance: float = tolerance
        self._surface_finish: str = surface_finish
        self._material_type: str = material_type
        self._notes: str = notes

    @classmethod
    def _parse(cls, text: str) -> Specification:
        """Разобрать спецификацию из строки.

        Args:
            text: Строка с полями через запятую.

        Returns:
            Новый экземпляр ``Specification``.
        """
        parts: list[str] = [p.strip() for p in text.split(",")]
        return cls(
            part_name=parts[0],
            tolerance=float(parts[1]),
            surface_finish=parts[2],
            material_type=parts[3],
            notes=parts[4] if len(parts) > 4 else "",
        )

    @property
    def part_name(self) -> str:
        """Наименование детали.

        Returns:
            Строка.
        """
        return self._part_name

    @property
    def tolerance(self) -> float:
        """Допуск.

        Returns:
            Миллиметры.
        """
        return self._tolerance

    @property
    def surface_finish(self) -> str:
        """Чистота поверхности.

        Returns:
            Строка.
        """
        return self._surface_finish

    def is_strict(self) -> bool:
        """Проверить, строгая ли спецификация.

        Returns:
            ``True``, если допуск меньше 0.05 мм.
        """
        return self._tolerance < 0.05

    def update_notes(self, notes: str) -> None:
        """Обновить примечания.

        Args:
            notes: Новые примечания.

        Returns:
            Ничего не возвращает.
        """
        self._notes = notes

    def is_valid(self) -> bool:
        """Проверить корректность спецификации.

        Returns:
            ``True``, если поля непустые и допуск положительный.
        """
        return (
            bool(self._part_name)
            and self._tolerance > 0
            and bool(self._surface_finish)
        )

    def __eq__(self, other: object) -> bool:
        """Сравнить две спецификации.

        Args:
            other: Другой объект.

        Returns:
            ``True``, если совпадают имя и допуск.
        """
        if not isinstance(other, Specification):
            return NotImplemented
        return (
            self._part_name == other._part_name
            and self._tolerance == other._tolerance
        )

    def __hash__(self) -> int:
        """Вернуть хеш спецификации.

        Returns:
            Целое число.
        """
        return hash((self._part_name, self._tolerance))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через запятую.
        """
        return (
            f"{self._part_name}, {self._tolerance}, "
            f"{self._surface_finish}, {self._material_type}, "
            f"{self._notes}"
        )
