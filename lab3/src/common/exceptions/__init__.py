"""
Все исключения предметной области.

Module: common.exceptions
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.exceptions.base import SocialNetworkError
from common.exceptions.connection_exceptions import (
    AdCampaignError,
    FriendshipError,
    MessageDeliveryError,
    NotificationError,
)
from common.exceptions.content_exceptions import (
    ContentModerationError,
    InvalidPostError,
    PrivacyViolationError,
)
from common.exceptions.user_exceptions import (
    AccountBlockedError,
    InvalidCredentialsError,
    InvalidUserError,
    UserNotFoundError,
)

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

__all__ = [
    "AccountBlockedError",
    "AdCampaignError",
    "ContentModerationError",
    "FriendshipError",
    "InvalidCredentialsError",
    "InvalidPostError",
    "InvalidUserError",
    "MessageDeliveryError",
    "NotificationError",
    "PrivacyViolationError",
    "SocialNetworkError",
    "UserNotFoundError",
]
