"""
Тесты класса MaterialBatch.

Module: tests.factory.domain.materials.test_material_batch
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.exceptions import InsufficientMaterialException
from factory.domain.materials.material import Material
from factory.domain.materials.material_batch import MaterialBatch
from factory.domain.materials.supplier import Supplier


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_batch(
    material: Material,
    supplier: Supplier,
    quantity: float = 100.0,
) -> MaterialBatch:
    """Создать партию материала.

    Args:
        material: Материал.
        supplier: Поставщик.
        quantity: Количество.

    Returns:
        Объект ``MaterialBatch``.
    """
    return MaterialBatch(
        material=material,
        supplier=supplier,
        quantity=quantity,
        batch_number="B-001",
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestMaterialBatch:
    """Проверки класса MaterialBatch."""

    def test_creates(
        self,
        steel: Material,
        supplier: Supplier,
    ) -> None:
        """Партия создаётся.

        Args:
            steel: Фикстура материала.
            supplier: Фикстура поставщика.
        """
        batch: MaterialBatch = _make_batch(steel, supplier)
        assert batch.material == steel
        assert batch.supplier == supplier
        assert batch.quantity == 100.0

    def test_consume(
        self,
        steel: Material,
        supplier: Supplier,
    ) -> None:
        """consume уменьшает количество.

        Args:
            steel: Фикстура материала.
            supplier: Фикстура поставщика.
        """
        batch: MaterialBatch = _make_batch(steel, supplier)
        batch.consume(30.0)
        assert batch.quantity == 70.0

    def test_consume_too_much_raises(
        self,
        steel: Material,
        supplier: Supplier,
    ) -> None:
        """consume больше остатка падает.

        Args:
            steel: Фикстура материала.
            supplier: Фикстура поставщика.
        """
        batch: MaterialBatch = _make_batch(steel, supplier, quantity=10.0)
        with pytest.raises(InsufficientMaterialException):
            batch.consume(50.0)

    def test_add(
        self,
        steel: Material,
        supplier: Supplier,
    ) -> None:
        """add увеличивает количество.

        Args:
            steel: Фикстура материала.
            supplier: Фикстура поставщика.
        """
        batch: MaterialBatch = _make_batch(steel, supplier)
        batch.add(50.0)
        assert batch.quantity == 150.0

    def test_is_empty(
        self,
        steel: Material,
        supplier: Supplier,
    ) -> None:
        """is_empty проверяет количество.

        Args:
            steel: Фикстура материала.
            supplier: Фикстура поставщика.
        """
        batch: MaterialBatch = _make_batch(steel, supplier)
        assert not batch.is_empty()
        batch.consume(100.0)
        assert batch.is_empty()

    def test_equality(
        self,
        steel: Material,
        supplier: Supplier,
    ) -> None:
        """Партии равны по номеру.

        Args:
            steel: Фикстура материала.
            supplier: Фикстура поставщика.
        """
        a: MaterialBatch = _make_batch(steel, supplier)
        b: MaterialBatch = _make_batch(steel, supplier)
        assert a == b
        assert a != "not a batch"

    def test_hash(
        self,
        steel: Material,
        supplier: Supplier,
    ) -> None:
        """Одинаковые партии имеют одинаковый хеш.

        Args:
            steel: Фикстура материала.
            supplier: Фикстура поставщика.
        """
        a: MaterialBatch = _make_batch(steel, supplier)
        b: MaterialBatch = _make_batch(steel, supplier)
        assert hash(a) == hash(b)

    def test_str(
        self,
        steel: Material,
        supplier: Supplier,
    ) -> None:
        """str возвращает поля.

        Args:
            steel: Фикстура материала.
            supplier: Фикстура поставщика.
        """
        batch: MaterialBatch = _make_batch(steel, supplier)
        text: str = str(batch)
        assert "B-001" in text
