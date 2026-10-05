"""
Тесты исключений.

Module: tests.common.exceptions.test_exceptions
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.exceptions import (
    AccountBlockedError,
    AdCampaignError,
    ContentModerationError,
    FriendshipError,
    InvalidCredentialsError,
    InvalidPostError,
    InvalidUserError,
    MessageDeliveryError,
    NotificationError,
    PrivacyViolationError,
    SocialNetworkError,
    UserNotFoundError,
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_ALL_EXCEPTIONS: list[type[SocialNetworkError]] = [
    AccountBlockedError,
    AdCampaignError,
    ContentModerationError,
    FriendshipError,
    InvalidCredentialsError,
    InvalidPostError,
    InvalidUserError,
    MessageDeliveryError,
    NotificationError,
    PrivacyViolationError,
    UserNotFoundError,
]
"""Все конкретные исключения."""


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestSocialNetworkError:
    """Проверки базового исключения."""

    def test_inherits_exception(self) -> None:
        """Наследуется от Exception."""
        assert issubclass(SocialNetworkError, Exception)

    def test_message(self) -> None:
        """Сообщение сохраняется."""
        exc: SocialNetworkError = SocialNetworkError("ошибка")
        assert exc.message == "ошибка"
        assert str(exc) == "ошибка"


class TestConcreteExceptions:
    """Проверки всех конкретных исключений."""

    @pytest.mark.parametrize("exc_class", _ALL_EXCEPTIONS)
    def test_inherits_base(
        self,
        exc_class: type[SocialNetworkError],
    ) -> None:
        """Наследуется от SocialNetworkError.

        Args:
            exc_class: Класс исключения.
        """
        assert issubclass(exc_class, SocialNetworkError)

    @pytest.mark.parametrize("exc_class", _ALL_EXCEPTIONS)
    def test_raises_with_message(
        self,
        exc_class: type[SocialNetworkError],
    ) -> None:
        """Можно поднять с сообщением.

        Args:
            exc_class: Класс исключения.
        """
        with pytest.raises(exc_class) as exc_info:
            raise exc_class("тестовое сообщение")
        assert "тестовое сообщение" in str(exc_info.value)
