"""
Отдел завода.

Module: factory.domain.management.department
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Department(Readable, Writable):
    """Административный отдел завода.

    Attributes:
        _name: Наименование отдела.
        _head_name: Имя руководителя.
        _employee_count: Число сотрудников.
    """

    def __init__(
        self,
        name: str,
        head_name: str = "",
    ) -> None:
        """Создать отдел.

        Args:
            name: Наименование.
            head_name: Имя руководителя.

        Raises:
            ValueError: Если имя пустое.
        """
        if not name:
            raise ValueError("имя отдела не может быть пустым")
        self._name: str = name
        self._head_name: str = head_name
        self._employee_count: int = 0

    @classmethod
    def _parse(cls, text: str) -> "Department":
        """Разобрать отдел из строки.

        Args:
            text: Строка с полями через запятую.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(",")]
        return cls(name=parts[0], head_name=parts[1])

    @property
    def name(self) -> str:
        """Наименование отдела.

        Returns:
            Строка.
        """
        return self._name

    def add_employee(self) -> None:
        """Увеличить счётчик сотрудников.

        Returns:
            Ничего не возвращает.
        """
        self._employee_count += 1

    def remove_employee(self) -> None:
        """Уменьшить счётчик сотрудников.

        Returns:
            Ничего не возвращает.
        """
        self._employee_count = max(0, self._employee_count - 1)

    def has_head(self) -> bool:
        """Проверить, есть ли руководитель.

        Returns:
            ``True``, если имя задано.
        """
        return bool(self._head_name)

    def __eq__(self, other: object) -> bool:
        """Сравнить два отдела.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении наименований.
        """
        if not isinstance(other, Department):
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
        return f"{self._name}, {self._head_name}"
