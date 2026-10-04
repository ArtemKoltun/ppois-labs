"""
Тесты класса Workshop.

Module: tests.factory.domain.workshops.test_workshop
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from factory.domain.workshops.workshop import Workshop


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestWorkshop:
    """Проверки класса Workshop."""

    def test_creates(self, workshop: Workshop) -> None:
        """Цех создаётся.

        Args:
            workshop: Фикстура цеха.
        """
        assert workshop.name == "Механический"
        assert workshop.number == 1

    def test_empty_name_raises(self) -> None:
        """Пустое имя недопустимо."""
        with pytest.raises(ValueError):
            Workshop(name="", number=1, area=100.0)

    def test_zero_number_raises(self) -> None:
        """Нулевой номер недопустим."""
        with pytest.raises(ValueError):
            Workshop(name="X", number=0, area=100.0)

    def test_zero_area_raises(self) -> None:
        """Нулевая площадь недопустима."""
        with pytest.raises(ValueError):
            Workshop(name="X", number=1, area=0.0)

    def test_hire_fire(self, workshop: Workshop) -> None:
        """Найм и увольнение меняют счётчик.

        Args:
            workshop: Фикстура цеха.
        """
        workshop.hire(5)
        workshop.fire(2)
        assert workshop._employee_count == 3

    def test_fire_below_zero(self, workshop: Workshop) -> None:
        """Увольнение не уходит в минус.

        Args:
            workshop: Фикстура цеха.
        """
        workshop.fire(5)
        assert workshop._employee_count == 0

    def test_assign_head(self, workshop: Workshop) -> None:
        """assign_head меняет начальника.

        Args:
            workshop: Фикстура цеха.
        """
        workshop.assign_head("Новый")
        assert workshop.has_head()

    def test_area_per_employee(self, workshop: Workshop) -> None:
        """area_per_employee считает площадь.

        Args:
            workshop: Фикстура цеха.
        """
        assert workshop.area_per_employee() == 0.0
        workshop.hire(5)
        assert workshop.area_per_employee() == 100.0

    def test_equality(self, workshop: Workshop) -> None:
        """Равные цеха по номеру.

        Args:
            workshop: Фикстура цеха.
        """
        other: Workshop = Workshop(name="Другой", number=1, area=100.0)
        assert workshop == other
        assert workshop != "not a workshop"

    def test_hash(self, workshop: Workshop) -> None:
        """Хеш по номеру.

        Args:
            workshop: Фикстура цеха.
        """
        other: Workshop = Workshop(name="X", number=1, area=1.0)
        assert hash(workshop) == hash(other)

    def test_str(self, workshop: Workshop) -> None:
        """str возвращает поля.

        Args:
            workshop: Фикстура цеха.
        """
        text: str = str(workshop)
        assert "Механический" in text

    def test_parse(self) -> None:
        """from_string разбирает цех."""
        w: Workshop = Workshop.from_string(
            "Литейный, 2, 800, Петров"
        )
        assert w.name == "Литейный"
        assert w.number == 2
