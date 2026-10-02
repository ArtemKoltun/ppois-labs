"""
Тесты класса Transition.

Module: tests.turing_machine.test_transition
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from turing_machine.domain.direction import Direction
from turing_machine.domain.transition import Transition


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_transition() -> Transition:
    """Создать эталонное правило для тестов.

    Returns:
        Правило ``q0 1 q1 0 R``.
    """
    return Transition(
        current_state="q0",
        read_symbol="1",
        next_state="q1",
        write_symbol="0",
        direction=Direction.RIGHT,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestTransition:
    """Проверки класса Transition."""

    def test_properties(self) -> None:
        """Свойства возвращают исходные значения."""
        rule: Transition = _make_transition()
        assert rule.current_state == "q0"
        assert rule.read_symbol == "1"
        assert rule.next_state == "q1"
        assert rule.write_symbol == "0"
        assert rule.direction is Direction.RIGHT

    def test_matches(self) -> None:
        """matches реагирует только на полное совпадение."""
        rule: Transition = _make_transition()
        assert rule.matches("q0", "1")
        assert not rule.matches("q0", "0")
        assert not rule.matches("q1", "1")

    def test_empty_state_raises(self) -> None:
        """Пустое имя состояния недопустимо."""
        with pytest.raises(ValueError):
            Transition("", "1", "q1", "0", Direction.RIGHT)

    def test_bad_symbol_raises(self) -> None:
        """Символ длиной != 1 недопустим."""
        with pytest.raises(ValueError):
            Transition("q0", "12", "q1", "0", Direction.RIGHT)

    def test_parse(self) -> None:
        """from_string разбирает правило."""
        rule: Transition = Transition.from_string("q0 1 q1 0 R")
        assert rule == _make_transition()

    def test_parse_wrong_parts_raises(self) -> None:
        """Мало полей — ошибка."""
        with pytest.raises(ValueError):
            Transition.from_string("q0 1 q1")

    def test_equality(self) -> None:
        """Равные правила равны."""
        assert _make_transition() == _make_transition()
        assert _make_transition() != "not a rule"

    def test_inequality(self) -> None:
        """Разные правила не равны."""
        other: Transition = Transition(
            "q0", "1", "q2", "0", Direction.RIGHT
        )
        assert _make_transition() != other

    def test_hash(self) -> None:
        """Равные правила имеют одинаковый хеш."""
        assert hash(_make_transition()) == hash(_make_transition())

    def test_str(self) -> None:
        """Формат str — пять полей через пробел."""
        assert str(_make_transition()) == "q0 1 q1 0 R"

    def test_round_trip(self) -> None:
        """str → from_string возвращает равное правило."""
        original: Transition = _make_transition()
        restored: Transition = Transition.from_string(str(original))
        assert original == restored
