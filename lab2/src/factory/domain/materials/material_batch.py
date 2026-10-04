"""
Партия материала.

Module: factory.domain.materials.material_batch
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.exceptions.material_exceptions import (
    InsufficientMaterialException,
)
from factory.domain.materials.material import Material
from factory.domain.materials.supplier import Supplier


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class MaterialBatch(Readable, Writable):
    """Партия материала от поставщика.

    Attributes:
        _material: Материал.
        _supplier: Поставщик.
        _quantity: Количество в килограммах.
        _batch_number: Номер партии.
    """

    def __init__(
        self,
        material: Material,
        supplier: Supplier,
        quantity: float,
        batch_number: str,
    ) -> None:
        """Создать партию.

        Args:
            material: Материал.
            supplier: Поставщик.
            quantity: Количество.
            batch_number: Номер партии.
        """
        self._material: Material = material
        self._supplier: Supplier = supplier
        self._quantity: float = quantity
        self._batch_number: str = batch_number

    @classmethod
    def _parse(cls, text: str) -> "MaterialBatch":
        """Разобрать партию из строки.

        Args:
            text: Строка с полями через запятую.

        Returns:
            Новый экземпляр ``MaterialBatch``.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        material: Material = Material.from_string(parts[0])
        supplier: Supplier = Supplier.from_string(parts[1])
        return cls(
            material=material,
            supplier=supplier,
            quantity=float(parts[2]),
            batch_number=parts[3],
        )

    @property
    def material(self) -> Material:
        """Материал.

        Returns:
            Объект материала.
        """
        return self._material

    @property
    def quantity(self) -> float:
        """Количество.

        Returns:
            Килограммы.
        """
        return self._quantity

    @property
    def supplier(self) -> Supplier:
        """Поставщик.

        Returns:
            Объект поставщика.
        """
        return self._supplier

    def consume(self, amount: float) -> None:
        """Израсходовать часть партии.

        Args:
            amount: Количество для списания.

        Returns:
            Ничего не возвращает.

        Raises:
            InsufficientMaterialException: Если не хватает материала.
        """
        if amount > self._quantity:
            raise InsufficientMaterialException(
                f"недостаточно материала: нужно {amount}, "
                f"есть {self._quantity}"
            )
        self._quantity -= amount

    def add(self, amount: float) -> None:
        """Добавить материал в партию.

        Args:
            amount: Количество.

        Returns:
            Ничего не возвращает.
        """
        self._quantity += amount

    def is_empty(self) -> bool:
        """Проверить, пуста ли партия.

        Returns:
            ``True``, если количество равно нулю.
        """
        return self._quantity <= 0

    def __eq__(self, other: object) -> bool:
        """Сравнить две партии.

        Args:
            other: Другой объект.

        Returns:
            ``True``, если совпадают номер партии.
        """
        if not isinstance(other, MaterialBatch):
            return NotImplemented
        return self._batch_number == other._batch_number

    def __hash__(self) -> int:
        """Вернуть хеш партии.

        Returns:
            Целое число.
        """
        return hash(self._batch_number)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._material}; {self._supplier}; "
            f"{self._quantity}; {self._batch_number}"
        )
