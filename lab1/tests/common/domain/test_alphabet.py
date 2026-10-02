"""
Тесты класса Alphabet.

Module: tests.common.domain.test_alphabet
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.domain.alphabet import Alphabet


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestAlphabet:
    """Проверки класса Alphabet."""

    def test_empty(self) -> None:
        """Пустой алфавит имеет длину 0."""
        assert len(Alphabet()) == 0

    def test_contains(self) -> None:
        """Проверка оператора in."""
        alphabet: Alphabet = Alphabet("abc")
        assert "a" in alphabet
        assert "z" not in alphabet

    def test_add_idempotent(self) -> None:
        """Повторное добавление не меняет мощность."""
        alphabet: Alphabet = Alphabet("a")
        alphabet.add("a")
        assert len(alphabet) == 1

    def test_remove(self) -> None:
        """Удаление убирает символ."""
        alphabet: Alphabet = Alphabet("abc")
        alphabet.remove("b")
        assert "b" not in alphabet

    def test_remove_missing_raises(self) -> None:
        """Удаление отсутствующего символа — KeyError."""
        with pytest.raises(KeyError):
            Alphabet("a").remove("z")

    def test_validate_multi_char_raises(self) -> None:
        """Многосимвольная строка недопустима."""
        with pytest.raises(ValueError):
            Alphabet(["ab"])

    def test_validate_non_string_raises(self) -> None:
        """Не-строка недопустима."""
        with pytest.raises(TypeError):
            Alphabet([1])  # type: ignore[list-item]

    def test_equality_ignores_order(self) -> None:
        """Порядок не влияет на равенство."""
        assert Alphabet("abc") == Alphabet("cba")

    def test_inequality(self) -> None:
        """Разные множества не равны."""
        assert Alphabet("abc") != Alphabet("abd")

    def test_hash_equal_for_equal(self) -> None:
        """Равные алфавиты имеют одинаковый хеш."""
        assert hash(Alphabet("abc")) == hash(Alphabet("cba"))

    def test_iteration_preserves_order(self) -> None:
        """Порядок итерации — порядок добавления."""
        assert list(Alphabet("abc")) == ["a", "b", "c"]

    def test_str(self) -> None:
        """Формат str — множество в фигурных скобках."""
        assert str(Alphabet("abc")) == "{a, b, c}"

    def test_parse_with_braces(self) -> None:
        """from_string со скобками и запятыми."""
        assert Alphabet.from_string("{a, b, c}") == Alphabet("abc")

    def test_parse_without_braces(self) -> None:
        """from_string без скобок."""
        assert Alphabet.from_string("abc") == Alphabet("abc")

    def test_parse_with_commas_no_braces(self) -> None:
        """from_string с запятыми без скобок."""
        assert Alphabet.from_string("a, b, c") == Alphabet("abc")
