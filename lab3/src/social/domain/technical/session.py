"""
Сессия пользователя.

Module: social.domain.technical.session
"""

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from social.domain.technical.device import Device


class Session(Readable, Writable):
    """Активная сессия пользователя.

    Attributes:
        _user: Пользователь.
        _device: Устройство.
        _token: Токен.
        _is_active: Активна ли.
    """

    def __init__(
        self,
        user: str,
        device: Device,
        token: str,
    ) -> None:
        """Создать сессию.

        Args:
            user: Пользователь.
            device: Устройство.
            token: Токен.
        """
        self._user: str = user
        self._device: Device = device
        self._token: str = token
        self._is_active: bool = True

    @classmethod
    def _parse(cls, text: str) -> Session:
        """Разобрать сессию из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        device: Device = Device(
            user=parts[0],
            device_type=parts[2],
            os_name=parts[3],
        )
        return cls(
            user=parts[0],
            device=device,
            token=parts[1],
        )

    @property
    def user(self) -> str:
        """Пользователь.

        Returns:
            Строка.
        """
        return self._user

    @property
    def token(self) -> str:
        """Токен.

        Returns:
            Строка.
        """
        return self._token

    def terminate(self) -> None:
        """Завершить сессию.

        Returns:
            Ничего не возвращает.
        """
        self._is_active = False

    def reactivate(self) -> None:
        """Возобновить.

        Returns:
            Ничего не возвращает.
        """
        self._is_active = True

    def is_active(self) -> bool:
        """Проверить активность.

        Returns:
            ``True``, если активна.
        """
        return self._is_active

    def belongs_to(self, username: str) -> bool:
        """Проверить принадлежность.

        Args:
            username: Имя.

        Returns:
            ``True``, если сессия пользователя.
        """
        return self._user == username

    def __eq__(self, other: object) -> bool:
        """Сравнить две сессии.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении токена.
        """
        if not isinstance(other, Session):
            return NotImplemented
        return self._token == other._token

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._token)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._user}; {self._token}; "
            f"{self._device.device_type}; {self._device._os}"
        )
