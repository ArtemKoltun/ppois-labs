"""
Тесты перечисления MachineStatus.

Module: tests.common.enums.test_machine_status
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.enums.machine_status import MachineStatus

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestMachineStatus:
    """Проверки MachineStatus."""

    def test_values(self) -> None:
        """Значения соответствуют строковым меткам."""
        assert MachineStatus.NOT_STARTED.value == "not_started"
        assert MachineStatus.RUNNING.value == "running"
        assert MachineStatus.HALTED.value == "halted"

    def test_str_not_started(self) -> None:
        """str для NOT_STARTED — человекочитаемое."""
        assert str(MachineStatus.NOT_STARTED) == "не запущена"

    def test_str_running(self) -> None:
        """str для RUNNING — человекочитаемое."""
        assert str(MachineStatus.RUNNING) == "выполняется"

    def test_str_halted(self) -> None:
        """str для HALTED — человекочитаемое."""
        assert str(MachineStatus.HALTED) == "остановлена"

    def test_distinct_members(self) -> None:
        """Элементы перечисления попарно различны."""
        statuses: set[MachineStatus] = {
            MachineStatus.NOT_STARTED,
            MachineStatus.RUNNING,
            MachineStatus.HALTED,
        }
        assert len(statuses) == 3
