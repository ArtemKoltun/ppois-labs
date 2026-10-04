"""
Тесты класса StorageUnit.

Module: tests.factory.domain.warehouse.test_storage_unit
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from factory.domain.warehouse.storage_unit import StorageUnit


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestStorageUnit:
    """Проверки класса StorageUnit."""

    def test_creates(self) -> None:
        """Единица хранения создаётся."""
        unit: StorageUnit = StorageUnit(
            code="A-01",
            unit_type="стеллаж",
            max_weight=1000.0,
        )
        assert unit.code == "A-01"
        assert unit.current_weight == 0.0

    def test_empty_code_raises(self) -> None:
        """Пустой код недопустим."""
        with pytest.raises(ValueError):
            StorageUnit(code="", unit_type="X", max_weight=100.0)

    def test_zero_max_weight_raises(self) -> None:
        """Нулевой максимум недопустим."""
        with pytest.raises(ValueError):
            StorageUnit(code="X", unit_type="X", max_weight=0.0)

    def test_load(self) -> None:
        """load загружает.

        Returns:
            Ничего не возвращает.
        """
        unit: StorageUnit = StorageUnit(
            code="A-01", unit_type="стеллаж", max_weight=1000.0
        )
        unit.load(500.0)
        assert unit.current_weight == 500.0

    def test_load_over_raises(self) -> None:
        """Превышение падает."""
        unit: StorageUnit = StorageUnit(
            code="A-01", unit_type="стеллаж", max_weight=1000.0
        )
        with pytest.raises(ValueError):
            unit.load(2000.0)

    def test_unload(self) -> None:
        """unload обнуляет."""
        unit: StorageUnit = StorageUnit(
            code="A-01", unit_type="стеллаж", max_weight=1000.0
        )
        unit.load(500.0)
        unit.unload()
        assert unit.current_weight == 0.0

    def test_is_empty(self) -> None:
        """is_empty проверяет пустоту."""
        unit: StorageUnit = StorageUnit(
            code="A-01", unit_type="стеллаж", max_weight=1000.0
        )
        assert unit.is_empty()
        unit.load(500.0)
        assert not unit.is_empty()

    def test_is_overloaded(self) -> None:
        """is_overloaded для нормальной единицы."""
        unit: StorageUnit = StorageUnit(
            code="A-01", unit_type="стеллаж", max_weight=1000.0
        )
        unit.load(500.0)
        assert not unit.is_overloaded()

    def test_equality(self) -> None:
        """Равные по коду."""
        a: StorageUnit = StorageUnit(
            code="A-01", unit_type="X", max_weight=100.0
        )
        b: StorageUnit = StorageUnit(
            code="A-01", unit_type="Y", max_weight=200.0
        )
        assert a == b
        assert a != "not a unit"

    def test_hash(self) -> None:
        """Хеш по коду."""
        a: StorageUnit = StorageUnit(
            code="A-01", unit_type="X", max_weight=100.0
        )
        b: StorageUnit = StorageUnit(
            code="A-01", unit_type="Y", max_weight=200.0
        )
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        unit: StorageUnit = StorageUnit(
            code="A-01", unit_type="стеллаж", max_weight=1000.0
        )
        assert "A-01" in str(unit)

    def test_parse(self) -> None:
        """from_string разбирает единицу."""
        unit: StorageUnit = StorageUnit.from_string(
            "B-05, паллета, 800, 200"
        )
        assert unit.code == "B-05"
        assert unit.current_weight == 200.0
