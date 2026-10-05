"""
Настройки пользователя.

Module: social.domain.users.user_settings
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.enums.post_visibility import PostVisibility

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class UserSettings(Readable, Writable):
    """Настройки пользователя.

    Attributes:
        _default_visibility: Видимость постов по умолчанию.
        _show_email: Показывать email в профиле.
        _allow_messages: Разрешить личные сообщения.
        _language: Язык интерфейса.
    """

    # -----------------------------------------------------------------------
    # Constructors
    # -----------------------------------------------------------------------

    def __init__(
        self,
        default_visibility: PostVisibility = PostVisibility.PUBLIC,
        show_email: bool = False,
        allow_messages: bool = True,
        language: str = "ru",
    ) -> None:
        """Создать настройки.

        Args:
            default_visibility: Видимость постов.
            show_email: Показывать ли email.
            allow_messages: Разрешить ли сообщения.
            language: Язык.
        """
        self._default_visibility: PostVisibility = default_visibility
        self._show_email: bool = show_email
        self._allow_messages: bool = allow_messages
        self._language: str = language

    @classmethod
    def _parse(cls, text: str) -> UserSettings:
        """Разобрать настройки из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            default_visibility=PostVisibility(parts[0]),
            show_email=parts[1].lower() == "true",
            allow_messages=parts[2].lower() == "true",
            language=parts[3],
        )

    # -----------------------------------------------------------------------
    # Properties
    # -----------------------------------------------------------------------

    @property
    def default_visibility(self) -> PostVisibility:
        """Видимость постов по умолчанию.

        Returns:
            Элемент перечисления.
        """
        return self._default_visibility

    @property
    def show_email(self) -> bool:
        """Показывать email.

        Returns:
            ``True``, если показывать.
        """
        return self._show_email

    @property
    def allow_messages(self) -> bool:
        """Разрешить сообщения.

        Returns:
            ``True``, если разрешено.
        """
        return self._allow_messages

    @property
    def language(self) -> str:
        """Язык интерфейса.

        Returns:
            Строка.
        """
        return self._language

    # -----------------------------------------------------------------------
    # Public methods
    # -----------------------------------------------------------------------

    def set_visibility(self, visibility: PostVisibility) -> None:
        """Изменить видимость по умолчанию.

        Args:
            visibility: Новая видимость.

        Returns:
            Ничего не возвращает.
        """
        self._default_visibility = visibility

    def toggle_email_visibility(self) -> None:
        """Переключить видимость email.

        Returns:
            Ничего не возвращает.
        """
        self._show_email = not self._show_email

    def toggle_messages(self) -> None:
        """Переключить приём сообщений.

        Returns:
            Ничего не возвращает.
        """
        self._allow_messages = not self._allow_messages

    def set_language(self, language: str) -> None:
        """Изменить язык.

        Args:
            language: Код языка.

        Returns:
            Ничего не возвращает.
        """
        self._language = language

    def is_open(self) -> bool:
        """Проверить открытость профиля.

        Returns:
            ``True``, если разрешены сообщения и email виден.
        """
        return self._allow_messages and self._show_email

    # -----------------------------------------------------------------------
    # Magic methods
    # -----------------------------------------------------------------------

    def __eq__(self, other: object) -> bool:
        """Сравнить две настройки.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении языка и видимости.
        """
        if not isinstance(other, UserSettings):
            return NotImplemented
        return (
            self._default_visibility == other._default_visibility
            and self._language == other._language
        )

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash((self._default_visibility, self._language))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._default_visibility.value}; "
            f"{self._show_email}; "
            f"{self._allow_messages}; {self._language}"
        )
