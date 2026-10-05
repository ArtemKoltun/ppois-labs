"""
Email-уведомление.

Module: social.domain.notifications.email_notification
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from social.domain.notifications.notification import Notification

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class EmailNotification(Notification):
    """Email-уведомление.

    Attributes:
        _email: Адрес получателя.
        _subject: Тема письма.
    """

    def __init__(
        self,
        notification: Notification,
        email: str,
        subject: str = "",
    ) -> None:
        """Создать email-уведомление.

        Args:
            notification: Базовое уведомление.
            email: Адрес.
            subject: Тема.
        """
        super().__init__(
            recipient=notification.recipient,
            notification_type=notification.notification_type,
            text=notification.text,
            priority=notification.priority,
        )
        self._email: str = email
        self._subject: str = subject or "Уведомление"

    @property
    def email(self) -> str:
        """Адрес.

        Returns:
            Строка.
        """
        return self._email

    @property
    def subject(self) -> str:
        """Тема.

        Returns:
            Строка.
        """
        return self._subject

    def set_subject(self, subject: str) -> None:
        """Сменить тему.

        Args:
            subject: Новая тема.

        Returns:
            Ничего не возвращает.
        """
        self._subject = subject

    def is_valid_email(self) -> bool:
        """Проверить адрес.

        Returns:
            ``True``, если адрес похож на корректный.
        """
        return "@" in self._email and "." in self._email
