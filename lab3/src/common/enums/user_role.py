"""
Роль пользователя в социальной сети.

Module: common.enums.user_role
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from enum import Enum

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class UserRole(Enum):
    """Роль пользователя в системе.

    Attributes:
        USER: Обычный пользователь.
        MODERATOR: Модератор.
        ADMIN: Администратор.
        ADVERTISER: Рекламодатель.
    """

    USER = "user"
    MODERATOR = "moderator"
    ADMIN = "admin"
    ADVERTISER = "advertiser"

    def __str__(self) -> str:
        """Вернуть человекочитаемое название.

        Returns:
            Строка на русском.
        """
        names: dict[UserRole, str] = {
            UserRole.USER: "пользователь",
            UserRole.MODERATOR: "модератор",
            UserRole.ADMIN: "администратор",
            UserRole.ADVERTISER: "рекламодатель",
        }
        return names[self]
