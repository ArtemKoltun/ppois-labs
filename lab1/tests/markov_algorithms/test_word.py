"""
Тесты класса Word.

Module: tests.markov_algorithms.test_word
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from markov_algorithms.domain.word import Word


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestWord:
    """Проверки класса Word."""

    def test_empty(self) -> None:
        """Пустое слово имеет длину 0."""
        assert len(Word()) == 0

    def test_symbols(self) -> None:
        """Свойство symbols возвращает строку."""
        assert Word("abc").symbols == "abc"

    def test_is_empty(self) -> None:
        """is_empty для пустого и непустого слова."""
        assert Word().is_empty()
        assert not Word("a").is_empty()

    def test_replace_first(self) -> None:
        """replace_first заменяет только первое вхождение."""
        word: Word = Word("aXbXc")
        result: Word = word.replace_first("X", "Y")
        assert result.symbols == "aYbXc"

    def test_replace_first_original_unchanged(self) -> None:
        """Исходное слово не меняется."""
        word: Word = Word("ab")
        word.replace_first("a", "c")
        assert word.symbols == "ab"

    def test_replace_first_missing_raises(self) -> None:
        """Отсутствующая подстрока — ошибка."""
        with pytest.raises(ValueError):
            Word("abc").replace_first("x", "y")

    def test_parse_strips(self) -> None:
        """from_string убирает пробелы по краям."""
        assert Word.from_string("  abc  ").symbols == "abc"

    def test_equality(self) -> None:
        """Равные слова равны."""
        assert Word("ab") == Word("ab")
        assert Word("ab") != Word("ac")
        assert Word("ab") != "not a word"

    def test_hash(self) -> None:
        """Равные слова имеют одинаковый хеш."""
        assert hash(Word("ab")) == hash(Word("ab"))

    def test_str(self) -> None:
        """str возвращает строку символов."""
        assert str(Word("hello")) == "hello"
