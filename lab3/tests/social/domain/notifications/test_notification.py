"""
Тесты класса Notification.

Module: tests.social.domain.notifications.test_notification
"""

from __future__ import annotations

import pytest

from common.enums.notification_type import NotificationType
from common.exceptions import NotificationError
from social.domain.notifications.notification import Notification


class TestNotification:
    """Проверки класса Notification."""

    def test_creates(self) -> None:
        """Уведомление создаётся."""
        n: Notification = Notification(
            "petr", NotificationType.LIKE, "лайк"
        )
        assert n.recipient == "petr"
        assert n.notification_type is NotificationType.LIKE
        assert n.text == "лайк"
        assert n.priority == 3
        assert not n.is_read

    def test_empty_recipient_raises(self) -> None:
        """Пустой получатель недопустим."""
        with pytest.raises(NotificationError):
            Notification("", NotificationType.LIKE)

    def test_bad_priority_raises(self) -> None:
        """Плохой приоритет недопустим."""
        with pytest.raises(NotificationError):
            Notification("petr", NotificationType.LIKE, priority=10)

    def test_mark_read(self) -> None:
        """mark_read отмечает."""
        n: Notification = Notification("petr", NotificationType.LIKE)
        n.mark_read()
        assert n.is_read

    def test_raise_priority(self) -> None:
        """raise_priority увеличивает до 5."""
        n: Notification = Notification("p", NotificationType.LIKE)
        n.raise_priority()
        n.raise_priority()
        n.raise_priority()
        assert n.priority == 5

    def test_is_urgent(self) -> None:
        """is_urgent приоритет >= 4."""
        urgent: Notification = Notification(
            "p", NotificationType.LIKE, priority=5
        )
        normal: Notification = Notification(
            "p", NotificationType.LIKE, priority=2
        )
        assert urgent.is_urgent()
        assert not normal.is_urgent()

    def test_equality(self) -> None:
        """Равные по полям."""
        a: Notification = Notification("p", NotificationType.LIKE, "x")
        b: Notification = Notification("p", NotificationType.LIKE, "x")
        assert a == b
        assert a != "not notification"

    def test_hash(self) -> None:
        """Хеш уведомления."""
        a: Notification = Notification("p", NotificationType.LIKE, "x")
        b: Notification = Notification("p", NotificationType.LIKE, "x")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        n: Notification = Notification(
            "petr", NotificationType.LIKE, "лайк"
        )
        text: str = str(n)
        assert "petr" in text
        assert "like" in text

    def test_parse(self) -> None:
        """from_string разбирает уведомление."""
        n: Notification = Notification.from_string(
            "petr; like; лайк; 4"
        )
        assert n.recipient == "petr"
        assert n.priority == 4
