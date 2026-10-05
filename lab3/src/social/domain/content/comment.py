"""
Комментарий к посту.

Module: social.domain.content.comment
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

class Comment(Readable, Writable):
    """Комментарий под постом.

    Attributes:
        _author: Автор.
        _post_id: Идентификатор поста.
        _text: Текст.
        _likes_count: Число лайков.
    """

    def __init__(
        self,
        author: str,
        post_id: str,
        text: str,
    ) -> None:
        """Создать комментарий.

        Args:
            author: Автор.
            post_id: Пост.
            text: Текст.

        Raises:
            InvalidPostError: Если данные некорректны.
        """
        if not author or not post_id or not text:
            raise InvalidPostError("поля не могут быть пустыми")
        self._author: str = author
        self._post_id: str = post_id
        self._text: str = text
        self._likes_count: int = 0

    @classmethod
    def _parse(cls, text: str) -> Comment:
        """Разобрать комментарий из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            author=parts[0],
            post_id=parts[1],
            text=parts[2],
        )

    @property
    def author(self) -> str:
        """Автор.

        Returns:
            Строка.
        """
        return self._author

    @property
    def post_id(self) -> str:
        """Идентификатор поста.

        Returns:
            Строка.
        """
        return self._post_id

    @property
    def text(self) -> str:
        """Текст.

        Returns:
            Строка.
        """
        return self._text

    def like(self) -> None:
        """Поставить лайк.

        Returns:
            Ничего не возвращает.
        """
        self._likes_count += 1

    def unlike(self) -> None:
        """Убрать лайк.

        Returns:
            Ничего не возвращает.
        """
        self._likes_count = max(0, self._likes_count - 1)

    def length(self) -> int:
        """Длина текста.

        Returns:
            Число символов.
        """
        return len(self._text)

    def __eq__(self, other: object) -> bool:
        """Сравнить два комментария.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении автора и текста.
        """
        if not isinstance(other, Comment):
            return NotImplemented
        return (
            self._author == other._author
            and self._text == other._text
        )

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash((self._author, self._text))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return f"{self._author}; {self._post_id}; {self._text}"
