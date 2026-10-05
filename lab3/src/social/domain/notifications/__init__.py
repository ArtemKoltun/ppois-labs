"""
Доменные классы уведомлений.

Module: social.domain.notifications
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from social.domain.notifications.email_notification import (
    EmailNotification,
)
from social.domain.notifications.notification import Notification
from social.domain.notifications.notification_settings import (
    NotificationSettings,
)
from social.domain.notifications.push_notification import (
    PushNotification,
)

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

__all__ = [
    "EmailNotification",
    "Notification",
    "NotificationSettings",
    "PushNotification",
]
