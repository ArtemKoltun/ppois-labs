"""
Консольное меню с пунктами и циклом обработки.

Module: common.ui.menu
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from collections.abc import Callable, Iterable
from dataclasses import dataclass

from common.ui.prompts import ask_int

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_BACK_CHOICE: int = 0
"""Номер пункта, возвращающего из меню."""


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class MenuItem:
    """Один пункт меню.

    Attributes:
        label: Название пункта для отображения.
        action: Функция без аргументов.
    """

    label: str
    action: Callable[[], None]


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Menu:
    """Интерактивное меню с циклом и обработкой выбора.

    Attributes:
        _title: Заголовок меню.
        _items: Список пунктов.
    """

    def __init__(
        self,
        title: str,
        items: Iterable[MenuItem],
    ) -> None:
        """Создать меню.

        Args:
            title: Заголовок, отображаемый сверху.
            items: Пункты меню в порядке отображения.
        """
        self._title: str = title
        self._items: list[MenuItem] = list(items)

    def run(self) -> None:
        """Запустить цикл меню до выбора «Назад».

        Returns:
            Ничего не возвращает.
        """
        while True:
            self._print()
            choice: int = ask_int(
                f"Выбор [{_BACK_CHOICE}-{len(self._items)}]: ",
                _BACK_CHOICE,
                len(self._items),
            )
            if choice == _BACK_CHOICE:
                return
            self._items[choice - 1].action()

    def _print(self) -> None:
        """Напечатать заголовок и список пунктов.

        Returns:
            Ничего не возвращает.
        """
        print()
        print(self._title)
        print("-" * len(self._title))
        for index, item in enumerate(self._items, start=1):
            print(f"  {index}. {item.label}")
        print(f"  {_BACK_CHOICE}. Назад")
