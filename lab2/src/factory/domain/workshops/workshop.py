"""
Цех завода.

Module: factory.domain.workshops.workshop
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

class Workshop(Readable, Writable):
    """Производственный цех.

    Attributes:
        _name: Наименование.
        _number: Номер цеха.
        _area: Площадь в м².
        _workshop_head: Имя начальника цеха.
        _employee_count: Число сотрудников.
    """

    def __init__(
        self,
        name: str,
        number: int,
        area: float,
        workshop_head: str = "",
    ) -> None:
        """Создать цех.

        Args:
            name: Наименование.
            number: Номер.
            area: Площадь.
            workshop_head: Начальник цеха.

        Raises:
            ValueError: Если данные некорректны.
        """
        if not name:
            raise ValueError("имя цеха не может быть пустым")
        if number <= 0:
            raise ValueError("номер должен быть положительным")
        if area <= 0:
            raise ValueError("площадь должна быть положительной")
        self._name: str = name
        self._number: int = number
        self._area: float = area
        self._workshop_head: str = workshop_head
        self._employee_count: int = 0

    @classmethod
    def _parse(cls, text: str) -> Workshop:
        """Разобрать цех из строки.

        Args:
            text: Строка с полями через запятую.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(",")]
        return cls(
            name=parts[0],
            number=int(parts[1]),
            area=float(parts[2]),
            workshop_head=parts[3],
        )

    @property
    def name(self) -> str:
        """Наименование.

        Returns:
            Строка.
        """
        return self._name

    @property
    def number(self) -> int:
        """Номер цеха.

        Returns:
            Целое число.
        """
        return self._number

    def hire(self, count: int = 1) -> None:
        """Нанять сотрудников в цех.

        Args:
            count: Число новых сотрудников.

        Returns:
            Ничего не возвращает.
        """
        self._employee_count += count

    def fire(self, count: int = 1) -> None:
        """Уволить сотрудников.

        Args:
            count: Число уволенных.

        Returns:
            Ничего не возвращает.
        """
        self._employee_count = max(0, self._employee_count - count)

    def assign_head(self, name: str) -> None:
        """Назначить начальника цеха.

        Args:
            name: Имя начальника.

        Returns:
            Ничего не возвращает.
        """
        self._workshop_head = name

    def has_head(self) -> bool:
        """Проверить, назначен ли начальник.

        Returns:
            ``True``, если начальник задан.
        """
        return bool(self._workshop_head)

    def area_per_employee(self) -> float:
        """Рассчитать площадь на одного сотрудника.

        Returns:
            Площадь в м² или 0, если сотрудников нет.
        """
        if self._employee_count == 0:
            return 0.0
        return self._area / self._employee_count

    def __eq__(self, other: object) -> bool:
        """Сравнить два цеха.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении номеров.
        """
        if not isinstance(other, Workshop):
            return NotImplemented
        return self._number == other._number

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._number)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через запятую.
        """
        return (
            f"{self._name}, {self._number}, {self._area}, "
            f"{self._workshop_head}"
        )
