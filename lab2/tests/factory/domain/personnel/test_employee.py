"""
Тесты класса Employee.

Module: tests.factory.domain.personnel.test_employee
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.domain.money import Money
from common.exceptions import EmployeeNotAvailableError
from factory.domain.management.department import Department
from factory.domain.personnel.employee import Employee
from factory.domain.workshops.workshop import Workshop

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestEmployee:
    """Проверки класса Employee."""

    def test_creates(self, employee: Employee) -> None:
        """Сотрудник создаётся.

        Args:
            employee: Фикстура сотрудника.
        """
        assert employee.name == "Иванов И.И."
        assert employee.position == "Инженер"
        assert employee.salary.amount == 80000.0

    def test_empty_name_raises(self, department: Department) -> None:
        """Пустое имя недопустимо.

        Args:
            department: Фикстура отдела.
        """
        with pytest.raises(ValueError):
            Employee(
                name="",
                position="X",
                salary=Money(amount=1.0),
                hire_date="2026-01-01",
                department=department,
            )

    def test_empty_position_raises(
        self,
        department: Department,
    ) -> None:
        """Пустая должность недопустима.

        Args:
            department: Фикстура отдела.
        """
        with pytest.raises(ValueError):
            Employee(
                name="X",
                position="",
                salary=Money(amount=1.0),
                hire_date="2026-01-01",
                department=department,
            )

    def test_raise_salary(self, employee: Employee) -> None:
        """raise_salary увеличивает оклад.

        Args:
            employee: Фикстура сотрудника.
        """
        employee.raise_salary(Money(amount=10000.0))
        assert employee.salary.amount == 90000.0

    def test_go_on_vacation(self, employee: Employee) -> None:
        """go_on_vacation делает недоступным.

        Args:
            employee: Фикстура сотрудника.
        """
        employee.go_on_vacation()
        with pytest.raises(EmployeeNotAvailableError):
            employee.ensure_available()

    def test_return_from_vacation(self, employee: Employee) -> None:
        """return_from_vacation делает доступным.

        Args:
            employee: Фикстура сотрудника.
        """
        employee.go_on_vacation()
        employee.return_from_vacation()
        employee.ensure_available()  # не должно бросить

    def test_transfer_to(
        self,
        employee: Employee,
        workshop: Workshop,
    ) -> None:
        """transfer_to меняет цех.

        Args:
            employee: Фикстура сотрудника.
            workshop: Фикстура цеха.
        """
        other: Workshop = Workshop(name="Другой", number=2, area=100.0)
        employee.transfer_to(other)
        # Проверяем через приватное поле
        assert employee._workshop == other

    def test_equality(self, employee: Employee) -> None:
        """Равные по имени.

        Args:
            employee: Фикстура сотрудника.
        """
        other: Employee = Employee(
            name="Иванов И.И.",
            position="Другой",
            salary=Money(amount=1.0),
            hire_date="X",
            department=employee.department,
        )
        assert employee == other

    def test_inequality(self, employee: Employee) -> None:
        """Разные сотрудники.

        Args:
            employee: Фикстура сотрудника.
        """
        assert employee != "not employee"

    def test_hash(self, employee: Employee) -> None:
        """Хеш по имени.

        Args:
            employee: Фикстура сотрудника.
        """
        other: Employee = Employee(
            name="Иванов И.И.",
            position="X",
            salary=Money(amount=1.0),
            hire_date="X",
            department=employee.department,
        )
        assert hash(employee) == hash(other)

    def test_str(self, employee: Employee) -> None:
        """str возвращает поля.

        Args:
            employee: Фикстура сотрудника.
        """
        text: str = str(employee)
        assert "Иванов И.И." in text
