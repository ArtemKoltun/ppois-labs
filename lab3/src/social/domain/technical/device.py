"""
Устройство пользователя.

Module: social.domain.technical.device
"""

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable


class Device(Readable, Writable):
    """Устройство пользователя.

    Attributes:
        _user: Владелец.
        _device_type: Тип (mobile/desktop/tablet).
        _os: Операционная система.
        _is_trusted: Доверенное ли.
    """

    def __init__(
        self,
        user: str,
        device_type: str,
        os_name: str,
    ) -> None:
        """Создать устройство.

        Args:
            user: Владелец.
            device_type: Тип.
            os_name: ОС.
        """
        self._user: str = user
        self._device_type: str = device_type
        self._os: str = os_name
        self._is_trusted: bool = False

    @classmethod
    def _parse(cls, text: str) -> Device:
        """Разобрать устройство из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            user=parts[0],
            device_type=parts[1],
            os_name=parts[2],
        )

    @property
    def user(self) -> str:
        """Владелец.

        Returns:
            Строка.
        """
        return self._user

    @property
    def device_type(self) -> str:
        """Тип.

        Returns:
            Строка.
        """
        return self._device_type

    def trust(self) -> None:
        """Пометить доверенным.

        Returns:
            Ничего не возвращает.
        """
        self._is_trusted = True

    def untrust(self) -> None:
        """Снять доверие.

        Returns:
            Ничего не возвращает.
        """
        self._is_trusted = False

    def is_trusted(self) -> bool:
        """Проверить доверие.

        Returns:
            ``True``, если доверенное.
        """
        return self._is_trusted

    def is_mobile(self) -> bool:
        """Проверить мобильность.

        Returns:
            ``True``, если mobile или tablet.
        """
        return self._device_type in ("mobile", "tablet")

    def __eq__(self, other: object) -> bool:
        """Сравнить два устройства.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении владельца и типа.
        """
        if not isinstance(other, Device):
            return NotImplemented
        return (
            self._user == other._user
            and self._device_type == other._device_type
        )

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash((self._user, self._device_type))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return f"{self._user}; {self._device_type}; {self._os}"
