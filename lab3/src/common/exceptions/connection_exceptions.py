"""
Исключения, связанные со связями.

Module: common.exceptions.connection_exceptions
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.exceptions.base import SocialNetworkError

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class FriendshipError(SocialNetworkError):
    """Ошибка при работе с дружбой."""


class MessageDeliveryError(SocialNetworkError):
    """Ошибка доставки сообщения."""


class NotificationError(SocialNetworkError):
    """Ошибка при работе с уведомлениями."""


class AdCampaignError(SocialNetworkError):
    """Ошибка рекламной кампании."""
