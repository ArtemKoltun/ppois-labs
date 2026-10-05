"""
Участник группы.

Module: social.domain.communities.group_member
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from social.domain.communities.group_role import GroupRole

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class GroupMember(Readable, Writable):
    """Участник группы с ролью.

    Attributes:
        _username: Имя участника.
        _group_name: Название группы.
        _role: Роль в группе.
        _is_active: Активен ли.
    """

    def __init__(
        self,
        username: str,
        group_name: str,
        role: GroupRole,
    ) -> None:
        """Создать участника группы.

        Args:
            username: Имя участника.
            group_name: Название группы.
            role: Роль.
        """
        self._username: str = username
        self._group_name: str = group_name
        self._role: GroupRole = role
        self._is_active: bool = True

    @classmethod
    def _parse(cls, text: str) -> GroupMember:
        """Разобрать участника из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        role: GroupRole = GroupRole(parts[2])
        return cls(
            username=parts[0],
            group_name=parts[1],
            role=role,
        )

    @property
    def username(self) -> str:
        """Имя участника.

        Returns:
            Строка.
        """
        return self._username

    @property
    def role(self) -> GroupRole:
        """Роль.

        Returns:
            Объект ``GroupRole``.
        """
        return self._role

    def change_role(self, role: GroupRole) -> None:
        """Сменить роль.

        Args:
            role: Новая роль.

        Returns:
            Ничего не возвращает.
        """
        self._role = role

    def leave(self) -> None:
        """Покинуть группу.

        Returns:
            Ничего не возвращает.
        """
        self._is_active = False

    def rejoin(self) -> None:
        """Вернуться в группу.

        Returns:
            Ничего не возвращает.
        """
        self._is_active = True

    def can_moderate(self) -> bool:
        """Проверить право модерации.

        Returns:
            ``True``, если роль позволяет.
        """
        return self._role.is_admin()

    def __eq__(self, other: object) -> bool:
        """Сравнить двух участников.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении пары (группа, участник).
        """
        if not isinstance(other, GroupMember):
            return NotImplemented
        return (
            self._username == other._username
            and self._group_name == other._group_name
        )

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash((self._username, self._group_name))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._username}; {self._group_name}; "
            f"{self._role}"
        )
