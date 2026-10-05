"""
Сообщество (базовый класс для групп и страниц).

Module: social.domain.communities.community
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.exceptions.content_exceptions import ContentModerationError

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Community(Readable, Writable):
    """Базовое сообщество социальной сети.

    Attributes:
        _name: Название.
        _owner: Владелец.
        _description: Описание.
        _members_count: Число участников.
        _is_verified: Верифицировано ли.
    """

    def __init__(
        self,
        name: str,
        owner: str,
        description: str = "",
    ) -> None:
        """Создать сообщество.

        Args:
            name: Название.
            owner: Владелец.
            description: Описание.

        Raises:
            ContentModerationError: Если данные некорректны.
        """
        if not name or not owner:
            raise ContentModerationError(
                "название и владелец не могут быть пустыми"
            )
        self._name: str = name
        self._owner: str = owner
        self._description: str = description
        self._members_count: int = 1
        self._is_verified: bool = False

    @classmethod
    def _parse(cls, text: str) -> Community:
        """Разобрать сообщество из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            name=parts[0],
            owner=parts[1],
            description=parts[2] if len(parts) > 2 else "",
        )

    @property
    def name(self) -> str:
        """Название.

        Returns:
            Строка.
        """
        return self._name

    @property
    def owner(self) -> str:
        """Владелец.

        Returns:
            Строка.
        """
        return self._owner

    @property
    def members_count(self) -> int:
        """Число участников.

        Returns:
            Целое число.
        """
        return self._members_count

    @property
    def is_verified(self) -> bool:
        """Верифицировано ли.

        Returns:
            ``True``, если верифицировано.
        """
        return self._is_verified

    def add_member(self) -> None:
        """Добавить участника.

        Returns:
            Ничего не возвращает.
        """
        self._members_count += 1

    def remove_member(self) -> None:
        """Убрать участника.

        Returns:
            Ничего не возвращает.
        """
        self._members_count = max(1, self._members_count - 1)

    def update_description(self, text: str) -> None:
        """Обновить описание.

        Args:
            text: Новое описание.

        Returns:
            Ничего не возвращает.
        """
        self._description = text

    def verify(self) -> None:
        """Верифицировать сообщество.

        Returns:
            Ничего не возвращает.
        """
        self._is_verified = True

    def transfer_ownership(self, new_owner: str) -> None:
        """Передать владение.

        Args:
            new_owner: Новый владелец.

        Returns:
            Ничего не возвращает.
        """
        self._owner = new_owner

    def is_popular(self) -> bool:
        """Проверить популярность.

        Returns:
            ``True``, если больше 10 000 участников.
        """
        return self._members_count > 10_000

    def __eq__(self, other: object) -> bool:
        """Сравнить два сообщества.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении имени.
        """
        if not isinstance(other, Community):
            return NotImplemented
        return self._name == other._name

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._name)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return f"{self._name}; {self._owner}; {self._description}"
