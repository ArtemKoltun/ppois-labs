"""
Тесты класса User.

Module: tests.social.domain.users.test_user
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.enums.user_role import UserRole
from common.exceptions import AccountBlockedError, InvalidUserError
from social.domain.users.user import User

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestUser:
    """Проверки класса User."""

    def test_creates(self, user: User) -> None:
        """Пользователь создаётся.

        Args:
            user: Фикстура пользователя.
        """
        assert user.username == "ivan"
        assert user.email == "ivan@mail.ru"
        assert user.display_name == "Иван"
        assert user.role is UserRole.USER
        assert user.is_active
        assert not user.is_blocked

    def test_empty_username_raises(self) -> None:
        """Пустое имя недопустимо."""
        with pytest.raises(InvalidUserError):
            User(username="", email="x@y.z")

    def test_bad_username_raises(self) -> None:
        """Неалфанумерическое имя недопустимо."""
        with pytest.raises(InvalidUserError):
            User(username="bad name!", email="x@y.z")

    def test_bad_email_raises(self) -> None:
        """Некорректный email недопустим."""
        with pytest.raises(InvalidUserError):
            User(username="ivan", email="not-email")

    def test_display_name_default(self) -> None:
        """Если display_name не задан — берётся username."""
        u: User = User(username="ivan", email="ivan@mail.ru")
        assert u.display_name == "ivan"

    def test_change_display_name(self, user: User) -> None:
        """change_display_name меняет имя.

        Args:
            user: Фикстура пользователя.
        """
        user.change_display_name("Иван Иванов")
        assert user.display_name == "Иван Иванов"

    def test_change_display_name_empty_raises(
        self,
        user: User,
    ) -> None:
        """Пустое новое имя недопустимо.

        Args:
            user: Фикстура пользователя.
        """
        with pytest.raises(InvalidUserError):
            user.change_display_name("")

    def test_block_unblock(self, user: User) -> None:
        """Блокировка и разблокировка.

        Args:
            user: Фикстура пользователя.
        """
        user.block()
        assert user.is_blocked
        user.unblock()
        assert not user.is_blocked

    def test_deactivate_activate(self, user: User) -> None:
        """Деактивация и активация.

        Args:
            user: Фикстура пользователя.
        """
        user.deactivate()
        assert not user.is_active
        user.activate()
        assert user.is_active

    def test_promote(self, user: User) -> None:
        """promote меняет роль.

        Args:
            user: Фикстура пользователя.
        """
        user.promote(UserRole.MODERATOR)
        assert user.role is UserRole.MODERATOR

    def test_ensure_active_ok(self, user: User) -> None:
        """Активный не падает.

        Args:
            user: Фикстура пользователя.
        """
        user.ensure_active()

    def test_ensure_active_blocked_raises(self, user: User) -> None:
        """Заблокированный падает.

        Args:
            user: Фикстура пользователя.
        """
        user.block()
        with pytest.raises(AccountBlockedError):
            user.ensure_active()

    def test_ensure_active_deactivated_raises(
        self,
        user: User,
    ) -> None:
        """Деактивированный падает.

        Args:
            user: Фикстура пользователя.
        """
        user.deactivate()
        with pytest.raises(AccountBlockedError):
            user.ensure_active()

    def test_is_admin(self, user: User, admin: User) -> None:
        """is_admin проверяет роль.

        Args:
            user: Фикстура пользователя.
            admin: Фикстура администратора.
        """
        assert not user.is_admin()
        assert admin.is_admin()

    def test_is_moderator(self, user: User, admin: User) -> None:
        """is_moderator для модератора и админа.

        Args:
            user: Фикстура пользователя.
            admin: Фикстура администратора.
        """
        assert not user.is_moderator()
        assert admin.is_moderator()
        user.promote(UserRole.MODERATOR)
        assert user.is_moderator()

    def test_equality(self, user: User) -> None:
        """Равные по username.

        Args:
            user: Фикстура пользователя.
        """
        other: User = User(
            username="ivan",
            email="other@mail.ru",
            display_name="Другой",
        )
        assert user == other
        assert user != "not user"

    def test_hash(self, user: User) -> None:
        """Хеш по username.

        Args:
            user: Фикстура пользователя.
        """
        other: User = User(
            username="ivan", email="x@y.z"
        )
        assert hash(user) == hash(other)

    def test_str(self, user: User) -> None:
        """str возвращает поля.

        Args:
            user: Фикстура пользователя.
        """
        text: str = str(user)
        assert "ivan" in text
        assert "ivan@mail.ru" in text

    def test_parse(self) -> None:
        """from_string разбирает пользователя."""
        u: User = User.from_string("ivan; ivan@mail.ru; Иван; user")
        assert u.username == "ivan"
        assert u.role is UserRole.USER
