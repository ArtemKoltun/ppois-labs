"""
Токарь.

Module: factory.domain.personnel.turner
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from factory.domain.equipment.lathe import Lathe
from factory.domain.personnel.employee import Employee

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Turner(Employee):
    """Токарь — работает на токарном станке.

    Attributes:
        _grade: Разряд (1-6).
        _assigned_lathe: Закреплённый станок.
    """

    def __init__(
        self,
        employee: Employee,
        grade: int,
        assigned_lathe: Lathe | None = None,
    ) -> None:
        """Создать токаря.

        Args:
            employee: Базовый сотрудник.
            grade: Разряд.
            assigned_lathe: Закреплённый станок.
        """
        super().__init__(
            name=employee.name,
            position=employee.position,
            salary=employee.salary,
            hire_date=employee._hire_date,
            department=employee.department,
            workshop=employee._workshop,
        )
        self._grade: int = grade
        self._assigned_lathe: Lathe | None = assigned_lathe

    def assign_lathe(self, lathe: Lathe) -> None:
        """Закрепить станок.

        Args:
            lathe: Токарный станок.

        Returns:
            Ничего не возвращает.
        """
        self._assigned_lathe = lathe

    def has_lathe(self) -> bool:
        """Проверить, закреплён ли станок.

        Returns:
            ``True``, если станок есть.
        """
        return self._assigned_lathe is not None

    def is_high_grade(self) -> bool:
        """Проверить высокий разряд.

        Returns:
            ``True``, если разряд не ниже 5.
        """
        return self._grade >= 5
