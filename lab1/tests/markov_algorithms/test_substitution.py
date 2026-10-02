"""
Тесты класса Substitution.

Module: tests.markov_algorithms.test_substitution
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from markov_algorithms.domain.substitution import Substitution


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestSubstitution:
    """Проверки класса Substitution."""

    def test_properties(self) -> None:
        """Свойства возвращают исходные значения."""
        rule: Substitution = Substitution("ab", "ba")
        assert rule.left == "ab"
        assert rule.right == "ba"
        assert rule.is_final is False

    def test_final_flag(self) -> None:
        """Заключительное правило возвращает is_final=True."""
        rule: Substitution = Substitution("x", "y", is_final=True)
        assert rule.is_final is True

    def test_both_empty_raises(self) -> None:
        """Обе пустые части недопустимы."""
        with pytest.raises(ValueError):
            Substitution("", "")

    def test_empty_left_allowed(self) -> None:
        """Пустая левая часть допустима."""
        rule: Substitution = Substitution("", "x")
        assert rule.left == ""

    def test_empty_right_allowed(self) -> None:
        """Пустая правая часть допустима."""
        rule: Substitution = Substitution("x", "")
        assert rule.right == ""

    def test_matches_true(self) -> None:
        """matches находит вхождение левой части."""
        assert Substitution("ab", "ba").matches("xxabxx")

    def test_matches_false(self) -> None:
        """matches возвращает False при отсутствии."""
        assert not Substitution("ab", "ba").matches("xxbaxx")

    def test_parse_plain(self) -> None:
        """from_string разбирает обычное правило."""
        rule: Substitution = Substitution.from_string("ab -> ba")
        assert rule == Substitution("ab", "ba")

    def test_parse_final(self) -> None:
        """from_string распознаёт заключительное правило."""
        rule: Substitution = Substitution.from_string("+ ->. ")
        assert rule.is_final is True
        assert rule.left == "+"
        assert rule.right == ""

    def test_parse_no_arrow_raises(self) -> None:
        """Строка без стрелки — ошибка."""
        with pytest.raises(ValueError):
            Substitution.from_string("ab")

    def test_equality(self) -> None:
        """Равные правила равны."""
        assert Substitution("a", "b") == Substitution("a", "b")
        assert Substitution("a", "b") != Substitution("a", "c")
        assert Substitution("a", "b") != "not a rule"

    def test_hash(self) -> None:
        """Равные правила имеют одинаковый хеш."""
        assert hash(Substitution("a", "b")) == hash(
            Substitution("a", "b")
        )

    def test_str_plain(self) -> None:
        """str обычного правила."""
        assert str(Substitution("ab", "ba")) == "ab -> ba"

    def test_str_final(self) -> None:
        """str заключительного правила."""
        rule: Substitution = Substitution("+", "", is_final=True)
        assert str(rule) == "+ ->. "

    def test_round_trip(self) -> None:
        """str → from_string возвращает равное правило."""
        original: Substitution = Substitution("abc", "xyz")
        restored: Substitution = Substitution.from_string(str(original))
        assert original == restored
