"""
Тесты класса Menu.

Module: tests.common.ui.test_menu
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.enums.menu_result import MenuResult
from common.ui.menu import Menu, MenuItem

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _patch_choices(
    monkeypatch: pytest.MonkeyPatch,
    choices: list[int],
) -> None:
    """Подменить ask_int на последовательность выборов.

    Args:
        monkeypatch: Фикстура pytest.
        choices: Значения, возвращаемые ask_int по очереди.

    Returns:
        Ничего не возвращает.
    """
    iterator = iter(choices)
    monkeypatch.setattr(
        "common.ui.menu.ask_int",
        lambda prompt, minimum, maximum: next(iterator),
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestMenu:
    """Проверки класса Menu."""

    def test_back_returns_back(
        self,
        monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        """Выбор 0 возвращает BACK."""
        _patch_choices(monkeypatch, [0])
        menu: Menu = Menu("Test", [])
        assert menu.run() is MenuResult.BACK

    def test_action_called(
        self,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Выбор пункта вызывает его action, затем выход."""
        calls: list[int] = []
        _patch_choices(monkeypatch, [1, 0])
        menu: Menu = Menu(
            "Test",
            [MenuItem("A", lambda: calls.append(1))],
        )
        menu.run()
        assert calls == [1]

    def test_exit_stops_menu(
        self,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Пункт, возвращающий EXIT, завершает цикл."""
        _patch_choices(monkeypatch, [1])
        menu: Menu = Menu(
            "Test",
            [MenuItem("Exit", lambda: MenuResult.EXIT)],
        )
        assert menu.run() is MenuResult.EXIT

    def test_prints_title_and_items(
        self,
        monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        """Заголовок и пункты печатаются."""
        _patch_choices(monkeypatch, [0])
        menu: Menu = Menu("Hello", [MenuItem("Первый", lambda: None)])
        menu.run()
        out: str = capsys.readouterr().out
        assert "Hello" in out
        assert "Первый" in out
