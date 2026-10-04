"""
Партия готовой продукции.

Module: factory.domain.warehouse.batch
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from factory.domain.materials.material_batch import MaterialBatch
from factory.domain.parts.part import Part


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Batch(Readable, Writable):
    """Партия готовой продукции.

    Attributes:
        _number: Номер партии.
        _part: Деталь.
        _quantity: Количество.
        _materials: Использованные партии материалов.
        _produced_date: Дата выпуска.
    """

    def __init__(
        self,
        number: str,
        part: Part,
        quantity: int,
        produced_date: str,
    ) -> None:
        """Создать партию.

        Args:
            number: Номер.
            part: Деталь.
            quantity: Количество.
            produced_date: Дата выпуска.

        Raises:
            ValueError: Если данные некорректны.
        """
        if quantity <= 0:
            raise ValueError("количество должно быть положительным")
        self._number: str = number
        self._part: Part = part
        self._quantity: int = quantity
        self._materials: list[MaterialBatch] = []
        self._produced_date: str = produced_date

    @classmethod
    def _parse(cls, text: str) -> "Batch":
        """Разобрать партию из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        part: Part = Part.from_string(parts[1])
        return cls(
            number=parts[0],
            part=part,
            quantity=int(parts[2]),
            produced_date=parts[3],
        )

    @property
    def number(self) -> str:
        """Номер партии.

        Returns:
            Строка.
        """
        return self._number

    @property
    def quantity(self) -> int:
        """Количество.

        Returns:
            Целое число.
        """
        return self._quantity

    def add_material_batch(self, batch: MaterialBatch) -> None:
        """Добавить использованную партию материала.

        Args:
            batch: Партия материала.

        Returns:
            Ничего не возвращает.
        """
        self._materials.append(batch)

    def materials_count(self) -> int:
        """Вернуть число использованных партий материалов.

        Returns:
            Целое число.
        """
        return len(self._materials)

    def total_material_used(self) -> float:
        """Вернуть суммарный расход материала.

        Returns:
            Килограммы.
        """
        return sum(batch.quantity for batch in self._materials)

    def __eq__(self, other: object) -> bool:
        """Сравнить две партии.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении номеров.
        """
        if not isinstance(other, Batch):
            return NotImplemented
        return self._number == other._number

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._number)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._number}; {self._part}; "
            f"{self._quantity}; {self._produced_date}"
        )
