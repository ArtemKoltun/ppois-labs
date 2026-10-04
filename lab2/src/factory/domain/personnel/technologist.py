"""
Технолог.

Module: factory.domain.personnel.technologist
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from factory.domain.personnel.employee import Employee
from factory.domain.workshops.production_process import (
    ProductionProcess,
)


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Technologist(Employee):
    """Технолог — разрабатывает техпроцессы.

    Attributes:
        _processes: Список разработанных процессов.
        _certification: Уровень сертификации.
    """

    def __init__(
        self,
        employee: Employee,
        certification: str,
    ) -> None:
        """Создать технолога.

        Args:
            employee: Базовый сотрудник.
            certification: Уровень сертификации.
        """
        super().__init__(
            name=employee.name,
            position=employee.position,
            salary=employee.salary,
            hire_date=employee._hire_date,
            department=employee.department,
            workshop=employee._workshop,
        )
        self._processes: list[ProductionProcess] = []
        self._certification: str = certification

    def develop_process(
        self,
        process: ProductionProcess,
    ) -> None:
        """Добавить разработанный процесс.

        Args:
            process: Техпроцесс.

        Returns:
            Ничего не возвращает.
        """
        self._processes.append(process)

    def processes_count(self) -> int:
        """Вернуть число разработанных процессов.

        Returns:
            Целое число.
        """
        return len(self._processes)

    def is_highly_certified(self) -> bool:
        """Проверить высокий уровень сертификации.

        Returns:
            ``True``, если сертификация содержит «высш».
        """
        return "высш" in self._certification.lower()
