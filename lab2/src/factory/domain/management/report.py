"""
Отчёт о работе завода.

Module: factory.domain.management.report
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from factory.domain.management.statistics import Statistics
from factory.domain.personnel.employee import Employee


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Report(Readable, Writable):
    """Отчёт о работе завода за период.

    Attributes:
        _title: Заголовок.
        _period: Период.
        _author: Автор отчёта.
        _statistics: Статистика.
    """

    def __init__(
        self,
        title: str,
        period: str,
        author: Employee,
        statistics: Statistics,
    ) -> None:
        """Создать отчёт.

        Args:
            title: Заголовок.
            period: Период.
            author: Автор.
            statistics: Статистика.

        Raises:
            ValueError: Если заголовок пустой.
        """
        if not title:
            raise ValueError("заголовок не может быть пустым")
        self._title: str = title
        self._period: str = period
        self._author: Employee = author
        self._statistics: Statistics = statistics

    @classmethod
    def _parse(cls, text: str) -> "Report":
        """Разобрать отчёт из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        author: Employee = Employee.from_string(parts[2])
        statistics: Statistics = Statistics.from_string(parts[3])
        return cls(
            title=parts[0],
            period=parts[1],
            author=author,
            statistics=statistics,
        )

    @property
    def title(self) -> str:
        """Заголовок.

        Returns:
            Строка.
        """
        return self._title

    @property
    def period(self) -> str:
        """Период.

        Returns:
            Строка.
        """
        return self._period

    def get_statistics(self) -> Statistics:
        """Вернуть статистику отчёта.

        Returns:
            Объект статистики.
        """
        return self._statistics

    def summary(self) -> str:
        """Вернуть краткую сводку отчёта.

        Returns:
            Строка.
        """
        return (
            f"{self._title} за {self._period}: "
            f"заказов {self._statistics.total_orders()}, "
            f"производство {self._statistics.total_produced_quantity()}, "
            f"брак {self._statistics.defect_rate():.1%}"
        )

    def is_positive(self) -> bool:
        """Проверить позитивность отчёта.

        Returns:
            ``True``, если доля брака ниже 2%.
        """
        return self._statistics.defect_rate() < 0.02

    def __eq__(self, other: object) -> bool:
        """Сравнить два отчёта.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении заголовка и периода.
        """
        if not isinstance(other, Report):
            return NotImplemented
        return (
            self._title == other._title
            and self._period == other._period
        )

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash((self._title, self._period))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._title}; {self._period}; "
            f"{self._author}; {self._statistics}"
        )
