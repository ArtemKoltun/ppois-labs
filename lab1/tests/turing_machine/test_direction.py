"""
Тесты перечисления Direction.

Module: tests.turing_machine.test_direction
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from turing_machine.domain.direction import Direction

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestDirection:
    """Проверки Direction.from_char."""

    def test_from_char_uppercase(self) -> None:
        """Верхний регистр распознаётся."""
        assert Direction.from_char("L") is Direction.LEFT
        assert Direction.from_char("R") is Direction.RIGHT
        assert Direction.from_char("S") is Direction.STAY

    def test_from_char_lowercase(self) -> None:
        """Нижний регистр тоже принимается."""
        assert Direction.from_char("l") is Direction.LEFT

    def test_from_char_unknown_raises(self) -> None:
        """Неизвестный символ — ValueError."""
        with pytest.raises(ValueError):
            Direction.from_char("X")

    def test_values(self) -> None:
        """Значения Enum соответствуют однобуквенным меткам."""
        assert Direction.LEFT.value == "L"
        assert Direction.RIGHT.value == "R"
        assert Direction.STAY.value == "S"
