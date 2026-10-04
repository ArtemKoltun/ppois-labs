"""
Тесты класса Report.

Module: tests.factory.domain.management.test_report
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from factory.domain.management.report import Report
from factory.domain.management.statistics import Statistics
from factory.domain.personnel.employee import Employee

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_report(
    employee: Employee,
    statistics: Statistics,
) -> Report:
    """Создать отчёт.

    Args:
        employee: Автор.
        statistics: Статистика.

    Returns:
        Объект ``Report``.
    """
    return Report(
        title="Отчёт за январь",
        period="2026-01",
        author=employee,
        statistics=statistics,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestReport:
    """Проверки класса Report."""

    def test_creates(
        self,
        employee: Employee,
        statistics: Statistics,
    ) -> None:
        """Отчёт создаётся.

        Args:
            employee: Фикстура сотрудника.
            statistics: Фикстура статистики.
        """
        report: Report = _make_report(employee, statistics)
        assert report.title == "Отчёт за январь"
        assert report.period == "2026-01"

    def test_empty_title_raises(
        self,
        employee: Employee,
        statistics: Statistics,
    ) -> None:
        """Пустой заголовок недопустим.

        Args:
            employee: Фикстура сотрудника.
            statistics: Фикстура статистики.
        """
        with pytest.raises(ValueError):
            Report(
                title="",
                period="X",
                author=employee,
                statistics=statistics,
            )

    def test_get_statistics(
        self,
        employee: Employee,
        statistics: Statistics,
    ) -> None:
        """get_statistics возвращает статистику.

        Args:
            employee: Фикстура сотрудника.
            statistics: Фикстура статистики.
        """
        report: Report = _make_report(employee, statistics)
        assert report.get_statistics() is statistics

    def test_summary(
        self,
        employee: Employee,
        statistics: Statistics,
    ) -> None:
        """summary возвращает сводку.

        Args:
            employee: Фикстура сотрудника.
            statistics: Фикстура статистики.
        """
        report: Report = _make_report(employee, statistics)
        text: str = report.summary()
        assert "2026-01" in text

    def test_is_positive(
        self,
        employee: Employee,
        statistics: Statistics,
    ) -> None:
        """is_positive без брака.

        Args:
            employee: Фикстура сотрудника.
            statistics: Фикстура статистики.
        """
        report: Report = _make_report(employee, statistics)
        assert report.is_positive()

    def test_equality(
        self,
        employee: Employee,
        statistics: Statistics,
    ) -> None:
        """Равные по заголовку и периоду.

        Args:
            employee: Фикстура сотрудника.
            statistics: Фикстура статистики.
        """
        a: Report = _make_report(employee, statistics)
        b: Report = _make_report(employee, statistics)
        assert a == b
        assert a != "not report"

    def test_hash(
        self,
        employee: Employee,
        statistics: Statistics,
    ) -> None:
        """Хеш отчёта.

        Args:
            employee: Фикстура сотрудника.
            statistics: Фикстура статистики.
        """
        a: Report = _make_report(employee, statistics)
        b: Report = _make_report(employee, statistics)
        assert hash(a) == hash(b)

    def test_str(
        self,
        employee: Employee,
        statistics: Statistics,
    ) -> None:
        """str содержит заголовок.

        Args:
            employee: Фикстура сотрудника.
            statistics: Фикстура статистики.
        """
        report: Report = _make_report(employee, statistics)
        assert "Отчёт за январь" in str(report)
