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

from common.enums.menu_result import MenuResult
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
        action: Функция без аргументов. Возвращает ``None`` или
            :attr:`MenuResult.CONTINUE`, чтобы продолжить в текущем
            меню; :attr:`MenuResult.EXIT` — чтобы завершить всю
            программу.
    """

    label: str
    action: Callable[[], MenuResult | None]


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Menu:
    """Интерактивное меню с циклом и обработкой выбора.

    Attributes:
        _title: Заголовок меню.
        _items: Список пунктов.
    """

    # -----------------------------------------------------------------------
    # Constructors
    # -----------------------------------------------------------------------

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

    # -----------------------------------------------------------------------
    # Public methods
    # -----------------------------------------------------------------------

    def run(self) -> MenuResult:
        """Запустить цикл меню до возврата или выхода.

        Returns:
            :attr:`MenuResult.BACK`, если пользователь выбрал
            «Назад»; :attr:`MenuResult.EXIT`, если какой-то пункт
            запросил завершение программы.
        """
        while True:
            self._print()
            choice: int = ask_int(
                f"Выбор [{_BACK_CHOICE}-{len(self._items)}]: ",
                _BACK_CHOICE,
                len(self._items),
            )
            if choice == _BACK_CHOICE:
                return MenuResult.BACK
            result: MenuResult | None = (
                self._items[choice - 1].action()
            )
            if result is MenuResult.EXIT:
                return MenuResult.EXIT

    # -----------------------------------------------------------------------
    # Private methods
    # -----------------------------------------------------------------------

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
