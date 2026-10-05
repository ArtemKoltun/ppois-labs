"""
Видимость поста.

Module: common.enums.post_visibility
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from enum import Enum

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class PostVisibility(Enum):
    """Кто может видеть пост.

    Attributes:
        PUBLIC: Все пользователи.
        FRIENDS: Только друзья.
        CLOSE_FRIENDS: Только близкие друзья.
        PRIVATE: Только автор.
    """

    PUBLIC = "public"
    FRIENDS = "friends"
    CLOSE_FRIENDS = "close_friends"
    PRIVATE = "private"

    def __str__(self) -> str:
        """Вернуть человекочитаемое название.

        Returns:
            Строка на русском.
        """
        names: dict[PostVisibility, str] = {
            PostVisibility.PUBLIC: "публичный",
            PostVisibility.FRIENDS: "для друзей",
            PostVisibility.CLOSE_FRIENDS: "для близких друзей",
            PostVisibility.PRIVATE: "приватный",
        }
        return names[self]
