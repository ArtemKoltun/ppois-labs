"""
Тесты класса Head.

Module: tests.turing_machine.test_head
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from turing_machine.domain.direction import Direction
from turing_machine.domain.head import Head


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestHead:
    """Проверки класса Head."""

    def test_default_position(self) -> None:
        """По умолчанию позиция равна 0."""
        assert Head().position == 0

    def test_custom_position(self) -> None:
        """Позиция задаётся в конструкторе."""
        assert Head(5).position == 5

    def test_increment(self) -> None:
        """increment сдвигает вправо."""
        head: Head = Head()
        head.increment()
        assert head.position == 1

    def test_decrement(self) -> None:
        """decrement сдвигает влево."""
        head: Head = Head()
        head.decrement()
        assert head.position == -1

    def test_move_left(self) -> None:
        """Движение влево."""
        head: Head = Head()
        head.move(Direction.LEFT)
        assert head.position == -1

    def test_move_right(self) -> None:
        """Движение вправо."""
        head: Head = Head()
        head.move(Direction.RIGHT)
        assert head.position == 1

    def test_move_stay(self) -> None:
        """STAY не меняет позицию."""
        head: Head = Head(7)
        head.move(Direction.STAY)
        assert head.position == 7

    def test_reset(self) -> None:
        """reset возвращает в заданную позицию."""
        head: Head = Head(5)
        head.reset()
        assert head.position == 0
        head.reset(3)
        assert head.position == 3

    def test_equality(self) -> None:
        """Совпадающие позиции — равные каретки."""
        assert Head(3) == Head(3)
        assert Head(3) != Head(4)
        assert Head(3) != "not a head"

    def test_hash(self) -> None:
        """Равные каретки имеют одинаковый хеш."""
        assert hash(Head(3)) == hash(Head(3))

    def test_str(self) -> None:
        """Формат str."""
        assert str(Head(3)) == "Head(position=3)"
