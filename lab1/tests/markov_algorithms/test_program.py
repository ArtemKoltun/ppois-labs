"""
Тесты класса Program.

Module: tests.markov_algorithms.test_program
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from markov_algorithms.domain.program import Program
from markov_algorithms.domain.substitution import Substitution

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _rule(left: str, right: str) -> Substitution:
    """Создать правило подстановки.

    Args:
        left: Левая часть.
        right: Правая часть.

    Returns:
        Новое правило.
    """
    return Substitution(left, right)


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
        program.add_rule(_rule("a", "b"))
        assert len(program) == 1

    def test_remove_rule(self) -> None:
        """remove_rule удаляет по индексу."""
        program: Program = Program([_rule("a", "b"), _rule("c", "d")])
        program.remove_rule(0)
        assert len(program) == 1
        assert program.rules[0] == _rule("c", "d")

    def test_remove_bad_index_raises(self) -> None:
        """Неверный индекс — IndexError."""
        program: Program = Program([_rule("a", "b")])
        with pytest.raises(IndexError):
            program.remove_rule(5)

    def test_find_returns_first_match(self) -> None:
        """find возвращает первое подходящее правило."""
        first: Substitution = _rule("a", "b")
        second: Substitution = _rule("b", "c")
        program: Program = Program([first, second])
        assert program.find("ab") == first

    def test_find_respects_order(self) -> None:
        """Порядок правил определяет, какое найдётся."""
        specific: Substitution = _rule("ab", "x")
        general: Substitution = _rule("a", "y")
        program: Program = Program([specific, general])
        assert program.find("abc") == specific

    def test_find_missing(self) -> None:
        """find возвращает None, если правила нет."""
        program: Program = Program([_rule("x", "y")])
        assert program.find("abc") is None

    def test_rules_returns_tuple(self) -> None:
        """rules возвращает кортеж."""
        program: Program = Program([_rule("a", "b")])
        assert isinstance(program.rules, tuple)

    def test_iteration(self) -> None:
        """Итерация по правилам."""
        program: Program = Program([_rule("a", "b"), _rule("c", "d")])
        assert list(program) == [_rule("a", "b"), _rule("c", "d")]

    def test_equality(self) -> None:
        """Программы равны при совпадении правил."""
        a: Program = Program([_rule("a", "b")])
        b: Program = Program([_rule("a", "b")])
        assert a == b
        assert a != "not a program"

    def test_hash(self) -> None:
        """Равные программы имеют одинаковый хеш."""
        a: Program = Program([_rule("a", "b")])
        b: Program = Program([_rule("a", "b")])
        assert hash(a) == hash(b)

    def test_parse_multiline(self) -> None:
        """from_string разбирает программу с несколькими строками."""
        program: Program = Program.from_string(
            "a -> b\nb -> c\n"
        )
        assert len(program) == 2

    def test_parse_skips_comments(self) -> None:
        """Комментарии и пустые строки игнорируются."""
        program: Program = Program.from_string(
            "# comment\n\na -> b\n\n"
        )
        assert len(program) == 1

    def test_str(self) -> None:
        """str выводит правила по одному на строку."""
        program: Program = Program([
            _rule("a", "b"),
            _rule("c", "d"),
        ])
        assert str(program) == "a -> b\nc -> d"
