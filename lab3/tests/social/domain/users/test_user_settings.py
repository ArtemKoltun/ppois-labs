"""
Тесты класса UserSettings.

Module: tests.social.domain.users.test_user_settings
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.enums.post_visibility import PostVisibility
from social.domain.users.user_settings import UserSettings

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestUserSettings:
    """Проверки класса UserSettings."""

    def test_creates_default(self) -> None:
        """Настройки создаются с дефолтами."""
        s: UserSettings = UserSettings()
        assert s.default_visibility is PostVisibility.PUBLIC
        assert not s.show_email
        assert s.allow_messages
        assert s.language == "ru"

    def test_set_visibility(self) -> None:
        """set_visibility меняет видимость."""
        s: UserSettings = UserSettings()
        s.set_visibility(PostVisibility.FRIENDS)
        assert s.default_visibility is PostVisibility.FRIENDS

    def test_toggle_email_visibility(self) -> None:
        """toggle_email_visibility переключает."""
        s: UserSettings = UserSettings()
        s.toggle_email_visibility()
        assert s.show_email
        s.toggle_email_visibility()
        assert not s.show_email

    def test_toggle_messages(self) -> None:
        """toggle_messages переключает приём сообщений."""
        s: UserSettings = UserSettings()
        s.toggle_messages()
        assert not s.allow_messages

    def test_set_language(self) -> None:
        """set_language меняет язык."""
        s: UserSettings = UserSettings()
        s.set_language("en")
        assert s.language == "en"

    def test_is_open(self) -> None:
        """is_open требует оба канала."""
        s: UserSettings = UserSettings()
        assert not s.is_open()
        s.toggle_email_visibility()
        assert s.is_open()

    def test_equality(self) -> None:
        """Равные по видимости и языку."""
        a: UserSettings = UserSettings()
        b: UserSettings = UserSettings()
        assert a == b
        assert a != "not settings"

    def test_hash(self) -> None:
        """Хеш настроек."""
        a: UserSettings = UserSettings()
        b: UserSettings = UserSettings()
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        s: UserSettings = UserSettings()
        assert "public" in str(s)

    def test_parse(self) -> None:
        """from_string разбирает настройки."""
        s: UserSettings = UserSettings.from_string(
            "friends; true; false; en"
        )
        assert s.default_visibility is PostVisibility.FRIENDS
        assert s.show_email
        assert not s.allow_messages
        assert s.language == "en"
