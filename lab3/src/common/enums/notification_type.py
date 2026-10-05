"""
Тип уведомления.

Module: common.enums.notification_type
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from enum import Enum

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class NotificationType(Enum):
    """Тип уведомления.

    Attributes:
        LIKE: Лайк.
        COMMENT: Комментарий.
        FRIEND_REQUEST: Заявка в друзья.
        MESSAGE: Сообщение.
        MENTION: Упоминание.
        SYSTEM: Системное.
    """

    LIKE = "like"
    COMMENT = "comment"
    FRIEND_REQUEST = "friend_request"
    MESSAGE = "message"
    MENTION = "mention"
    SYSTEM = "system"

    def __str__(self) -> str:
        """Вернуть человекочитаемое название.

        Returns:
            Строка на русском.
        """
        names: dict[NotificationType, str] = {
            NotificationType.LIKE: "лайк",
            NotificationType.COMMENT: "комментарий",
            NotificationType.FRIEND_REQUEST: "заявка в друзья",
            NotificationType.MESSAGE: "сообщение",
            NotificationType.MENTION: "упоминание",
            NotificationType.SYSTEM: "системное",
        }
        return names[self]
