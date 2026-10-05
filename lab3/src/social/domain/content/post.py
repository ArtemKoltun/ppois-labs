"""
Пост в социальной сети.

Module: social.domain.content.post
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.constants import MAX_POST_LENGTH
from common.enums.post_visibility import PostVisibility
from common.exceptions.content_exceptions import InvalidPostError

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Post(Readable, Writable):
    """Пост пользователя.

    Attributes:
        _author: Имя автора.
        _text: Текст поста.
        _visibility: Видимость.
        _likes_count: Число лайков.
        _comments_count: Число комментариев.
        _is_edited: Редактировался ли.
    """

    def __init__(
        self,
        author: str,
        text: str,
        visibility: PostVisibility = PostVisibility.PUBLIC,
    ) -> None:
        """Создать пост.

        Args:
            author: Имя автора.
            text: Текст поста.
            visibility: Видимость.

        Raises:
            InvalidPostError: Если текст некорректен.
        """
        if not author:
            raise InvalidPostError("автор не может быть пустым")
        if not text:
            raise InvalidPostError("текст не может быть пустым")
        if len(text) > MAX_POST_LENGTH:
            raise InvalidPostError(
                f"текст не должен превышать {MAX_POST_LENGTH} символов"
            )
        self._author: str = author
        self._text: str = text
        self._visibility: PostVisibility = visibility
        self._likes_count: int = 0
        self._comments_count: int = 0
        self._is_edited: bool = False

    @classmethod
    def _parse(cls, text: str) -> Post:
        """Разобрать пост из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            author=parts[0],
            text=parts[1],
            visibility=PostVisibility(parts[2]),
        )

    @property
    def author(self) -> str:
        """Автор.

        Returns:
            Строка.
        """
        return self._author

    @property
    def text(self) -> str:
        """Текст поста.

        Returns:
            Строка.
        """
        return self._text

    @property
    def visibility(self) -> PostVisibility:
        """Видимость.

        Returns:
            Элемент перечисления.
        """
        return self._visibility

    @property
    def likes_count(self) -> int:
        """Число лайков.

        Returns:
            Целое число.
        """
        return self._likes_count

    @property
    def comments_count(self) -> int:
        """Число комментариев.

        Returns:
            Целое число.
        """
        return self._comments_count

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

    def add_comment(self) -> None:
        """Увеличить счётчик комментариев.

        Returns:
            Ничего не возвращает.
        """
        self._comments_count += 1

    def edit(self, new_text: str) -> None:
        """Отредактировать пост.

        Args:
            new_text: Новый текст.

        Returns:
            Ничего не возвращает.

        Raises:
            InvalidPostError: Если текст некорректен.
        """
        if not new_text:
            raise InvalidPostError("текст не может быть пустым")
        if len(new_text) > MAX_POST_LENGTH:
            raise InvalidPostError(
                f"текст не должен превышать {MAX_POST_LENGTH} символов"
            )
        self._text = new_text
        self._is_edited = True

    def change_visibility(self, visibility: PostVisibility) -> None:
        """Изменить видимость.

        Args:
            visibility: Новая видимость.

        Returns:
            Ничего не возвращает.
        """
        self._visibility = visibility

    def is_edited(self) -> bool:
        """Проверить, редактировался ли.

        Returns:
            ``True``, если редактировался.
        """
        return self._is_edited

    def is_popular(self) -> bool:
        """Проверить популярность.

        Returns:
            ``True``, если лайков больше 100.
        """
        return self._likes_count > 100

    def __eq__(self, other: object) -> bool:
        """Сравнить два поста.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении автора и текста.
        """
        if not isinstance(other, Post):
            return NotImplemented
        return (
            self._author == other._author
            and self._text == other._text
        )

    def __hash__(self) -> int:
        """Вернуть хеш поста.

        Returns:
            Целое число.
        """
        return hash((self._author, self._text))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._author}; {self._text}; "
            f"{self._visibility.value}"
        )
