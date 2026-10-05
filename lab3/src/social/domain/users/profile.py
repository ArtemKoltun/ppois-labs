"""
Профиль пользователя.

Module: social.domain.users.profile
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.constants import MAX_BIO_LENGTH
from common.exceptions.user_exceptions import InvalidUserError

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Profile(Readable, Writable):
    """Профиль пользователя.

    Attributes:
        _bio: Описание.
        _avatar_url: Ссылка на аватар.
        _city: Город.
        _website: Сайт.
        _is_private: Закрытый ли профиль.
    """

    # -----------------------------------------------------------------------
    # Constructors
    # -----------------------------------------------------------------------

    def __init__(
        self,
        bio: str = "",
        avatar_url: str = "",
        city: str = "",
        website: str = "",
        is_private: bool = False,
    ) -> None:
        """Создать профиль.

        Args:
            bio: Описание.
            avatar_url: Аватар.
            city: Город.
            website: Сайт.
            is_private: Приватность.

        Raises:
            InvalidUserError: Если bio слишком длинное.
        """
        if len(bio) > MAX_BIO_LENGTH:
            raise InvalidUserError(
                f"описание не должно превышать {MAX_BIO_LENGTH} символов"
            )
        self._bio: str = bio
        self._avatar_url: str = avatar_url
        self._city: str = city
        self._website: str = website
        self._is_private: bool = is_private

    @classmethod
    def _parse(cls, text: str) -> Profile:
        """Разобрать профиль из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            bio=parts[0],
            avatar_url=parts[1],
            city=parts[2],
            website=parts[3],
            is_private=parts[4].lower() == "true",
        )

    # -----------------------------------------------------------------------
    # Properties
    # -----------------------------------------------------------------------

    @property
    def bio(self) -> str:
        """Описание профиля.

        Returns:
            Строка.
        """
        return self._bio

    @property
    def avatar_url(self) -> str:
        """Аватар.

        Returns:
            Строка.
        """
        return self._avatar_url

    @property
    def city(self) -> str:
        """Город.

        Returns:
            Строка.
        """
        return self._city

    @property
    def website(self) -> str:
        """Сайт.

        Returns:
            Строка.
        """
        return self._website

    @property
    def is_private(self) -> bool:
        """Приватность профиля.

        Returns:
            ``True``, если профиль закрыт.
        """
        return self._is_private

    # -----------------------------------------------------------------------
    # Public methods
    # -----------------------------------------------------------------------

    def update_bio(self, bio: str) -> None:
        """Обновить описание.

        Args:
            bio: Новое описание.

        Returns:
            Ничего не возвращает.

        Raises:
            InvalidUserError: Если bio слишком длинное.
        """
        if len(bio) > MAX_BIO_LENGTH:
            raise InvalidUserError(
                f"описание не должно превышать {MAX_BIO_LENGTH} символов"
            )
        self._bio = bio

    def set_avatar(self, url: str) -> None:
        """Установить аватар.

        Args:
            url: Ссылка на аватар.

        Returns:
            Ничего не возвращает.
        """
        self._avatar_url = url

    def set_private(self, is_private: bool) -> None:
        """Изменить приватность.

        Args:
            is_private: Новая приватность.

        Returns:
            Ничего не возвращает.
        """
        self._is_private = is_private

    def has_avatar(self) -> bool:
        """Проверить наличие аватара.

        Returns:
            ``True``, если аватар задан.
        """
        return bool(self._avatar_url)

    def is_complete(self) -> bool:
        """Проверить заполненность профиля.

        Returns:
            ``True``, если заполнены bio и city.
        """
        return bool(self._bio) and bool(self._city)

    # -----------------------------------------------------------------------
    # Magic methods
    # -----------------------------------------------------------------------

    def __eq__(self, other: object) -> bool:
        """Сравнить два профиля.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении bio и city.
        """
        if not isinstance(other, Profile):
            return NotImplemented
        return self._bio == other._bio and self._city == other._city

    def __hash__(self) -> int:
        """Вернуть хеш профиля.

        Returns:
            Целое число.
        """
        return hash((self._bio, self._city))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._bio}; {self._avatar_url}; "
            f"{self._city}; {self._website}; "
            f"{self._is_private}"
        )
