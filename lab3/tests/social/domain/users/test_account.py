"""
Тесты класса Account.

Module: tests.social.domain.users.test_account
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.exceptions import InvalidCredentialsError, InvalidUserError
from social.domain.users.account import Account

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_LONG_HASH: str = "a" * 20
"""Длинный хеш пароля."""


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestAccount:
    """Проверки класса Account."""

    def test_creates(self) -> None:
        """Аккаунт создаётся."""
        a: Account = Account(login="ivan", password_hash=_LONG_HASH)
        assert a.login == "ivan"
        assert not a.is_verified
        assert not a.two_factor_enabled

    def test_empty_login_raises(self) -> None:
        """Пустой логин недопустим."""
        with pytest.raises(InvalidUserError):
            Account(login="", password_hash=_LONG_HASH)

    def test_verify(self) -> None:
        """verify подтверждает email."""
        a: Account = Account(login="ivan", password_hash=_LONG_HASH)
        a.verify()
        assert a.is_verified

    def test_enable_disable_two_factor(self) -> None:
        """Включение и выключение 2FA."""
        a: Account = Account(login="ivan", password_hash=_LONG_HASH)
        a.enable_two_factor()
        assert a.two_factor_enabled
        a.disable_two_factor()
        assert not a.two_factor_enabled

    def test_change_password(self) -> None:
        """Смена пароля."""
        a: Account = Account(login="ivan", password_hash=_LONG_HASH)
        a.change_password("b" * 20)
        assert a.check_password("b" * 20)

    def test_change_password_short_raises(self) -> None:
        """Короткий пароль недопустим."""
        a: Account = Account(login="ivan", password_hash=_LONG_HASH)
        with pytest.raises(InvalidCredentialsError):
            a.change_password("short")

    def test_check_password(self) -> None:
        """Проверка пароля."""
        a: Account = Account(login="ivan", password_hash=_LONG_HASH)
        assert a.check_password(_LONG_HASH)
        assert not a.check_password("other")

    def test_is_secure(self) -> None:
        """is_secure требует 2FA и verified."""
        a: Account = Account(login="ivan", password_hash=_LONG_HASH)
        assert not a.is_secure()
        a.verify()
        assert not a.is_secure()
        a.enable_two_factor()
        assert a.is_secure()

    def test_equality(self) -> None:
        """Равные по логину."""
        a: Account = Account(login="ivan", password_hash=_LONG_HASH)
        b: Account = Account(login="ivan", password_hash="other")
        assert a == b
        assert a != "not account"

    def test_hash(self) -> None:
        """Хеш по логину."""
        a: Account = Account(login="ivan", password_hash=_LONG_HASH)
        b: Account = Account(login="ivan", password_hash="other")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        a: Account = Account(login="ivan", password_hash=_LONG_HASH)
        assert "ivan" in str(a)

    def test_parse(self) -> None:
        """from_string разбирает аккаунт."""
        a: Account = Account.from_string("ivan; hash; true")
        assert a.login == "ivan"
        assert a.is_verified
