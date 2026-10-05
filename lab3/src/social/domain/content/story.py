"""
История (сторис).

Module: social.domain.content.story
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.exceptions.content_exceptions import InvalidPostError

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

DEFAULT_STORY_HOURS: int = 24
"""Время жизни истории по умолчанию в часах."""


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Story(Readable, Writable):
    """История, живущая ограниченное время.

    Attributes:
        _author: Автор.
        _media_url: Ссылка на медиа.
        _hours_to_live: Сколько часов живёт.
        _views_count: Число просмотров.
    """

    def __init__(
        self,
        author: str,
        media_url: str,
        hours_to_live: int = DEFAULT_STORY_HOURS,
    ) -> None:
        """Создать историю.

        Args:
            author: Автор.
            media_url: Медиа.
            hours_to_live: Время жизни.

        Raises:
            InvalidPostError: Если данные некорректны.
        """
        if not author or not media_url:
            raise InvalidPostError(
                "автор и медиа не могут быть пустыми"
            )
        if hours_to_live <= 0:
            raise InvalidPostError(
                "время жизни должно быть положительным"
            )
        self._author: str = author
        self._media_url: str = media_url
        self._hours_to_live: int = hours_to_live
        self._views_count: int = 0

    @classmethod
    def _parse(cls, text: str) -> Story:
        """Разобрать историю из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            author=parts[0],
            media_url=parts[1],
            hours_to_live=int(parts[2]) if len(parts) > 2 else 24,
        )

    @property
    def author(self) -> str:
        """Автор.

        Returns:
            Строка.
        """
        return self._author

    @property
    def media_url(self) -> str:
        """Медиа.

        Returns:
            Строка.
        """
        return self._media_url

    @property
    def views_count(self) -> int:
        """Число просмотров.

        Returns:
            Целое число.
        """
        return self._views_count

    def view(self) -> None:
        """Отметить просмотр.

        Returns:
            Ничего не возвращает.
        """
        self._views_count += 1

    def is_expired(self, hours_passed: int) -> bool:
        """Проверить, истёк ли срок.

        Args:
            hours_passed: Сколько часов прошло.

        Returns:
            ``True``, если срок истёк.
        """
        return hours_passed >= self._hours_to_live

    def __eq__(self, other: object) -> bool:
        """Сравнить две истории.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении автора и медиа.
        """
        if not isinstance(other, Story):
            return NotImplemented
        return (
            self._author == other._author
            and self._media_url == other._media_url
        )

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash((self._author, self._media_url))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._author}; {self._media_url}; "
            f"{self._hours_to_live}"
        )
