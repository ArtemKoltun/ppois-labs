"""
Уведомление.

Module: social.domain.notifications.notification
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.enums.notification_type import NotificationType
from common.exceptions.connection_exceptions import NotificationError

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Notification(Readable, Writable):
    """Уведомление пользователю.

    Attributes:
        _recipient: Получатель.
        _type: Тип уведомления.
        _text: Текст.
        _is_read: Прочитано ли.
        _priority: Приоритет от 1 до 5.
    """

    def __init__(
        self,
        recipient: str,
        notification_type: NotificationType,
        text: str = "",
        priority: int = 3,
    ) -> None:
        """Создать уведомление.

        Args:
            recipient: Получатель.
            notification_type: Тип.
            text: Текст.
            priority: Приоритет.

        Raises:
            NotificationError: Если данные некорректны.
        """
        if not recipient:
            raise NotificationError(
                "получатель не может быть пустым"
            )
        if not 1 <= priority <= 5:
            raise NotificationError(
                "приоритет должен быть от 1 до 5"
            )
        self._recipient: str = recipient
        self._type: NotificationType = notification_type
        self._text: str = text
        self._is_read: bool = False
        self._priority: int = priority

    @classmethod
    def _parse(cls, text: str) -> Notification:
        """Разобрать уведомление из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            recipient=parts[0],
            notification_type=NotificationType(parts[1]),
            text=parts[2] if len(parts) > 2 else "",
            priority=int(parts[3]) if len(parts) > 3 else 3,
        )

    @property
    def recipient(self) -> str:
        """Получатель.

        Returns:
            Строка.
        """
        return self._recipient

    @property
    def notification_type(self) -> NotificationType:
        """Тип.

        Returns:
            Элемент перечисления.
        """
        return self._type

    @property
    def text(self) -> str:
        """Текст.

        Returns:
            Строка.
        """
        return self._text

    @property
    def is_read(self) -> bool:
        """Прочитано ли.

        Returns:
            ``True``, если прочитано.
        """
        return self._is_read

    @property
    def priority(self) -> int:
        """Приоритет.

        Returns:
            Целое число от 1 до 5.
        """
        return self._priority

    def mark_read(self) -> None:
        """Отметить как прочитанное.

        Returns:
            Ничего не возвращает.
        """
        self._is_read = True

    def raise_priority(self) -> None:
        """Повысить приоритет.

        Returns:
            Ничего не возвращает.
        """
        self._priority = min(5, self._priority + 1)

    def is_urgent(self) -> bool:
        """Проверить срочность.

        Returns:
            ``True``, если приоритет >= 4.
        """
        return self._priority >= 4

    def __eq__(self, other: object) -> bool:
        """Сравнить два уведомления.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении получателя и типа.
        """
        if not isinstance(other, Notification):
            return NotImplemented
        return (
            self._recipient == other._recipient
            and self._type == other._type
            and self._text == other._text
        )

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash((self._recipient, self._type, self._text))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._recipient}; {self._type.value}; "
            f"{self._text}; {self._priority}"
        )
