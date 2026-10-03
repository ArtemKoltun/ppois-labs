"""
Тесты функций ввода.

Module: tests.common.ui.test_prompts
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.ui.prompts import ask_int, ask_str, confirm

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _feed(monkeypatch: pytest.MonkeyPatch, values: list[str]) -> None:
    """Подменить input последовательностью значений.

    Args:
        monkeypatch: Фикстура pytest.
        values: Значения, возвращаемые input по очереди.

    Returns:
        Ничего не возвращает.
    """
    iterator = iter(values)
    monkeypatch.setattr("builtins.input", lambda _="": next(iterator))


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestAskStr:
    """Проверки ask_str."""

    def test_strips(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Пробелы по краям убираются."""
        _feed(monkeypatch, ["  hello  "])
        assert ask_str("> ") == "hello"


class TestAskInt:
    """Проверки ask_int."""

    def test_valid_first_try(
        self,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Корректное значение возвращается сразу."""
        _feed(monkeypatch, ["5"])
        assert ask_int("> ", 1, 10) == 5

    def test_retries_on_non_number(
        self,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Нечисловое значение приводит к повторному запросу."""
        _feed(monkeypatch, ["abc", "5"])
        assert ask_int("> ", 1, 10) == 5

    def test_retries_on_out_of_range(
        self,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Значение вне диапазона приводит к повторному запросу."""
        _feed(monkeypatch, ["99", "5"])
        assert ask_int("> ", 1, 10) == 5


class TestConfirm:
    """Проверки confirm."""

    @pytest.mark.parametrize(
        "answer",
        ["y", "Y", "yes", "д", "да"],
    )
    def test_yes(
        self,
        monkeypatch: pytest.MonkeyPatch,
        answer: str,
    ) -> None:
        """Ответы согласия распознаются."""
        _feed(monkeypatch, [answer])
        assert confirm("?") is True

    @pytest.mark.parametrize(
        "answer",
        ["n", "N", "no", "н", "нет"],
    )
    def test_no(
        self,
        monkeypatch: pytest.MonkeyPatch,
        answer: str,
    ) -> None:
        """Ответы отказа распознаются."""
        _feed(monkeypatch, [answer])
        assert confirm("?") is False

    def test_retries_on_garbage(
        self,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Непонятный ответ — повтор."""
        _feed(monkeypatch, ["maybe", "y"])
        assert confirm("?") is True
