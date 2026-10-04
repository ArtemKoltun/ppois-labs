"""
Инженер.

Module: factory.domain.personnel.engineer
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from factory.domain.personnel.employee import Employee

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Engineer(Employee):
    """Инженер-конструктор.

    Attributes:
        _specialization: Специализация.
        _category: Категория (1, 2, 3).
        _projects_count: Число проектов.
    """

    def __init__(
        self,
        employee: Employee,
        specialization: str,
        category: int,
    ) -> None:
        """Создать инженера.

        Args:
            employee: Базовый сотрудник.
            specialization: Специализация.
            category: Категория.
        """
        super().__init__(
            name=employee.name,
            position=employee.position,
            salary=employee.salary,
            hire_date=employee._hire_date,
            department=employee.department,
            workshop=employee._workshop,
        )
        self._specialization: str = specialization
        self._category: int = category
        self._projects_count: int = 0

    def assign_project(self) -> None:
        """Назначить проект.

        Returns:
            Ничего не возвращает.
        """
        self._projects_count += 1

    def is_senior(self) -> bool:
        """Проверить, старший ли инженер.

        Returns:
            ``True``, если категория не ниже первой.
        """
        return self._category <= 1

    def is_overloaded(self) -> bool:
        """Проверить перегрузку.

        Returns:
            ``True``, если проектов больше пяти.
        """
        return self._projects_count > 5
