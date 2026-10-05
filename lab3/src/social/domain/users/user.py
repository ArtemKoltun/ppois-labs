"""
Пользователь социальной сети.

Module: social.domain.users.user
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.constants import MAX_NAME_LENGTH, MIN_NAME_LENGTH
from common.enums.user_role import UserRole
from common.exceptions.user_exceptions import AccountBlockedError, InvalidUserError

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class User(Readable, Writable):
    """Пользователь социальной сети.

    Attributes:
        _username: Уникальное имя пользователя.
        _email: Электронная почта.
        _display_name: Отображаемое имя.
        _role: Роль в системе.
        _is_active: Активен ли аккаунт.
        _is_blocked: Заблокирован ли.
    """

    # -----------------------------------------------------------------------
    # Constructors
    # -----------------------------------------------------------------------

    def __init__(
        self,
        username: str,
        email: str,
        display_name: str = "",
        role: UserRole = UserRole.USER,
    ) -> None:
        """Создать пользователя.

        Args:
            username: Уникальное имя.
            email: Электронная почта.
            display_name: Отображаемое имя.
            role: Роль.

        Raises:
            InvalidUserError: Если данные некорректны.
        """
        self._validate_username(username)
        self._validate_email(email)
        self._username: str = username
        self._email: str = email
        self._display_name: str = display_name or username
        self._role: UserRole = role
        self._is_active: bool = True
        self._is_blocked: bool = False

    @classmethod
    def _parse(cls, text: str) -> User:
        """Разобрать пользователя из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            username=parts[0],
            email=parts[1],
            display_name=parts[2],
            role=UserRole(parts[3]),
        )

    # -----------------------------------------------------------------------
    # Private methods
    # -----------------------------------------------------------------------

    @staticmethod
    def _validate_username(username: str) -> None:
        """Проверить имя пользователя.

        Args:
            username: Проверяемое имя.

        Raises:
            InvalidUserError: Если имя некорректно.
        """
        if not MIN_NAME_LENGTH <= len(username) <= MAX_NAME_LENGTH:
            raise InvalidUserError(
                f"длина имени должна быть от {MIN_NAME_LENGTH} "
                f"до {MAX_NAME_LENGTH}"
            )
        if not username.replace("_", "").isalnum():
            raise InvalidUserError(
                "имя может содержать только буквы, цифры и _"
            )

    @staticmethod
    def _validate_email(email: str) -> None:
        """Проверить email.

        Args:
            email: Проверяемый email.

        Raises:
            InvalidUserError: Если email некорректен.
        """
        if "@" not in email or "." not in email:
            raise InvalidUserError(f"некорректный email: {email!r}")

    # -----------------------------------------------------------------------
    # Properties
    # -----------------------------------------------------------------------

    @property
    def username(self) -> str:
        """Уникальное имя.

        Returns:
            Строка.
        """
        return self._username

    @property
    def email(self) -> str:
        """Электронная почта.

        Returns:
            Строка.
        """
        return self._email

    @property
    def display_name(self) -> str:
        """Отображаемое имя.

        Returns:
            Строка.
        """
        return self._display_name

    @property
    def role(self) -> UserRole:
        """Роль в системе.

        Returns:
            Элемент перечисления.
        """
        return self._role

    @property
    def is_active(self) -> bool:
        """Активен ли аккаунт.

        Returns:
            ``True``, если аккаунт активен.
        """
        return self._is_active

    @property
    def is_blocked(self) -> bool:
        """Заблокирован ли аккаунт.

        Returns:
            ``True``, если заблокирован.
        """
        return self._is_blocked

    # -----------------------------------------------------------------------
    # Public methods
    # -----------------------------------------------------------------------

    def block(self) -> None:
        """Заблокировать аккаунт.

        Returns:
            Ничего не возвращает.
        """
        self._is_blocked = True

    def unblock(self) -> None:
        """Разблокировать аккаунт.

        Returns:
            Ничего не возвращает.
        """
        self._is_blocked = False

    def deactivate(self) -> None:
        """Деактивировать аккаунт.

        Returns:
            Ничего не возвращает.
        """
        self._is_active = False

    def activate(self) -> None:
        """Активировать аккаунт.

        Returns:
            Ничего не возвращает.
        """
        self._is_active = True

    def change_display_name(self, name: str) -> None:
        """Сменить отображаемое имя.

        Args:
            name: Новое имя.

        Returns:
            Ничего не возвращает.

        Raises:
            InvalidUserError: Если имя пустое.
        """
        if not name:
            raise InvalidUserError("имя не может быть пустым")
        self._display_name = name

    def promote(self, role: UserRole) -> None:
        """Назначить новую роль.

        Args:
            role: Новая роль.

        Returns:
            Ничего не возвращает.
        """
        self._role = role

    def ensure_active(self) -> None:
        """Проверить, что аккаунт активен и не заблокирован.

        Returns:
            Ничего не возвращает.

        Raises:
            AccountBlockedError: Если аккаунт заблокирован или деактивирован.
        """
        if self._is_blocked:
            raise AccountBlockedError(
                f"аккаунт {self._username} заблокирован"
            )
        if not self._is_active:
            raise AccountBlockedError(
                f"аккаунт {self._username} деактивирован"
            )

    def is_admin(self) -> bool:
        """Проверить, администратор ли.

        Returns:
            ``True``, если роль — ADMIN.
        """
        return self._role is UserRole.ADMIN

    def is_moderator(self) -> bool:
        """Проверить, модератор ли.

        Returns:
            ``True``, если роль — MODERATOR или ADMIN.
        """
        return self._role in (UserRole.MODERATOR, UserRole.ADMIN)

    # -----------------------------------------------------------------------
    # Magic methods
    # -----------------------------------------------------------------------

    def __eq__(self, other: object) -> bool:
        """Сравнить двух пользователей.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении username.
        """
        if not isinstance(other, User):
            return NotImplemented
        return self._username == other._username

    def __hash__(self) -> int:
        """Вернуть хеш пользователя.

        Returns:
            Целое число.
        """
        return hash(self._username)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._username}; {self._email}; "
            f"{self._display_name}; {self._role.value}"
        )
