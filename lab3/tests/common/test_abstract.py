"""
Тесты ABC Readable и Writable.

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
    """Минимальная реализация для тестов."""

    def __init__(self, value: str) -> None:
        """Сохранить значение.

        Args:
            value: Строка.
        """
        self.value: str = value

    def __str__(self) -> str:
        """Вернуть значение.

        Returns:
            Строка.
        """
        return self.value

    @classmethod
    def _parse(cls, text: str) -> "_Sample":
        """Разобрать строку.

        Args:
            text: Входная строка.

        Returns:
            Новый экземпляр.
        """
        return cls(text)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestReadableWritable:
    """Проверки базовых методов ABC."""

    def test_from_string_strips(self) -> None:
        """from_string обрезает пробелы."""
        assert _Sample.from_string("  hi  ").value == "hi"

    def test_from_stream(self) -> None:
        """from_stream читает поток."""
        stream: StringIO = StringIO("hello")
        assert _Sample.from_stream(stream).value == "hello"

    def test_to_stream(self) -> None:
        """to_stream пишет в поток."""
        stream: StringIO = StringIO()
        _Sample("bye").to_stream(stream)
        assert stream.getvalue() == "bye"

    def test_repr(self) -> None:
        """repr имеет формат ClassName(value)."""
        assert repr(_Sample("x")) == "_Sample(x)"
