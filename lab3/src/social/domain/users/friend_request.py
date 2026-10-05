"""
Заявка в друзья.

Module: social.domain.users.friend_request
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.exceptions.connection_exceptions import FriendshipError

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class FriendRequest(Readable, Writable):
    """Заявка в друзья от одного пользователя другому.

    Attributes:
        _from_username: От кого.
        _to_username: Кому.
        _message: Сообщение к заявке.
        _is_accepted: Принята ли.
        _is_rejected: Отклонена ли.
    """

    # -----------------------------------------------------------------------
    # Constructors
    # -----------------------------------------------------------------------

    def __init__(
        self,
        from_username: str,
        to_username: str,
        message: str = "",
    ) -> None:
        """Создать заявку в друзья.

        Args:
            from_username: От кого.
            to_username: Кому.
            message: Сообщение.

        Raises:
            FriendshipError: Если отправитель и получатель совпадают.
        """
        if from_username == to_username:
            raise FriendshipError(
                "нельзя отправить заявку самому себе"
            )
        self._from_username: str = from_username
        self._to_username: str = to_username
        self._message: str = message
        self._is_accepted: bool = False
        self._is_rejected: bool = False

    @classmethod
    def _parse(cls, text: str) -> FriendRequest:
        """Разобрать заявку из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            from_username=parts[0],
            to_username=parts[1],
            message=parts[2],
        )

    # -----------------------------------------------------------------------
    # Properties
    # -----------------------------------------------------------------------

    @property
    def from_username(self) -> str:
        """Отправитель.

        Returns:
            Строка.
        """
        return self._from_username

    @property
    def to_username(self) -> str:
        """Получатель.

        Returns:
            Строка.
        """
        return self._to_username

    @property
    def message(self) -> str:
        """Сообщение к заявке.

        Returns:
            Строка.
        """
        return self._message

    @property
    def is_accepted(self) -> bool:
        """Принята ли заявка.

        Returns:
            ``True``, если принята.
        """
        return self._is_accepted

    @property
    def is_rejected(self) -> bool:
        """Отклонена ли заявка.

        Returns:
            ``True``, если отклонена.
        """
        return self._is_rejected

    # -----------------------------------------------------------------------
    # Public methods
    # -----------------------------------------------------------------------

    def accept(self) -> None:
        """Принять заявку.

        Returns:
            Ничего не возвращает.

        Raises:
            FriendshipError: Если заявка уже обработана.
        """
        if self._is_rejected:
            raise FriendshipError("заявка уже отклонена")
        self._is_accepted = True

    def reject(self) -> None:
        """Отклонить заявку.

        Returns:
            Ничего не возвращает.

        Raises:
            FriendshipError: Если заявка уже обработана.
        """
        if self._is_accepted:
            raise FriendshipError("заявка уже принята")
        self._is_rejected = True

    def is_pending(self) -> bool:
        """Проверить, что заявка ещё не обработана.

        Returns:
            ``True``, если ни принята, ни отклонена.
        """
        return not self._is_accepted and not self._is_rejected

    def has_message(self) -> bool:
        """Проверить наличие сообщения.

        Returns:
            ``True``, если сообщение непустое.
        """
        return bool(self._message)

    # -----------------------------------------------------------------------
    # Magic methods
    # -----------------------------------------------------------------------

    def __eq__(self, other: object) -> bool:
        """Сравнить две заявки.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении пары (от, кому).
        """
        if not isinstance(other, FriendRequest):
            return NotImplemented
        return (
            self._from_username == other._from_username
            and self._to_username == other._to_username
        )

    def __hash__(self) -> int:
        """Вернуть хеш заявки.

        Returns:
            Целое число.
        """
        return hash((self._from_username, self._to_username))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._from_username}; {self._to_username}; "
            f"{self._message}"
        )
