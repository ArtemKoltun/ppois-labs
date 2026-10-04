"""
Тесты класса CNCMachine.

Module: tests.factory.domain.equipment.test_cnc_machine
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.equipment.cnc_machine import CNCMachine
from factory.domain.equipment.machine import Machine

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestCNCMachine:
    """Проверки класса CNCMachine."""

    def test_creates(self, machine: Machine) -> None:
        """Станок создаётся.

        Args:
            machine: Фикстура станка.
        """
        cnc: CNCMachine = CNCMachine(
            machine=machine,
            controller_model="Fanuc",
        )
        assert cnc.name == "Токарный 16К20"

    def test_load_program(self, machine: Machine) -> None:
        """load_program увеличивает счётчик.

        Args:
            machine: Фикстура станка.
        """
        cnc: CNCMachine = CNCMachine(
            machine=machine, controller_model="Fanuc"
        )
        cnc.load_program()
        assert cnc.can_remote_control() is False  # нет сети

    def test_is_connected(self, machine: Machine) -> None:
        """is_connected возвращает наличие сети.

        Args:
            machine: Фикстура станка.
        """
        connected: CNCMachine = CNCMachine(
            machine=machine,
            controller_model="Fanuc",
            has_network=True,
        )
        not_connected: CNCMachine = CNCMachine(
            machine=machine,
            controller_model="Fanuc",
            has_network=False,
        )
        assert connected.is_connected()
        assert not not_connected.is_connected()

    def test_can_remote_control(self, machine: Machine) -> None:
        """can_remote_control нужен и сети, и программа.

        Args:
            machine: Фикстура станка.
        """
        cnc: CNCMachine = CNCMachine(
            machine=machine,
            controller_model="Fanuc",
            has_network=True,
        )
        assert not cnc.can_remote_control()
        cnc.load_program()
        assert cnc.can_remote_control()
