"""
Тесты класса Material.

Module: tests.factory.domain.materials.test_material
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.enums.material_type import MaterialType
from common.exceptions import InvalidMaterialError
from factory.domain.materials.material import Material

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestMaterial:
    """Проверки класса Material."""

    def test_creates(self, steel: Material) -> None:
        """Материал создаётся.

        Args:
            steel: Фикстура материала.
        """
        assert steel.name == "Сталь 45"
        assert steel.material_type == MaterialType.STEEL.value
        assert steel.density == 7800.0
        assert steel.cost_per_kg == 80.0

    def test_empty_name_raises(self) -> None:
        """Пустое имя недопустимо."""
        with pytest.raises(InvalidMaterialError):
            Material(
                name="",
                material_type="steel",
                density=7800.0,
                cost_per_kg=80.0,
            )

    def test_zero_density_raises(self) -> None:
        """Нулевая плотность недопустима."""
        with pytest.raises(InvalidMaterialError):
            Material(
                name="X",
                material_type="steel",
                density=0.0,
                cost_per_kg=80.0,
            )

    def test_negative_cost_raises(self) -> None:
        """Отрицательная цена недопустима."""
        with pytest.raises(InvalidMaterialError):
            Material(
                name="X",
                material_type="steel",
                density=7800.0,
                cost_per_kg=-1.0,
            )

    def test_calculate_cost(self, steel: Material) -> None:
        """calculate_cost считает по весу.

        Args:
            steel: Фикстура материала.
        """
        assert steel.calculate_cost(2.0) == 160.0

    def test_is_valid(self, steel: Material) -> None:
        """Валидный материал.

        Args:
            steel: Фикстура материала.
        """
        assert steel.is_valid()

    def test_equality(self, steel: Material) -> None:
        """Одинаковые материалы равны.

        Args:
            steel: Фикстура материала.
        """
        other: Material = Material(
            name="Сталь 45",
            material_type="steel",
            density=1.0,
            cost_per_kg=1.0,
        )
        assert steel == other

    def test_inequality(self, steel: Material) -> None:
        """Разные материалы не равны.

        Args:
            steel: Фикстура материала.
        """
        assert steel != "not a material"

    def test_hash(self, steel: Material) -> None:
        """Одинаковые материалы имеют одинаковый хеш.

        Args:
            steel: Фикстура материала.
        """
        other: Material = Material(
            name="Сталь 45",
            material_type="steel",
            density=1.0,
            cost_per_kg=1.0,
        )
        assert hash(steel) == hash(other)

    def test_str(self, steel: Material) -> None:
        """str возвращает поля.

        Args:
            steel: Фикстура материала.
        """
        text: str = str(steel)
        assert "Сталь 45" in text
        assert "steel" in text

    def test_parse(self) -> None:
        """from_string разбирает материал."""
        m: Material = Material.from_string("Медь, copper, 8900, 500")
        assert m.name == "Медь"
        assert m.density == 8900.0
