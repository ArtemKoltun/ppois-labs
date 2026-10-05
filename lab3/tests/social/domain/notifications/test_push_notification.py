"""
Тесты класса PushNotification.

Module: tests.social.domain.notifications.test_push_notification
"""

from __future__ import annotations

from common.enums.notification_type import NotificationType
from social.domain.notifications.notification import Notification
from social.domain.notifications.push_notification import (
    PushNotification,
)


class TestPushNotification:
    """Проверки класса PushNotification."""

    def test_creates(self) -> None:
        """Push создаётся."""
        base: Notification = Notification("petr", NotificationType.LIKE)
        p: PushNotification = PushNotification(base, "token123")
        assert p.device_token == "token123"
        assert not p.is_delivered()

    def test_deliver(self) -> None:
        """deliver отмечает доставку."""
        base: Notification = Notification("petr", NotificationType.LIKE)
        p: PushNotification = PushNotification(base, "token123")
        p.deliver()
        assert p.is_delivered()

    def test_has_token(self) -> None:
        """has_token проверяет токен."""
        base: Notification = Notification("petr", NotificationType.LIKE)
        p: PushNotification = PushNotification(base, "")
        assert not p.has_token()
