"""
Рабочая смена.

Module: factory.domain.personnel.work_shift
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from factory.domain.personnel.employee import Employee

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class WorkShift(Readable, Writable):
    """Рабочая смена.

    Attributes:
        _name: Название смены.
        _start_hour: Час начала.
        _end_hour: Час окончания.
        _employees: Список сотрудников.
    """

    def __init__(
        self,
        name: str,
        start_hour: int,
        end_hour: int,
    ) -> None:
        """Создать смену.

        Args:
            name: Название.
            start_hour: Час начала.
            end_hour: Час окончания.

        Raises:
            ValueError: Если часы некорректны.
        """
        if not 0 <= start_hour < 24:
            raise ValueError("час начала вне диапазона")
        if not 0 < end_hour <= 24:
            raise ValueError("час окончания вне диапазона")
        self._name: str = name
        self._start_hour: int = start_hour
        self._end_hour: int = end_hour
        self._employees: list[Employee] = []

    @classmethod
    def _parse(cls, text: str) -> WorkShift:
        """Разобрать смену из строки.

        Args:
            text: Строка с полями через запятую.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(",")]
        return cls(
            name=parts[0],
            start_hour=int(parts[1]),
            end_hour=int(parts[2]),
        )

    @property
    def name(self) -> str:
        """Название смены.

        Returns:
            Строка.
        """
        return self._name

    @property
    def start_hour(self) -> int:
        """Час начала смены.

        Returns:
            Целое число от 0 до 23.
        """
        return self._start_hour

    @property
    def end_hour(self) -> int:
        """Час окончания смены.

        Returns:
            Целое число от 1 до 24.
        """
        return self._end_hour

    def add_employee(self, employee: Employee) -> None:
        """Добавить сотрудника в смену.

        Args:
            employee: Сотрудник.

        Returns:
            Ничего не возвращает.
        """
        self._employees.append(employee)

    def remove_employee(self, employee: Employee) -> None:
        """Убрать сотрудника из смены.

        Args:
            employee: Сотрудник.

        Returns:
            Ничего не возвращает.
        """
        if employee in self._employees:
            self._employees.remove(employee)

    def duration(self) -> int:
        """Вернуть длительность смены.

        Returns:
            Часы.
        """
        return self._end_hour - self._start_hour

    def employee_count(self) -> int:
        """Вернуть число сотрудников.

        Returns:
            Целое число.
        """
        return len(self._employees)

    def is_night_shift(self) -> bool:
        """Проверить, ночная ли смена.

        Returns:
            ``True``, если начало после 20:00 или до 6:00.
        """
        return self._start_hour >= 20 or self._start_hour < 6

    def __eq__(self, other: object) -> bool:
        """Сравнить две смены.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении названий.
        """
        if not isinstance(other, WorkShift):
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
            Строка с полями через запятую.
        """
        return f"{self._name}, {self._start_hour}, {self._end_hour}"
