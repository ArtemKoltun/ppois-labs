"""
Сотрудник завода.

Module: factory.domain.personnel.employee
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.domain.money import Money
from common.exceptions.employee_exceptions import (
    EmployeeNotAvailableError,
)
from factory.domain.management.department import Department
from factory.domain.workshops.workshop import Workshop

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Employee(Readable, Writable):
    """Сотрудник завода.

    Attributes:
        _name: ФИО.
        _position: Должность.
        _salary: Оклад.
        _hire_date: Дата найма.
        _department: Отдел.
        _workshop: Цех.
        _is_available: Доступен ли сотрудник.
    """

    def __init__(
        self,
        name: str,
        position: str,
        salary: Money,
        hire_date: str,
        department: Department,
        workshop: Workshop | None = None,
    ) -> None:
        """Создать сотрудника.

        Args:
            name: ФИО.
            position: Должность.
            salary: Оклад.
            hire_date: Дата найма.
            department: Отдел.
            workshop: Цех.

        Raises:
            ValueError: Если имя или должность пустые.
        """
        if not name or not position:
            raise ValueError("имя и должность не могут быть пустыми")
        self._name: str = name
        self._position: str = position
        self._salary: Money = salary
        self._hire_date: str = hire_date
        self._department: Department = department
        self._workshop: Workshop | None = workshop
        self._is_available: bool = True

    @classmethod
    def _parse(cls, text: str) -> Employee:
        """Разобрать сотрудника из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        department: Department = Department.from_string(parts[4])
        salary: Money = Money(amount=float(parts[2]))
        return cls(
            name=parts[0],
            position=parts[1],
            salary=salary,
            hire_date=parts[3],
            department=department,
        )

    @property
    def name(self) -> str:
        """ФИО.

        Returns:
            Строка.
        """
        return self._name

    @property
    def position(self) -> str:
        """Должность.

        Returns:
            Строка.
        """
        return self._position

    @property
    def salary(self) -> Money:
        """Оклад.

        Returns:
            Денежная сумма.
        """
        return self._salary

    @property
    def department(self) -> Department:
        """Отдел.

        Returns:
            Объект отдела.
        """
        return self._department

    def raise_salary(self, amount: Money) -> None:
        """Повысить оклад.

        Args:
            amount: Сумма повышения.

        Returns:
            Ничего не возвращает.
        """
        self._salary = self._salary.add(amount)

    def go_on_vacation(self) -> None:
        """Отправить сотрудника в отпуск.

        Returns:
            Ничего не возвращает.
        """
        self._is_available = False

    def return_from_vacation(self) -> None:
        """Вернуть сотрудника из отпуска.

        Returns:
            Ничего не возвращает.
        """
        self._is_available = True

    def ensure_available(self) -> None:
        """Проверить доступность сотрудника.

        Returns:
            Ничего не возвращает.

        Raises:
            EmployeeNotAvailableError: Если сотрудник недоступен.
        """
        if not self._is_available:
            raise EmployeeNotAvailableError(
                f"сотрудник {self._name} недоступен"
            )

    def transfer_to(self, workshop: Workshop) -> None:
        """Перевести сотрудника в другой цех.

        Args:
            workshop: Новый цех.

        Returns:
            Ничего не возвращает.
        """
        self._workshop = workshop

    def __eq__(self, other: object) -> bool:
        """Сравнить двух сотрудников.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении имён.
        """
        if not isinstance(other, Employee):
            return NotImplemented
        return self._name == other._name

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._name)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._name}; {self._position}; {self._salary.amount}; "
            f"{self._hire_date}; {self._department}"
        )
