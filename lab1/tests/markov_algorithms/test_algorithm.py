"""
Тесты класса MarkovAlgorithm.

Module: tests.markov_algorithms.test_algorithm
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.enums.machine_status import MachineStatus
from common.exceptions import StepLimitExceededError
from markov_algorithms.domain.algorithm import MarkovAlgorithm
from markov_algorithms.domain.word import Word

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_ADDITION_JSON: str = """
{
  "alphabet": ["1", "+"],
  "initial_word": "11+111",
  "rules": ["1+ -> +1", "+ ->."]
}
"""

_SORT_JSON: str = """
{
  "alphabet": ["a", "b"],
  "initial_word": "aabbaa",
  "rules": ["ba -> ab"]
}
"""

_LOOPING_JSON: str = """
{
  "alphabet": ["a", "b"],
  "initial_word": "a",
  "rules": ["a -> b", "b -> a"]
}
"""


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestMarkovAlgorithm:
    """Проверки класса MarkovAlgorithm."""

    def test_parse(self) -> None:
        """Алгорифм восстанавливается из JSON."""
        algo: MarkovAlgorithm = MarkovAlgorithm.from_string(
            _ADDITION_JSON
        )
        assert str(algo.word) == "11+111"
        assert algo.steps == 0

    def test_alphabet_property(self) -> None:
        """Свойство alphabet возвращает алфавит."""
        algo: MarkovAlgorithm = MarkovAlgorithm.from_string(
            _ADDITION_JSON
        )
        assert "1" in algo.alphabet
        assert "+" in algo.alphabet

    def test_program_property(self) -> None:
        """Свойство program возвращает программу."""
        algo: MarkovAlgorithm = MarkovAlgorithm.from_string(
            _ADDITION_JSON
        )
        assert len(algo.program) == 2

    def test_initial_status(self) -> None:
        """До первого шага статус — NOT_STARTED."""
        algo: MarkovAlgorithm = MarkovAlgorithm.from_string(
            _ADDITION_JSON
        )
        assert algo.status is MachineStatus.NOT_STARTED

    def test_step_changes_word(self) -> None:
        """Один шаг меняет слово."""
        algo: MarkovAlgorithm = MarkovAlgorithm.from_string(
            _ADDITION_JSON
        )
        algo.step()
        assert str(algo.word) == "1+1111"

    def test_step_increments_counter(self) -> None:
        """Счётчик шагов увеличивается."""
        algo: MarkovAlgorithm = MarkovAlgorithm.from_string(
            _ADDITION_JSON
        )
        algo.step()
        assert algo.steps == 1

    def test_status_running_after_step(self) -> None:
        """После шага статус — RUNNING."""
        algo: MarkovAlgorithm = MarkovAlgorithm.from_string(
            _ADDITION_JSON
        )
        algo.step()
        assert algo.status is MachineStatus.RUNNING

    def test_run_to_halt(self) -> None:
        """run доводит алгорифм до остановки."""
        algo: MarkovAlgorithm = MarkovAlgorithm.from_string(
            _ADDITION_JSON
        )
        algo.run()
        assert str(algo.word) == "11111"

    def test_status_halted_after_run(self) -> None:
        """После остановки статус — HALTED."""
        algo: MarkovAlgorithm = MarkovAlgorithm.from_string(
            _ADDITION_JSON
        )
        algo.run()
        assert algo.status is MachineStatus.HALTED

    def test_halted_property(self) -> None:
        """halted возвращает True после остановки."""
        algo: MarkovAlgorithm = MarkovAlgorithm.from_string(
            _ADDITION_JSON
        )
        algo.run()
        assert algo.halted

    def test_run_sort_example(self) -> None:
        """Сортировка a/b выполняется до конца."""
        algo: MarkovAlgorithm = MarkovAlgorithm.from_string(_SORT_JSON)
        algo.run()
        assert str(algo.word) == "aaaabb"

    def test_run_on_step_hook(self) -> None:
        """Callback on_step вызывается на каждом шаге."""
        algo: MarkovAlgorithm = MarkovAlgorithm.from_string(
            _ADDITION_JSON
        )
        calls: list[str] = []
        algo.run(on_step=lambda a: calls.append(str(a.word)))
        assert len(calls) == algo.steps
        assert calls[-1] == "11111"

    def test_run_step_limit_raises(self) -> None:
        """run падает на зацикленном алгорифме."""
        algo: MarkovAlgorithm = MarkovAlgorithm.from_string(
            _LOOPING_JSON
        )
        with pytest.raises(StepLimitExceededError):
            algo.run(max_steps=50)

    def test_reset(self) -> None:
        """reset возвращает алгорифм в начальное состояние."""
        algo: MarkovAlgorithm = MarkovAlgorithm.from_string(
            _ADDITION_JSON
        )
        algo.run()
        algo.reset()
        assert str(algo.word) == "11+111"
        assert algo.steps == 0
        assert algo.status is MachineStatus.NOT_STARTED

    def test_set_word(self) -> None:
        """set_word заменяет текущее слово."""
        algo: MarkovAlgorithm = MarkovAlgorithm.from_string(
            _ADDITION_JSON
        )
        algo.set_word(Word("1+1"))
        assert str(algo.word) == "1+1"

    def test_step_on_halted_returns_false(self) -> None:
        """step возвращает False, если правил нет."""
        algo: MarkovAlgorithm = MarkovAlgorithm.from_string(
            _ADDITION_JSON
        )
        algo.run()
        assert algo.step() is False

    def test_step_on_final_returns_false(self) -> None:
        """step возвращает False при заключительном правиле."""
        algo: MarkovAlgorithm = MarkovAlgorithm.from_string(
            _ADDITION_JSON
        )
        algo.step()  # первое обычное правило
        algo.step()  # снова первое обычное правило
        assert algo.step() is False  # заключительное правило

    def test_round_trip(self) -> None:
        """str → from_string возвращает эквивалент."""
        original: MarkovAlgorithm = MarkovAlgorithm.from_string(
            _ADDITION_JSON
        )
        restored: MarkovAlgorithm = MarkovAlgorithm.from_string(
            str(original)
        )
        assert str(restored.word) == str(original.word)
        assert len(restored.program) == len(original.program)
