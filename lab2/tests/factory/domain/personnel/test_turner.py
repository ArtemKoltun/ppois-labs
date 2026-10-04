"""
Тесты класса Turner.

Module: tests.factory.domain.personnel.test_turner
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.equipment.lathe import Lathe
from factory.domain.equipment.machine import Machine
from factory.domain.personnel.employee import Employee
from factory.domain.personnel.turner import Turner

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestTurner:
    """Проверки класса Turner."""

    def test_creates(self, employee: Employee) -> None:
        """Токарь создаётся.

        Args:
            employee: Фикстура сотрудника.
        """
        turner: Turner = Turner(employee=employee, grade=5)
        assert turner.name == "Иванов И.И."
        assert not turner.has_lathe()

    def test_assign_lathe(
        self,
        employee: Employee,
        machine: Machine,
    ) -> None:
        """assign_lathe закрепляет станок.

        Args:
            employee: Фикстура сотрудника.
            machine: Фикстура станка.
        """
        turner: Turner = Turner(employee=employee, grade=5)
        lathe: Lathe = Lathe(
            machine=machine, max_diameter=400.0, max_length=1000.0
        )
        turner.assign_lathe(lathe)
        assert turner.has_lathe()

    def test_is_high_grade(self, employee: Employee) -> None:
        """is_high_grade проверяет разряд.

        Args:
            employee: Фикстура сотрудника.
        """
        high: Turner = Turner(employee=employee, grade=6)
        low: Turner = Turner(employee=employee, grade=3)
        assert high.is_high_grade()
        assert not low.is_high_grade()
