"""
Точка входа лабораторной работы №2.

Module: main
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

import sys

from common.domain.address import Address
from factory.domain.management.factory import Factory
from factory.ui.menu import build_menu


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_DEFAULT_FACTORY_NAME: str = "Автодеталь"
"""Имя завода по умолчанию."""


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> int:
    """Запустить приложение.

    Returns:
        Код возврата процесса.
    """
    factory: Factory = _create_default_factory()
    menu = build_menu(factory)
    try:
        menu.run()
    except (KeyboardInterrupt, EOFError):
        print("\nВыход.")
    return 0


# ---------------------------------------------------------------------------
# Private functions
# ---------------------------------------------------------------------------

def _create_default_factory() -> Factory:
    """Создать завод с начальными данными.

    Returns:
        Готовый объект завода.
    """
    address: Address = Address(
        country="Россия",
        city="Москва",
        street="Заводская",
        building="1",
        postal_code="101000",
    )
    return Factory(name=_DEFAULT_FACTORY_NAME, address=address)


if __name__ == "__main__":
    sys.exit(main())
