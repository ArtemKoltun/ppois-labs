"""
Настройки уведомлений.

Module: social.domain.notifications.notification_settings
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class NotificationSettings(Readable, Writable):
    """Настройки уведомлений пользователя.

    Attributes:
        _user: Пользователь.
        _push_enabled: Push включён.
        _email_enabled: Email включён.
        _quiet_hours_start: Час начала тишины.
    """

    def __init__(
        self,
        user: str,
        push_enabled: bool = True,
        email_enabled: bool = True,
        quiet_hours_start: int = 22,
    ) -> None:
        """Создать настройки.

        Args:
            user: Пользователь.
            push_enabled: Push.
            email_enabled: Email.
            quiet_hours_start: Начало тишины.
        """
        self._user: str = user
        self._push_enabled: bool = push_enabled
        self._email_enabled: bool = email_enabled
        self._quiet_hours_start: int = quiet_hours_start

    @classmethod
    def _parse(cls, text: str) -> NotificationSettings:
        """Разобрать настройки из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            user=parts[0],
            push_enabled=parts[1].lower() == "true",
            email_enabled=parts[2].lower() == "true",
            quiet_hours_start=int(parts[3]),
        )

    @property
    def user(self) -> str:
        """Пользователь.

        Returns:
            Строка.
        """
        return self._user

    def toggle_push(self) -> None:
        """Переключить push.

        Returns:
            Ничего не возвращает.
        """
        self._push_enabled = not self._push_enabled

    def toggle_email(self) -> None:
        """Переключить email.

        Returns:
            Ничего не возвращает.
        """
        self._email_enabled = not self._email_enabled

    def set_quiet_hours(self, hour: int) -> None:
        """Установить час тишины.

        Args:
            hour: Час от 0 до 23.

        Returns:
            Ничего не возвращает.
        """
        self._quiet_hours_start = hour

    def is_in_quiet_hours(self, current_hour: int) -> bool:
        """Проверить тихие часы.

        Args:
            current_hour: Текущий час.

        Returns:
            ``True``, если в тихих часах.
        """
        return current_hour >= self._quiet_hours_start

    def all_disabled(self) -> bool:
        """Проверить, все ли каналы отключены.

        Returns:
            ``True``, если оба канала выключены.
        """
        return not self._push_enabled and not self._email_enabled

    def __eq__(self, other: object) -> bool:
        """Сравнить настройки.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении пользователя.
        """
        if not isinstance(other, NotificationSettings):
            return NotImplemented
        return self._user == other._user

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._user)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._user}; {self._push_enabled}; "
            f"{self._email_enabled}; {self._quiet_hours_start}"
        )
