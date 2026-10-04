"""
Тесты класса Part.

Module: tests.factory.domain.parts.test_part
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.enums.part_type import PartType
from common.exceptions import InvalidPartException
from factory.domain.materials.material import Material
from factory.domain.parts.part import Part
from factory.domain.parts.specification import Specification


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestPart:
    """Проверки класса Part."""

    def test_creates(self, piston_part: Part) -> None:
        """Деталь создаётся с полями.

        Args:
            piston_part: Фикстура детали.
        """
        assert piston_part.name == "Поршень"
        assert piston_part.weight == 1.5

    def test_empty_name_raises(
        self,
        specification: Specification,
        steel: Material,
    ) -> None:
        """Пустое имя недопустимо.

        Args:
            specification: Фикстура спецификации.
            steel: Фикстура материала.
        """
        with pytest.raises(InvalidPartException):
            Part(
                name="",
                part_type=PartType.PISTON,
                weight=1.0,
                specification=specification,
                material=steel,
            )

    def test_zero_weight_raises(
        self,
        specification: Specification,
        steel: Material,
    ) -> None:
        """Нулевой вес недопустим.

        Args:
            specification: Фикстура спецификации.
            steel: Фикстура материала.
        """
        with pytest.raises(InvalidPartException):
            Part(
                name="X",
                part_type=PartType.PISTON,
                weight=0.0,
                specification=specification,
                material=steel,
            )

    def test_negative_weight_raises(
        self,
        specification: Specification,
        steel: Material,
    ) -> None:
        """Отрицательный вес недопустим.

        Args:
            specification: Фикстура спецификации.
            steel: Фикстура материала.
        """
        with pytest.raises(InvalidPartException):
            Part(
                name="X",
                part_type=PartType.PISTON,
                weight=-1.0,
                specification=specification,
                material=steel,
            )

    def test_calculate_cost(self, piston_part: Part) -> None:
        """calculate_cost считает по весу и цене материала.

        Args:
            piston_part: Фикстура детали.
        """
        assert piston_part.calculate_cost() == 120.0

    def test_get_full_name(self, piston_part: Part) -> None:
        """get_full_name возвращает имя с типом.

        Args:
            piston_part: Фикстура детали.
        """
        text: str = piston_part.get_full_name()
        assert "Поршень" in text
        assert "поршень" in text

    def test_is_valid(self, piston_part: Part) -> None:
        """Валидная деталь проходит проверку.

        Args:
            piston_part: Фикстура детали.
        """
        assert piston_part.is_valid()

    def test_equality(self, piston_part: Part) -> None:
        """Одинаковые детали равны.

        Args:
            piston_part: Фикстура детали.
        """
        other: Part = Part(
            name="Поршень",
            part_type=PartType.PISTON,
            weight=1.5,
            specification=piston_part._specification,
            material=piston_part._material,
        )
        assert piston_part == other

    def test_inequality(self, piston_part: Part) -> None:
        """Разные детали не равны.

        Args:
            piston_part: Фикстура детали.
        """
        other: Part = Part(
            name="Цилиндр",
            part_type=PartType.CYLINDER,
            weight=2.0,
            specification=piston_part._specification,
            material=piston_part._material,
        )
        assert piston_part != other
        assert piston_part != "not a part"

    def test_hash(self, piston_part: Part) -> None:
        """Одинаковые детали имеют одинаковый хеш.

        Args:
            piston_part: Фикстура детали.
        """
        other: Part = Part(
            name="Поршень",
            part_type=PartType.PISTON,
            weight=1.5,
            specification=piston_part._specification,
            material=piston_part._material,
        )
        assert hash(piston_part) == hash(other)

    def test_str(self, piston_part: Part) -> None:
        """str возвращает все поля.

        Args:
            piston_part: Фикстура детали.
        """
        text: str = str(piston_part)
        assert "Поршень" in text
        assert "piston" in text

    def test_parse(self, specification: Specification) -> None:
        """from_string разбирает деталь."""
        line: str = (
            "Поршень, piston, 1.5, spec, Сталь 45, steel, "
            "7800, 80, 0.05, Ra 1.6"
        )
        part: Part = Part.from_string(line)
        assert part.name == "Поршень"
        assert part.weight == 1.5
