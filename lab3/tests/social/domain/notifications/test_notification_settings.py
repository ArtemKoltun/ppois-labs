"""
Тесты класса NotificationSettings.

Module: tests.social.domain.notifications.test_notification_settings
"""

from __future__ import annotations

from social.domain.notifications.notification_settings import (
    NotificationSettings,
)


class TestNotificationSettings:
    """Проверки класса NotificationSettings."""

    def test_creates_default(self) -> None:
        """Настройки создаются с дефолтами."""
        s: NotificationSettings = NotificationSettings("ivan")
        assert s.user == "ivan"

    def test_toggle_push(self) -> None:
        """toggle_push переключает."""
        s: NotificationSettings = NotificationSettings("ivan")
        s.toggle_push()
        assert not s._push_enabled

    def test_toggle_email(self) -> None:
        """toggle_email переключает."""
        s: NotificationSettings = NotificationSettings("ivan")
        s.toggle_email()
        assert not s._email_enabled

    def test_set_quiet_hours(self) -> None:
        """set_quiet_hours меняет час."""
        s: NotificationSettings = NotificationSettings("ivan")
        s.set_quiet_hours(20)
        assert s._quiet_hours_start == 20

    def test_is_in_quiet_hours(self) -> None:
        """is_in_quiet_hours проверяет час."""
        s: NotificationSettings = NotificationSettings(
            "ivan", quiet_hours_start=22
        )
        assert not s.is_in_quiet_hours(10)
        assert s.is_in_quiet_hours(23)

    def test_all_disabled(self) -> None:
        """all_disabled при двух выключенных."""
        s: NotificationSettings = NotificationSettings("ivan")
        assert not s.all_disabled()
        s.toggle_push()
        s.toggle_email()
        assert s.all_disabled()

    def test_equality(self) -> None:
        """Равные по пользователю."""
        a: NotificationSettings = NotificationSettings("ivan")
        b: NotificationSettings = NotificationSettings("ivan")
        assert a == b
        assert a != "not settings"

    def test_hash(self) -> None:
        """Хеш настроек."""
        a: NotificationSettings = NotificationSettings("ivan")
        b: NotificationSettings = NotificationSettings("ivan")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        s: NotificationSettings = NotificationSettings("ivan")
        assert "ivan" in str(s)

    def test_parse(self) -> None:
        """from_string разбирает настройки."""
        s: NotificationSettings = NotificationSettings.from_string(
            "ivan; true; false; 21"
        )
        assert s._quiet_hours_start == 21
