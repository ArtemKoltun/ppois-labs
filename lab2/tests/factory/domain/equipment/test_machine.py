"""
Тесты класса Machine.

Module: tests.factory.domain.equipment.test_machine
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.equipment.machine import Machine

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestMachine:
    """Проверки класса Machine."""

    def test_creates(self, machine: Machine) -> None:
        """Станок создаётся.

        Args:
            machine: Фикстура станка.
        """
        assert machine.name == "Токарный 16К20"

    def test_is_high_power(self, machine: Machine) -> None:
        """is_high_power проверяет мощность.

        Args:
            machine: Фикстура станка.
        """
        assert not machine.is_high_power()

    def test_calculate_output(self, machine: Machine) -> None:
        """calculate_output считает операции.

        Args:
            machine: Фикстура станка.
        """
        assert machine.calculate_output(10.0) == 20

    def test_needs_maintenance(self, machine: Machine) -> None:
        """needs_maintenance проверяет часы.

        Args:
            machine: Фикстура станка.
        """
        assert not machine.needs_maintenance()
        machine.add_hours(2000.0)
        assert machine.needs_maintenance()
