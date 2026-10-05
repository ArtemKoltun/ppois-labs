"""
Роль в группе.

Module: social.domain.communities.group_role
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

class GroupRole(Readable, Writable):
    """Роль пользователя в группе.

    Attributes:
        _name: Название роли.
        _can_post: Может публиковать.
        _can_moderate: Может модерировать.
    """

    def __init__(
        self,
        name: str,
        can_post: bool = True,
        can_moderate: bool = False,
    ) -> None:
        """Создать роль.

        Args:
            name: Название.
            can_post: Право публикации.
            can_moderate: Право модерации.
        """
        self._name: str = name
        self._can_post: bool = can_post
        self._can_moderate: bool = can_moderate

    @classmethod
    def _parse(cls, text: str) -> GroupRole:
        """Разобрать роль из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            name=parts[0],
            can_post=parts[1].lower() == "true",
            can_moderate=parts[2].lower() == "true",
        )

    @property
    def name(self) -> str:
        """Название роли.

        Returns:
            Строка.
        """
        return self._name

    def grant_moderation(self) -> None:
        """Выдать право модерации.

        Returns:
            Ничего не возвращает.
        """
        self._can_moderate = True

    def revoke_moderation(self) -> None:
        """Отозвать право модерации.

        Returns:
            Ничего не возвращает.
        """
        self._can_moderate = False

    def is_admin(self) -> bool:
        """Проверить, админ ли роль.

        Returns:
            ``True``, если может и постить, и модерировать.
        """
        return self._can_post and self._can_moderate

    def can_interact(self) -> bool:
        """Проверить, может ли роль взаимодействовать.

        Returns:
            ``True``, если может постить или модерировать.
        """
        return self._can_post or self._can_moderate

    def __eq__(self, other: object) -> bool:
        """Сравнить две роли.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении имени.
        """
        if not isinstance(other, GroupRole):
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
        return (
            f"{self._name}; {self._can_post}; "
            f"{self._can_moderate}"
        )
