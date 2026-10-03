"""
Тесты класса TuringMachine.

Module: tests.turing_machine.test_machine
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.enums.machine_status import MachineStatus
from common.exceptions import StepLimitExceededError
from turing_machine.domain.machine import TuringMachine

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_MACHINE_JSON: str = """
{
  "alphabet": ["_", "1"],
  "blank": "_",
  "initial_tape": "111",
  "initial_head": 0,
  "initial_state": "q0",
  "final_states": ["q_accept"],
  "transitions": [
    "q0 1 q0 1 R",
    "q0 _ q_accept _ S"
  ]
}
"""

_LOOPING_JSON: str = """
{
  "alphabet": ["_", "1"],
  "blank": "_",
  "initial_tape": "1",
  "initial_head": 0,
  "initial_state": "q0",
  "final_states": ["q_accept"],
  "transitions": [
    "q0 1 q0 1 R",
    "q0 _ q0 1 L"
  ]
}
"""


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestTuringMachine:
    """Проверки класса TuringMachine."""

    def test_parse(self) -> None:
        """Машина восстанавливается из JSON."""
        machine: TuringMachine = TuringMachine.from_string(_MACHINE_JSON)
        assert machine.state == "q0"
        assert machine.head.position == 0
        assert str(machine.tape) == "111"

    def test_initial_status(self) -> None:
        """До первого шага статус — NOT_STARTED."""
        machine: TuringMachine = TuringMachine.from_string(_MACHINE_JSON)
        assert machine.status is MachineStatus.NOT_STARTED
        assert machine.steps == 0

    def test_step_moves_head(self) -> None:
        """Один шаг двигает каретку вправо."""
        machine: TuringMachine = TuringMachine.from_string(_MACHINE_JSON)
        machine.step()
        assert machine.head.position == 1

    def test_step_increments_counter(self) -> None:
        """Счётчик шагов увеличивается."""
        machine: TuringMachine = TuringMachine.from_string(_MACHINE_JSON)
        machine.step()
        assert machine.steps == 1

    def test_status_running_after_step(self) -> None:
        """После первого шага статус — RUNNING."""
        machine: TuringMachine = TuringMachine.from_string(_MACHINE_JSON)
        machine.step()
        assert machine.status is MachineStatus.RUNNING

    def test_step_returns_true_while_running(self) -> None:
        """step возвращает True, пока есть правило."""
        machine: TuringMachine = TuringMachine.from_string(_MACHINE_JSON)
        assert machine.step() is True

    def test_step_returns_false_on_halt(self) -> None:
        """step возвращает False, когда правило не найдено."""
        machine: TuringMachine = TuringMachine.from_string(_MACHINE_JSON)
        machine.run()
        assert machine.step() is False

    def test_run_to_halt(self) -> None:
        """run доводит машину до конечного состояния."""
        machine: TuringMachine = TuringMachine.from_string(_MACHINE_JSON)
        machine.run()
        assert machine.state == "q_accept"

    def test_status_halted_after_run(self) -> None:
        """После остановки статус — HALTED."""
        machine: TuringMachine = TuringMachine.from_string(_MACHINE_JSON)
        machine.run()
        assert machine.status is MachineStatus.HALTED

    def test_halted_property(self) -> None:
        """halted возвращает True после остановки."""
        machine: TuringMachine = TuringMachine.from_string(_MACHINE_JSON)
        machine.run()
        assert machine.halted

    def test_run_step_limit_raises(self) -> None:
        """run падает на зацикленной машине."""
        machine: TuringMachine = TuringMachine.from_string(_LOOPING_JSON)
        with pytest.raises(StepLimitExceededError):
            machine.run(max_steps=50)

    def test_reset(self) -> None:
        """reset возвращает машину в начальное состояние."""
        machine: TuringMachine = TuringMachine.from_string(_MACHINE_JSON)
        machine.run()
        machine.reset()
        assert machine.state == "q0"
        assert machine.head.position == 0
        assert str(machine.tape) == "111"

    def test_reset_clears_steps(self) -> None:
        """reset сбрасывает счётчик шагов."""
        machine: TuringMachine = TuringMachine.from_string(_MACHINE_JSON)
        machine.step()
        machine.reset()
        assert machine.steps == 0
        assert machine.status is MachineStatus.NOT_STARTED

    def test_round_trip(self) -> None:
        """str → from_string возвращает эквивалентную машину."""
        original: TuringMachine = TuringMachine.from_string(_MACHINE_JSON)
        restored: TuringMachine = TuringMachine.from_string(str(original))
        assert restored.state == original.state
        assert restored.head.position == original.head.position
        assert str(restored.tape) == str(original.tape)
