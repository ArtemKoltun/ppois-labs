"""
Тесты класса EmailNotification.

Module: tests.social.domain.notifications.test_email_notification
"""

from __future__ import annotations

from common.enums.notification_type import NotificationType
from social.domain.notifications.email_notification import (
    EmailNotification,
)
from social.domain.notifications.notification import Notification


class TestEmailNotification:
    """Проверки класса EmailNotification."""

    def test_creates(self) -> None:
        """Email создаётся."""
        base: Notification = Notification("petr", NotificationType.LIKE)
        e: EmailNotification = EmailNotification(
            base, "petr@mail.ru"
        )
        assert e.email == "petr@mail.ru"
        assert e.subject == "Уведомление"

    def test_set_subject(self) -> None:
        """set_subject меняет тему."""
        base: Notification = Notification("petr", NotificationType.LIKE)
        e: EmailNotification = EmailNotification(base, "p@m.ru")
        e.set_subject("Новая тема")
        assert e.subject == "Новая тема"

    def test_is_valid_email(self) -> None:
        """is_valid_email проверяет формат."""
        base: Notification = Notification("petr", NotificationType.LIKE)
        good: EmailNotification = EmailNotification(base, "a@b.c")
        bad: EmailNotification = EmailNotification(base, "not-email")
        assert good.is_valid_email()
        assert not bad.is_valid_email()
