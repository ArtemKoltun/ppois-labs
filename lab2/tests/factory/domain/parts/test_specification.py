"""
Тесты класса Specification.

Module: tests.factory.domain.parts.test_specification
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.exceptions import InvalidSpecificationException
from factory.domain.parts.specification import Specification


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestSpecification:
    """Проверки класса Specification."""

    def test_creates(self, specification: Specification) -> None:
        """Спецификация создаётся с полями.

        Args:
            specification: Фикстура спецификации.
        """
        assert specification.part_name == "Поршень"
        assert specification.tolerance == 0.05
        assert specification.surface_finish == "Ra 1.6"

    def test_empty_name_raises(self) -> None:
        """Пустое имя недопустимо."""
        with pytest.raises(InvalidSpecificationException):
            Specification(part_name="")

    def test_zero_tolerance_raises(self) -> None:
        """Нулевой допуск недопустим."""
        with pytest.raises(InvalidSpecificationException):
            Specification(part_name="X", tolerance=0.0)

    def test_is_strict(self) -> None:
        """is_strict проверяет допуск."""
        assert Specification(part_name="X", tolerance=0.01).is_strict()
        assert not Specification(part_name="X", tolerance=0.5).is_strict()

    def test_update_notes(self) -> None:
        """update_notes меняет примечания."""
        spec: Specification = Specification(part_name="X")
        spec.update_notes("новое примечание")
        assert spec.is_valid()

    def test_is_valid(self, specification: Specification) -> None:
        """Валидная спецификация проходит проверку.

        Args:
            specification: Фикстура спецификации.
        """
        assert specification.is_valid()

    def test_equality(self, specification: Specification) -> None:
        """Одинаковые спецификации равны.

        Args:
            specification: Фикстура спецификации.
        """
        other: Specification = Specification(
            part_name="Поршень", tolerance=0.05
        )
        assert specification == other

    def test_inequality(self, specification: Specification) -> None:
        """Разные спецификации не равны.

        Args:
            specification: Фикстура спецификации.
        """
        other: Specification = Specification(
            part_name="Поршень", tolerance=0.5
        )
        assert specification != other
        assert specification != "not a spec"

    def test_hash(self, specification: Specification) -> None:
        """Одинаковые спецификации имеют одинаковый хеш.

        Args:
            specification: Фикстура спецификации.
        """
        other: Specification = Specification(
            part_name="Поршень", tolerance=0.05
        )
        assert hash(specification) == hash(other)

    def test_str(self, specification: Specification) -> None:
        """str возвращает все поля.

        Args:
            specification: Фикстура спецификации.
        """
        text: str = str(specification)
        assert "Поршень" in text
        assert "0.05" in text

    def test_parse(self) -> None:
        """from_string разбирает спецификацию."""
        spec: Specification = Specification.from_string(
            "Вал, 0.1, Ra 3.2, steel, примечание"
        )
        assert spec.part_name == "Вал"
        assert spec.tolerance == 0.1
        assert spec.surface_finish == "Ra 3.2"

    def test_parse_no_notes(self) -> None:
        """from_string без примечаний."""
        spec: Specification = Specification.from_string(
            "Вал, 0.1, Ra 3.2, steel"
        )
        assert spec.part_name == "Вал"
