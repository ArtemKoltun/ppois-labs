"""
Тесты класса Batch.

Module: tests.factory.domain.warehouse.test_batch
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from factory.domain.materials.material import Material
from factory.domain.materials.material_batch import MaterialBatch
from factory.domain.materials.supplier import Supplier
from factory.domain.parts.part import Part
from factory.domain.warehouse.batch import Batch

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_material_batch(
    material: Material,
    supplier: Supplier,
    quantity: float = 50.0,
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
        batch_number="MB-001",
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestBatch:
    """Проверки класса Batch."""

    def test_creates(self, piston_part: Part) -> None:
        """Партия создаётся.

        Args:
            piston_part: Фикстура детали.
        """
        batch: Batch = Batch(
            number="B-001",
            part=piston_part,
            quantity=100,
            produced_date="2026-02-01",
        )
        assert batch.number == "B-001"
        assert batch.quantity == 100

    def test_zero_quantity_raises(self, piston_part: Part) -> None:
        """Нулевое количество недопустимо.

        Args:
            piston_part: Фикстура детали.
        """
        with pytest.raises(ValueError):
            Batch(
                number="X",
                part=piston_part,
                quantity=0,
                produced_date="X",
            )

    def test_add_material_batch(
        self,
        piston_part: Part,
        steel: Material,
        supplier: Supplier,
    ) -> None:
        """add_material_batch добавляет.

        Args:
            piston_part: Фикстура детали.
            steel: Фикстура материала.
            supplier: Фикстура поставщика.
        """
        batch: Batch = Batch(
            number="B-001",
            part=piston_part,
            quantity=100,
            produced_date="X",
        )
        mb: MaterialBatch = _make_material_batch(steel, supplier)
        batch.add_material_batch(mb)
        assert batch.materials_count() == 1

    def test_total_material_used(
        self,
        piston_part: Part,
        steel: Material,
        supplier: Supplier,
    ) -> None:
        """total_material_used суммирует.

        Args:
            piston_part: Фикстура детали.
            steel: Фикстура материала.
            supplier: Фикстура поставщика.
        """
        batch: Batch = Batch(
            number="B-001",
            part=piston_part,
            quantity=100,
            produced_date="X",
        )
        batch.add_material_batch(
            _make_material_batch(steel, supplier, quantity=30.0)
        )
        batch.add_material_batch(
            _make_material_batch(steel, supplier, quantity=20.0)
        )
        assert batch.total_material_used() == 50.0

    def test_equality(self, piston_part: Part) -> None:
        """Равные по номеру.

        Args:
            piston_part: Фикстура детали.
        """
        a: Batch = Batch(
            number="B-001",
            part=piston_part,
            quantity=100,
            produced_date="X",
        )
        b: Batch = Batch(
            number="B-001",
            part=piston_part,
            quantity=50,
            produced_date="Y",
        )
        assert a == b
        assert a != "not a batch"

    def test_hash(self, piston_part: Part) -> None:
        """Хеш по номеру.

        Args:
            piston_part: Фикстура детали.
        """
        a: Batch = Batch(
            number="B-001",
            part=piston_part,
            quantity=1,
            produced_date="X",
        )
        b: Batch = Batch(
            number="B-001",
            part=piston_part,
            quantity=2,
            produced_date="Y",
        )
        assert hash(a) == hash(b)

    def test_str(self, piston_part: Part) -> None:
        """str возвращает номер.

        Args:
            piston_part: Фикстура детали.
        """
        batch: Batch = Batch(
            number="B-42",
            part=piston_part,
            quantity=100,
            produced_date="X",
        )
        assert "B-42" in str(batch)
