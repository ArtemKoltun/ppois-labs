"""
Push-уведомление.

Module: social.domain.notifications.push_notification
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from social.domain.notifications.notification import Notification

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class PushNotification(Notification):
    """Push-уведомление на устройство.

    Attributes:
        _device_token: Токен устройства.
        _is_delivered: Доставлено ли.
    """

    def __init__(
        self,
        notification: Notification,
        device_token: str,
    ) -> None:
        """Создать push.

        Args:
            notification: Базовое уведомление.
            device_token: Токен устройства.
        """
        super().__init__(
            recipient=notification.recipient,
            notification_type=notification.notification_type,
            text=notification.text,
            priority=notification.priority,
        )
        self._device_token: str = device_token
        self._is_delivered: bool = False

    @property
    def device_token(self) -> str:
        """Токен.

        Returns:
            Строка.
        """
        return self._device_token

    def deliver(self) -> None:
        """Доставить.

        Returns:
            Ничего не возвращает.
        """
        self._is_delivered = True

    def is_delivered(self) -> bool:
        """Проверить доставку.

        Returns:
            ``True``, если доставлено.
        """
        return self._is_delivered

    def has_token(self) -> bool:
        """Проверить наличие токена.

        Returns:
            ``True``, если токен задан.
        """
        return bool(self._device_token)
