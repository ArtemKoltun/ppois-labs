"""
Тесты класса Technologist.

Module: tests.factory.domain.personnel.test_technologist
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.parts.part import Part
from factory.domain.personnel.employee import Employee
from factory.domain.personnel.technologist import Technologist
from factory.domain.workshops.production_process import (
    ProductionProcess,
)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestTechnologist:
    """Проверки класса Technologist."""

    def test_creates(self, employee: Employee) -> None:
        """Технолог создаётся.

        Args:
            employee: Фикстура сотрудника.
        """
        tech: Technologist = Technologist(
            employee=employee, certification="высшая"
        )
        assert tech.name == "Иванов И.И."
        assert tech.processes_count() == 0

    def test_develop_process(
        self,
        employee: Employee,
        piston_part: Part,
    ) -> None:
        """develop_process добавляет процесс.

        Args:
            employee: Фикстура сотрудника.
            piston_part: Фикстура детали.
        """
        tech: Technologist = Technologist(
            employee=employee, certification="высшая"
        )
        process: ProductionProcess = ProductionProcess(
            name="Процесс", part=piston_part
        )
        tech.develop_process(process)
        assert tech.processes_count() == 1

    def test_is_highly_certified(self, employee: Employee) -> None:
        """is_highly_certified проверяет сертификацию.

        Args:
            employee: Фикстура сотрудника.
        """
        high: Technologist = Technologist(
            employee=employee, certification="высшая категория"
        )
        normal: Technologist = Technologist(
            employee=employee, certification="первая"
        )
        assert high.is_highly_certified()
        assert not normal.is_highly_certified()
