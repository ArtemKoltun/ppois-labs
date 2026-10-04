"""
Тесты класса Foreman.

Module: tests.factory.domain.personnel.test_foreman
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.personnel.employee import Employee
from factory.domain.personnel.foreman import Foreman
from factory.domain.workshops.workshop import Workshop

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_foreman(
    employee: Employee,
    workshop: Workshop,
    shift: int = 10,
) -> Foreman:
    """Создать мастера.

    Args:
        employee: Сотрудник.
        workshop: Цех.
        shift: Размер смены.

    Returns:
        Объект ``Foreman``.
    """
    return Foreman(
        employee=employee,
        managed_workshop=workshop,
        shift_size=shift,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestForeman:
    """Проверки класса Foreman."""

    def test_creates(
        self,
        employee: Employee,
        workshop: Workshop,
    ) -> None:
        """Мастер создаётся.

        Args:
            employee: Фикстура сотрудника.
            workshop: Фикстура цеха.
        """
        foreman: Foreman = _make_foreman(employee, workshop)
        assert foreman.name == "Иванов И.И."

    def test_add_remove_worker(
        self,
        employee: Employee,
        workshop: Workshop,
    ) -> None:
        """Рабочие добавляются и убираются.

        Args:
            employee: Фикстура сотрудника.
            workshop: Фикстура цеха.
        """
        foreman: Foreman = _make_foreman(employee, workshop)
        foreman.add_worker()
        foreman.add_worker()
        foreman.remove_worker()
        assert not foreman.is_full_team()

    def test_is_full_team(
        self,
        employee: Employee,
        workshop: Workshop,
    ) -> None:
        """is_full_team проверяет заполненность.

        Args:
            employee: Фикстура сотрудника.
            workshop: Фикстура цеха.
        """
        foreman: Foreman = _make_foreman(employee, workshop, shift=3)
        for _ in range(3):
            foreman.add_worker()
        assert foreman.is_full_team()
        assert not foreman.needs_more_workers()

    def test_needs_more_workers(
        self,
        employee: Employee,
        workshop: Workshop,
    ) -> None:
        """needs_more_workers для неполной смены.

        Args:
            employee: Фикстура сотрудника.
            workshop: Фикстура цеха.
        """
        foreman: Foreman = _make_foreman(employee, workshop, shift=5)
        foreman.add_worker()
        assert foreman.needs_more_workers()
