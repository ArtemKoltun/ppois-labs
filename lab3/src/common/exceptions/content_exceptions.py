"""
Исключения, связанные с контентом.

Module: common.exceptions.content_exceptions
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.exceptions.base import SocialNetworkError

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class InvalidPostError(SocialNetworkError):
    """Некорректный пост."""


class ContentModerationError(SocialNetworkError):
    """Ошибка модерации контента."""


class PrivacyViolationError(SocialNetworkError):
    """Нарушение приватности."""
