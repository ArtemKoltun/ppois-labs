"""
Точка входа лабораторной работы №3.

Module: main
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

import sys

from social.domain.users.user import User
from social.ui.menu import SocialSession, build_menu

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_DEFAULT_USERNAME: str = "demo_user"
"""Имя пользователя по умолчанию."""

_DEFAULT_EMAIL: str = "demo@social.net"
"""Email по умолчанию."""

_DEFAULT_DISPLAY_NAME: str = "Демо Пользователь"
"""Отображаемое имя."""


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> int:
    """Запустить приложение.

    Returns:
        Код возврата процесса.
    """
    user: User = _create_default_user()
    session: SocialSession = SocialSession(user)
    menu = build_menu(session)
    try:
        menu.run()
    except (KeyboardInterrupt, EOFError):
        print("\nВыход.")
    return 0


# ---------------------------------------------------------------------------
# Private functions
# ---------------------------------------------------------------------------

def _create_default_user() -> User:
    """Создать пользователя по умолчанию.

    Returns:
        Объект ``User``.
    """
    return User(
        username=_DEFAULT_USERNAME,
        email=_DEFAULT_EMAIL,
        display_name=_DEFAULT_DISPLAY_NAME,
    )


if __name__ == "__main__":
    sys.exit(main())
