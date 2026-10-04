"""
Тесты класса WorkShift.

Module: tests.factory.domain.personnel.test_work_shift
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from factory.domain.personnel.employee import Employee
from factory.domain.personnel.work_shift import WorkShift


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestWorkShift:
    """Проверки класса WorkShift."""

    def test_creates(self) -> None:
        """Смена создаётся."""
        shift: WorkShift = WorkShift(
            name="Дневная", start_hour=8, end_hour=16
        )
        assert shift.name == "Дневная"
        assert shift.employee_count() == 0

    def test_bad_start_hour_raises(self) -> None:
        """Некорректный час начала."""
        with pytest.raises(ValueError):
            WorkShift(name="X", start_hour=25, end_hour=16)

    def test_bad_end_hour_raises(self) -> None:
        """Некорректный час окончания."""
        with pytest.raises(ValueError):
            WorkShift(name="X", start_hour=8, end_hour=30)

    def test_add_remove_employee(self, employee: Employee) -> None:
        """Сотрудники добавляются и убираются.

        Args:
            employee: Фикстура сотрудника.
        """
        shift: WorkShift = WorkShift(
            name="Дневная", start_hour=8, end_hour=16
        )
        shift.add_employee(employee)
        assert shift.employee_count() == 1
        shift.remove_employee(employee)
        assert shift.employee_count() == 0

    def test_remove_nonexistent(self, employee: Employee) -> None:
        """Удаление отсутствующего не падает.

        Args:
            employee: Фикстура сотрудника.
        """
        shift: WorkShift = WorkShift(
            name="Дневная", start_hour=8, end_hour=16
        )
        shift.remove_employee(employee)  # не должно бросить

    def test_duration(self) -> None:
        """duration считает часы."""
        shift: WorkShift = WorkShift(
            name="Дневная", start_hour=8, end_hour=16
        )
        assert shift.duration() == 8

    def test_is_night_shift(self) -> None:
        """is_night_shift определяет ночную."""
        night: WorkShift = WorkShift(
            name="Ночная", start_hour=22, end_hour=6
        )
        day: WorkShift = WorkShift(
            name="Дневная", start_hour=9, end_hour=18
        )
        assert night.is_night_shift()
        assert not day.is_night_shift()

    def test_equality(self) -> None:
        """Равные смены по имени."""
        a: WorkShift = WorkShift(
            name="Дневная", start_hour=8, end_hour=16
        )
        b: WorkShift = WorkShift(
            name="Дневная", start_hour=9, end_hour=17
        )
        assert a == b
        assert a != "not a shift"

    def test_hash(self) -> None:
        """Хеш по имени."""
        a: WorkShift = WorkShift(
            name="Дневная", start_hour=8, end_hour=16
        )
        b: WorkShift = WorkShift(
            name="Дневная", start_hour=9, end_hour=17
        )
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        shift: WorkShift = WorkShift(
            name="Дневная", start_hour=8, end_hour=16
        )
        text: str = str(shift)
        assert "Дневная" in text

    def test_parse(self) -> None:
        """from_string разбирает смену."""
        shift: WorkShift = WorkShift.from_string("Ночная, 22, 6")
        assert shift.name == "Ночная"
        assert shift.start_hour == 22
        assert shift.end_hour == 6
