"""
Тесты класса Department.

Module: tests.factory.domain.management.test_department
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from factory.domain.management.department import Department

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestDepartment:
    """Проверки класса Department."""

    def test_creates(self, department: Department) -> None:
        """Отдел создаётся.

        Args:
            department: Фикстура отдела.
        """
        assert department.name == "Инженерный отдел"

    def test_empty_name_raises(self) -> None:
        """Пустое имя недопустимо."""
        with pytest.raises(ValueError):
            Department(name="")

    def test_add_employee(self, department: Department) -> None:
        """add_employee увеличивает счётчик.

        Args:
            department: Фикстура отдела.
        """
        department.add_employee()
        assert department._employee_count == 1

    def test_remove_employee(self, department: Department) -> None:
        """remove_employee уменьшает.

        Args:
            department: Фикстура отдела.
        """
        department.add_employee()
        department.add_employee()
        department.remove_employee()
        assert department._employee_count == 1

    def test_remove_below_zero(self, department: Department) -> None:
        """Не уходит в минус.

        Args:
            department: Фикстура отдела.
        """
        department.remove_employee()
        assert department._employee_count == 0

    def test_has_head(self) -> None:
        """has_head проверяет руководителя."""
        without: Department = Department(name="X")
        with_head: Department = Department(name="Y", head_name="Иванов")
        assert not without.has_head()
        assert with_head.has_head()

    def test_equality(self, department: Department) -> None:
        """Равные по имени.

        Args:
            department: Фикстура отдела.
        """
        other: Department = Department(name="Инженерный отдел")
        assert department == other
        assert department != "not department"

    def test_hash(self, department: Department) -> None:
        """Хеш по имени.

        Args:
            department: Фикстура отдела.
        """
        other: Department = Department(name="Инженерный отдел")
        assert hash(department) == hash(other)

    def test_str(self, department: Department) -> None:
        """str возвращает имя.

        Args:
            department: Фикстура отдела.
        """
        assert "Инженерный отдел" in str(department)

    def test_parse(self) -> None:
        """from_string разбирает отдел."""
        d: Department = Department.from_string("Отдел, Иванов")
        assert d.name == "Отдел"
        assert d._head_name == "Иванов"
