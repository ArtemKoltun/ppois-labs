"""
Учётная запись пользователя.

Module: social.domain.users.account
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.constants import MIN_PASSWORD_LENGTH
from common.exceptions.user_exceptions import InvalidCredentialsError, InvalidUserError

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Account(Readable, Writable):
    """Учётная запись с логином и паролем.

    Attributes:
        _login: Логин.
        _password_hash: Хеш пароля.
        _is_verified: Подтверждён ли email.
        _two_factor_enabled: Включена ли 2FA.
    """

    # -----------------------------------------------------------------------
    # Constructors
    # -----------------------------------------------------------------------

    def __init__(
        self,
        login: str,
        password_hash: str,
        is_verified: bool = False,
    ) -> None:
        """Создать учётную запись.

        Args:
            login: Логин.
            password_hash: Хеш пароля.
            is_verified: Подтверждён ли email.

        Raises:
            InvalidUserError: Если логин пустой.
        """
        if not login:
            raise InvalidUserError("логин не может быть пустым")
        self._login: str = login
        self._password_hash: str = password_hash
        self._is_verified: bool = is_verified
        self._two_factor_enabled: bool = False

    @classmethod
    def _parse(cls, text: str) -> Account:
        """Разобрать аккаунт из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            login=parts[0],
            password_hash=parts[1],
            is_verified=parts[2].lower() == "true",
        )

    # -----------------------------------------------------------------------
    # Properties
    # -----------------------------------------------------------------------

    @property
    def login(self) -> str:
        """Логин.

        Returns:
            Строка.
        """
        return self._login

    @property
    def is_verified(self) -> bool:
        """Подтверждён ли email.

        Returns:
            ``True``, если подтверждён.
        """
        return self._is_verified

    @property
    def two_factor_enabled(self) -> bool:
        """Включена ли 2FA.

        Returns:
            ``True``, если включена.
        """
        return self._two_factor_enabled

    # -----------------------------------------------------------------------
    # Public methods
    # -----------------------------------------------------------------------

    def verify(self) -> None:
        """Подтвердить email.

        Returns:
            Ничего не возвращает.
        """
        self._is_verified = True

    def enable_two_factor(self) -> None:
        """Включить двухфакторную аутентификацию.

        Returns:
            Ничего не возвращает.
        """
        self._two_factor_enabled = True

    def disable_two_factor(self) -> None:
        """Выключить 2FA.

        Returns:
            Ничего не возвращает.
        """
        self._two_factor_enabled = False

    def change_password(self, new_hash: str) -> None:
        """Сменить пароль.

        Args:
            new_hash: Новый хеш пароля.

        Returns:
            Ничего не возвращает.

        Raises:
            InvalidCredentialsError: Если хеш слишком короткий.
        """
        if len(new_hash) < MIN_PASSWORD_LENGTH:
            raise InvalidCredentialsError(
                f"пароль должен быть не короче {MIN_PASSWORD_LENGTH} "
                f"символов"
            )
        self._password_hash = new_hash

    def check_password(self, password_hash: str) -> bool:
        """Проверить пароль.

        Args:
            password_hash: Проверяемый хеш.

        Returns:
            ``True``, если хеши совпадают.
        """
        return self._password_hash == password_hash

    def is_secure(self) -> bool:
        """Проверить безопасность аккаунта.

        Returns:
            ``True``, если email подтверждён и включена 2FA.
        """
        return self._is_verified and self._two_factor_enabled

    # -----------------------------------------------------------------------
    # Magic methods
    # -----------------------------------------------------------------------

    def __eq__(self, other: object) -> bool:
        """Сравнить два аккаунта.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении логина.
        """
        if not isinstance(other, Account):
            return NotImplemented
        return self._login == other._login

    def __hash__(self) -> int:
        """Вернуть хеш аккаунта.

        Returns:
            Целое число.
        """
        return hash(self._login)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._login}; {self._password_hash}; "
            f"{self._is_verified}"
        )
