"""
Тесты общих ABC Readable и Writable.

Module: tests.common.test_abstract
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from io import StringIO

from common.abstract.readable import Readable
from common.abstract.writable import Writable

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

class _Sample(Readable, Writable):
    """Минимальная реализация Readable и Writable для тестов."""

    def __init__(self, value: str) -> None:
        """Сохранить значение.

        Args:
            value: Произвольная строка.
        """
        self.value: str = value

    def __str__(self) -> str:
        """Вернуть значение как строку.

        Returns:
            Содержимое ``value``.
        """
        return self.value

    @classmethod
    def _parse(cls, text: str) -> "_Sample":
        """Разобрать строку.

        Args:
            text: Входная строка.

        Returns:
            Новый экземпляр ``_Sample``.
        """
        return cls(text)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestReadableWritable:
    """Проверки базовых методов Readable и Writable."""

    def test_from_string_strips(self) -> None:
        """from_string обрезает пробелы по краям."""
        assert _Sample.from_string("  hi  ").value == "hi"

    def test_from_stream(self) -> None:
        """from_stream читает поток целиком."""
        stream: StringIO = StringIO("hello")
        assert _Sample.from_stream(stream).value == "hello"

    def test_to_stream(self) -> None:
        """to_stream записывает str-представление."""
        stream: StringIO = StringIO()
        _Sample("bye").to_stream(stream)
        assert stream.getvalue() == "bye"

    def test_repr(self) -> None:
        """repr имеет формат ``ClassName(value)``."""
        assert repr(_Sample("x")) == "_Sample(x)"
