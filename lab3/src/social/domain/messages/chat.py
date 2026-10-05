"""
Личный чат.

Module: social.domain.messages.chat
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.exceptions.connection_exceptions import MessageDeliveryError

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Chat(Readable, Writable):
    """Личный чат между двумя пользователями.

    Attributes:
        _first_user: Первый участник.
        _second_user: Второй участник.
        _messages_count: Число сообщений.
        _is_muted: Отключены ли уведомления.
        _is_archived: Архивирован ли.
    """

    def __init__(
        self,
        first_user: str,
        second_user: str,
    ) -> None:
        """Создать чат.

        Args:
            first_user: Первый участник.
            second_user: Второй участник.

        Raises:
            MessageDeliveryError: Если участники совпадают.
        """
        if first_user == second_user:
            raise MessageDeliveryError(
                "участники чата не могут совпадать"
            )
        self._first_user: str = first_user
        self._second_user: str = second_user
        self._messages_count: int = 0
        self._is_muted: bool = False
        self._is_archived: bool = False

    @classmethod
    def _parse(cls, text: str) -> Chat:
        """Разобрать чат из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            first_user=parts[0],
            second_user=parts[1],
        )

    @property
    def first_user(self) -> str:
        """Первый участник.

        Returns:
            Строка.
        """
        return self._first_user

    @property
    def second_user(self) -> str:
        """Второй участник.

        Returns:
            Строка.
        """
        return self._second_user

    @property
    def messages_count(self) -> int:
        """Число сообщений.

        Returns:
            Целое число.
        """
        return self._messages_count

    @property
    def is_muted(self) -> bool:
        """Отключены ли уведомления.

        Returns:
            ``True``, если отключены.
        """
        return self._is_muted

    def send(self) -> None:
        """Отправить сообщение.

        Returns:
            Ничего не возвращает.
        """
        self._messages_count += 1

    def mute(self) -> None:
        """Отключить уведомления.

        Returns:
            Ничего не возвращает.
        """
        self._is_muted = True

    def unmute(self) -> None:
        """Включить уведомления.

        Returns:
            Ничего не возвращает.
        """
        self._is_muted = False

    def archive(self) -> None:
        """Архивировать чат.

        Returns:
            Ничего не возвращает.
        """
        self._is_archived = True

    def unarchive(self) -> None:
        """Разархивировать чат.

        Returns:
            Ничего не возвращает.
        """
        self._is_archived = False

    def is_archived(self) -> bool:
        """Проверить архивацию.

        Returns:
            ``True``, если архивирован.
        """
        return self._is_archived

    def has_participant(self, username: str) -> bool:
        """Проверить, участвует ли пользователь.

        Args:
            username: Имя пользователя.

        Returns:
            ``True``, если участвует.
        """
        return username in (self._first_user, self._second_user)

    def is_active(self) -> bool:
        """Проверить активность чата.

        Returns:
            ``True``, если есть сообщения и не архивирован.
        """
        return self._messages_count > 0 and not self._is_archived

    def __eq__(self, other: object) -> bool:
        """Сравнить два чата.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении пары участников.
        """
        if not isinstance(other, Chat):
            return NotImplemented
        pair_self: tuple[str, str] = (
            self._first_user,
            self._second_user,
        )
        pair_other: tuple[str, str] = (
            other._first_user,
            other._second_user,
        )
        return pair_self == pair_other or pair_self == pair_other[::-1]

    def __hash__(self) -> int:
        """Вернуть хеш чата.

        Returns:
            Целое число.
        """
        first: str
        second: str
        first, second = sorted(
            (self._first_user, self._second_user)
        )
        return hash((first, second))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return f"{self._first_user}; {self._second_user}"
