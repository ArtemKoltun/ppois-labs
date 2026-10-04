"""
Тесты класса ProductionProcess.

Module: tests.factory.domain.workshops.test_production_process
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.parts.part import Part
from factory.domain.workshops.production_process import (
    ProductionProcess,
)
from factory.domain.workshops.workshop import Workshop

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestProductionProcess:
    """Проверки класса ProductionProcess."""

    def test_creates(self, piston_part: Part) -> None:
        """Процесс создаётся.

        Args:
            piston_part: Фикстура детали.
        """
        process: ProductionProcess = ProductionProcess(
            name="Изготовление поршня",
            part=piston_part,
            duration_hours=10.0,
        )
        assert process.name == "Изготовление поршня"
        assert process.workshops_count() == 0

    def test_add_workshop(
        self,
        piston_part: Part,
        workshop: Workshop,
    ) -> None:
        """add_workshop добавляет цех.

        Args:
            piston_part: Фикстура детали.
            workshop: Фикстура цеха.
        """
        process: ProductionProcess = ProductionProcess(
            name="Процесс", part=piston_part
        )
        process.add_workshop(workshop)
        assert process.workshops_count() == 1

    def test_total_duration(self, piston_part: Part) -> None:
        """total_duration возвращает длительность.

        Args:
            piston_part: Фикстура детали.
        """
        process: ProductionProcess = ProductionProcess(
            name="X", part=piston_part, duration_hours=15.0
        )
        assert process.total_duration() == 15.0

    def test_is_long(self, piston_part: Part) -> None:
        """is_long проверяет длительность.

        Args:
            piston_part: Фикстура детали.
        """
        long: ProductionProcess = ProductionProcess(
            name="X", part=piston_part, duration_hours=30.0
        )
        short: ProductionProcess = ProductionProcess(
            name="Y", part=piston_part, duration_hours=5.0
        )
        assert long.is_long()
        assert not short.is_long()

    def test_equality(self, piston_part: Part) -> None:
        """Равные процессы по имени.

        Args:
            piston_part: Фикстура детали.
        """
        a: ProductionProcess = ProductionProcess(
            name="X", part=piston_part
        )
        b: ProductionProcess = ProductionProcess(
            name="X", part=piston_part
        )
        assert a == b
        assert a != "not a process"

    def test_hash(self, piston_part: Part) -> None:
        """Хеш по имени.

        Args:
            piston_part: Фикстура детали.
        """
        a: ProductionProcess = ProductionProcess(
            name="X", part=piston_part
        )
        b: ProductionProcess = ProductionProcess(
            name="X", part=piston_part
        )
        assert hash(a) == hash(b)

    def test_str(self, piston_part: Part) -> None:
        """str возвращает имя.

        Args:
            piston_part: Фикстура детали.
        """
        process: ProductionProcess = ProductionProcess(
            name="Процесс 1", part=piston_part
        )
        assert "Процесс 1" in str(process)
