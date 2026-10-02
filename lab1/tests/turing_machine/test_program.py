"""
Тесты класса Program.

Module: tests.turing_machine.test_program
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from turing_machine.domain.direction import Direction
from turing_machine.domain.program import Program
from turing_machine.domain.transition import Transition


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _rule(state: str, read: str) -> Transition:
    """Создать правило с заданным состоянием и символом.

    Args:
        state: Имя состояния.
        read: Читаемый символ.

    Returns:
        Правило с фиктивными выходными полями.
    """
    return Transition(state, read, "q_next", "_", Direction.RIGHT)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestProgram:
    """Проверки класса Program."""

    def test_empty(self) -> None:
        """Пустая программа имеет длину 0."""
        assert len(Program()) == 0

    def test_add_rule(self) -> None:
        """add_rule увеличивает длину."""
        program: Program = Program()
        program.add_rule(_rule("q0", "1"))
        assert len(program) == 1

    def test_remove_rule(self) -> None:
        """remove_rule удаляет правило по индексу."""
        program: Program = Program([_rule("q0", "1"), _rule("q1", "0")])
        program.remove_rule(0)
        assert len(program) == 1
        assert program.rules[0] == _rule("q1", "0")

    def test_remove_bad_index_raises(self) -> None:
        """Неверный индекс — IndexError."""
        program: Program = Program([_rule("q0", "1")])
        with pytest.raises(IndexError):
            program.remove_rule(5)

    def test_find(self) -> None:
        """find находит правило по паре (состояние, символ)."""
        rule: Transition = _rule("q0", "1")
        program: Program = Program([rule])
        assert program.find("q0", "1") == rule

    def test_find_missing(self) -> None:
        """find возвращает None, если правила нет."""
        program: Program = Program([_rule("q0", "1")])
        assert program.find("q0", "0") is None

    def test_rules_returns_tuple(self) -> None:
        """rules возвращает неизменяемый кортеж."""
        program: Program = Program([_rule("q0", "1")])
        assert isinstance(program.rules, tuple)

    def test_iteration(self) -> None:
        """Итерация по правилам в порядке добавления."""
        program: Program = Program([_rule("q0", "1"), _rule("q1", "0")])
        assert list(program) == [_rule("q0", "1"), _rule("q1", "0")]

    def test_equality(self) -> None:
        """Программы равны при совпадении списка правил."""
        a: Program = Program([_rule("q0", "1")])
        b: Program = Program([_rule("q0", "1")])
        assert a == b
        assert a != "not a program"

    def test_hash(self) -> None:
        """Равные программы имеют одинаковый хеш."""
        a: Program = Program([_rule("q0", "1")])
        b: Program = Program([_rule("q0", "1")])
        assert hash(a) == hash(b)

    def test_parse_multiline(self) -> None:
        """from_string разбирает программу с несколькими строками."""
        program: Program = Program.from_string(
            "q0 1 q1 0 R\nq1 0 q0 1 L\n"
        )
        assert len(program) == 2

    def test_str(self) -> None:
        """str выводит правила по одному на строку."""
        program: Program = Program([
            _rule("q0", "1"),
            _rule("q1", "0"),
        ])
        assert str(program) == "q0 1 q_next _ R\nq1 0 q_next _ R"
