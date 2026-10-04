"""
Мастер цеха.

Module: factory.domain.personnel.foreman
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from factory.domain.personnel.employee import Employee
from factory.domain.workshops.workshop import Workshop


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Foreman(Employee):
    """Мастер цеха — руководит сменой.

    Attributes:
        _managed_workshop: Управляемый цех.
        _shift_size: Размер смены.
        _team_size: Число подчинённых.
    """

    def __init__(
        self,
        employee: Employee,
        managed_workshop: Workshop,
        shift_size: int,
    ) -> None:
        """Создать мастера.

        Args:
            employee: Базовый сотрудник.
            managed_workshop: Цех.
            shift_size: Размер смены.
        """
        super().__init__(
            name=employee.name,
            position=employee.position,
            salary=employee.salary,
            hire_date=employee._hire_date,
            department=employee.department,
            workshop=employee._workshop,
        )
        self._managed_workshop: Workshop = managed_workshop
        self._shift_size: int = shift_size
        self._team_size: int = 0

    def add_worker(self) -> None:
        """Добавить рабочего в команду.

        Returns:
            Ничего не возвращает.
        """
        self._team_size += 1

    def remove_worker(self) -> None:
        """Убрать рабочего из команды.

        Returns:
            Ничего не возвращает.
        """
        self._team_size = max(0, self._team_size - 1)

    def is_full_team(self) -> bool:
        """Проверить, укомплектована ли команда.

        Returns:
            ``True``, если команда заполнена.
        """
        return self._team_size >= self._shift_size

    def needs_more_workers(self) -> bool:
        """Проверить, нужны ли ещё рабочие.

        Returns:
            ``True``, если команда неполная.
        """
        return self._team_size < self._shift_size
