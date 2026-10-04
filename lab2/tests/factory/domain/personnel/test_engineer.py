"""
Тесты класса Engineer.

Module: tests.factory.domain.personnel.test_engineer
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.personnel.employee import Employee
from factory.domain.personnel.engineer import Engineer


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_engineer(base: Employee, category: int = 1) -> Engineer:
    """Создать инженера.

    Args:
        base: Базовый сотрудник.
        category: Категория.

    Returns:
        Объект ``Engineer``.
    """
    return Engineer(
        employee=base,
        specialization="Механика",
        category=category,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestEngineer:
    """Проверки класса Engineer."""

    def test_creates(self, employee: Employee) -> None:
        """Инженер создаётся.

        Args:
            employee: Фикстура сотрудника.
        """
        eng: Engineer = _make_engineer(employee)
        assert eng.name == "Иванов И.И."

    def test_assign_project(self, employee: Employee) -> None:
        """assign_project увеличивает счётчик.

        Args:
            employee: Фикстура сотрудника.
        """
        eng: Engineer = _make_engineer(employee)
        eng.assign_project()
        assert not eng.is_overloaded()

    def test_is_senior(self, employee: Employee) -> None:
        """is_senior проверяет категорию.

        Args:
            employee: Фикстура сотрудника.
        """
        senior: Engineer = _make_engineer(employee, category=1)
        junior: Engineer = _make_engineer(employee, category=3)
        assert senior.is_senior()
        assert not junior.is_senior()

    def test_is_overloaded(self, employee: Employee) -> None:
        """is_overloaded проверяет число проектов.

        Args:
            employee: Фикстура сотрудника.
        """
        eng: Engineer = _make_engineer(employee)
        for _ in range(6):
            eng.assign_project()
        assert eng.is_overloaded()
