"""
Хэштег.

Module: social.domain.content.hashtag
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.exceptions.content_exceptions import InvalidPostError

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Hashtag(Readable, Writable):
    """Хэштег.

    Attributes:
        _tag: Имя тега без #.
        _posts_count: Число постов.
        _is_trending: В тренде ли.
    """

    def __init__(self, tag: str) -> None:
        """Создать хэштег.

        Args:
            tag: Имя тега (без #).

        Raises:
            InvalidPostError: Если тег некорректен.
        """
        cleaned: str = tag.lstrip("#")
        if not cleaned:
            raise InvalidPostError("тег не может быть пустым")
        if not cleaned.isalnum():
            raise InvalidPostError(
                "тег может содержать только буквы и цифры"
            )
        self._tag: str = cleaned
        self._posts_count: int = 0
        self._is_trending: bool = False

    @classmethod
    def _parse(cls, text: str) -> Hashtag:
        """Разобрать хэштег из строки.

        Args:
            text: Имя тега.

        Returns:
            Новый экземпляр.
        """
        return cls(text.strip())

    @property
    def tag(self) -> str:
        """Имя тега.

        Returns:
            Строка.
        """
        return self._tag

    @property
    def posts_count(self) -> int:
        """Число постов.

        Returns:
            Целое число.
        """
        return self._posts_count

    def add_post(self) -> None:
        """Увеличить счётчик постов.

        Returns:
            Ничего не возвращает.
        """
        self._posts_count += 1
        if self._posts_count > 1000:
            self._is_trending = True

    def mark_trending(self) -> None:
        """Пометить как трендовый.

        Returns:
            Ничего не возвращает.
        """
        self._is_trending = True

    def is_trending(self) -> bool:
        """Проверить трендовость.

        Returns:
            ``True``, если в тренде.
        """
        return self._is_trending

    def full(self) -> str:
        """Вернуть тег с #.

        Returns:
            Строка.
        """
        return f"#{self._tag}"

    def __eq__(self, other: object) -> bool:
        """Сравнить два хэштега.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении тега.
        """
        if not isinstance(other, Hashtag):
            return NotImplemented
        return self._tag == other._tag

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._tag)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка.
        """
        return self._tag
