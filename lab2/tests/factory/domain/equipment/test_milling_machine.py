"""
Тесты класса MillingMachine.

Module: tests.factory.domain.equipment.test_milling_machine
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.equipment.machine import Machine
from factory.domain.equipment.milling_machine import MillingMachine


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_milling(
    base: Machine,
    axes: int = 3,
    table: float = 500.0,
) -> MillingMachine:
    """Создать фрезерный станок.

    Args:
        base: Базовый станок.
        axes: Число осей.
        table: Размер стола.

    Returns:
        Объект ``MillingMachine``.
    """
    return MillingMachine(
        machine=base,
        axes_count=axes,
        table_size=table,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestMillingMachine:
    """Проверки класса MillingMachine."""

    def test_creates(self, machine: Machine) -> None:
        """Станок создаётся.

        Args:
            machine: Фикстура станка.
        """
        milling: MillingMachine = _make_milling(machine)
        assert milling.name == "Токарный 16К20"

    def test_is_multiaxis(self, machine: Machine) -> None:
        """is_multiaxis проверяет число осей.

        Args:
            machine: Фикстура станка.
        """
        three: MillingMachine = _make_milling(machine, axes=3)
        five: MillingMachine = _make_milling(machine, axes=5)
        assert not three.is_multiaxis()
        assert five.is_multiaxis()

    def test_can_process_part(self, machine: Machine) -> None:
        """can_process_part проверяет размер детали.

        Args:
            machine: Фикстура станка.
        """
        milling: MillingMachine = _make_milling(machine, table=500.0)
        assert milling.can_process_part(300.0)
        assert not milling.can_process_part(600.0)
