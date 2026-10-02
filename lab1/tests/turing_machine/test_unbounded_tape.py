"""
Тесты класса UnboundedTape.

Module: tests.turing_machine.test_unbounded_tape
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from turing_machine.domain.unbounded_tape import UnboundedTape


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestUnboundedTape:
    """Проверки класса UnboundedTape."""

    def test_empty_tape_reads_blank(self) -> None:
        """Пустая лента читает blank."""
        tape: UnboundedTape = UnboundedTape()
        assert tape.read(0) == "_"

    def test_reads_initial_symbols(self) -> None:
        """Начальное содержимое доступно с позиции start."""
        tape: UnboundedTape = UnboundedTape(initial="abc")
        assert tape.read(0) == "a"
        assert tape.read(1) == "b"
        assert tape.read(2) == "c"

    def test_reads_outside_initial_range(self) -> None:
        """За пределами содержимого читается blank."""
        tape: UnboundedTape = UnboundedTape(initial="abc")
        assert tape.read(-1) == "_"
        assert tape.read(3) == "_"

    def test_write_and_read(self) -> None:
        """Запись и последующее чтение совпадают."""
        tape: UnboundedTape = UnboundedTape()
        tape.write(5, "x")
        assert tape.read(5) == "x"

    def test_write_blank_clears_cell(self) -> None:
        """Запись blank удаляет ячейку."""
        tape: UnboundedTape = UnboundedTape(initial="abc")
        tape.write(0, "_")
        assert tape.read(0) == "_"

    def test_write_wrong_length_raises(self) -> None:
        """Многосимвольная запись недопустима."""
        tape: UnboundedTape = UnboundedTape()
        with pytest.raises(ValueError):
            tape.write(0, "xy")

    def test_blank_wrong_length_raises(self) -> None:
        """Blank длиной != 1 недопустим."""
        with pytest.raises(ValueError):
            UnboundedTape(blank="__")

    def test_equality(self) -> None:
        """Совпадающие ленты равны, разные — нет."""
        a: UnboundedTape = UnboundedTape(initial="abc")
        b: UnboundedTape = UnboundedTape(initial="abc")
        c: UnboundedTape = UnboundedTape(initial="abd")
        assert a == b
        assert a != c
        assert a != "not a tape"

    def test_hash_equal_for_equal_tapes(self) -> None:
        """Равные ленты имеют одинаковый хеш."""
        a: UnboundedTape = UnboundedTape(initial="abc")
        b: UnboundedTape = UnboundedTape(initial="abc")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """Строковое представление — содержимое ленты."""
        tape: UnboundedTape = UnboundedTape(initial="abc")
        assert str(tape) == "abc"

    def test_str_empty_tape(self) -> None:
        """Пустая лента выводит blank."""
        assert str(UnboundedTape()) == "_"

    def test_parse_plain_text(self) -> None:
        """from_string читает ленту без префикса."""
        tape: UnboundedTape = UnboundedTape.from_string("abc")
        assert tape.read(0) == "a"
        assert str(tape) == "abc"

    def test_parse_with_blank_prefix(self) -> None:
        """from_string распознаёт префикс blank=."""
        tape: UnboundedTape = UnboundedTape.from_string("blank=. abc")
        assert tape.blank == "."
        assert str(tape) == "abc"

    def test_round_trip_through_string(self) -> None:
        """str → from_string возвращает равную ленту."""
        original: UnboundedTape = UnboundedTape(initial="hello")
        restored: UnboundedTape = UnboundedTape.from_string(str(original))
        assert original == restored
