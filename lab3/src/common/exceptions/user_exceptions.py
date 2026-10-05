"""
Исключения, связанные с пользователями.

Module: common.exceptions.user_exceptions
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.exceptions.base import SocialNetworkError

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class InvalidUserError(SocialNetworkError):
    """Некорректные данные пользователя."""


class UserNotFoundError(SocialNetworkError):
    """Пользователь не найден."""


class InvalidCredentialsError(SocialNetworkError):
    """Неверные логин или пароль."""


class AccountBlockedError(SocialNetworkError):
    """Аккаунт заблокирован."""
