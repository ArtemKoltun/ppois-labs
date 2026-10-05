"""
Группа.

Module: social.domain.communities.group
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from social.domain.communities.community import Community

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Group(Community):
    """Группа — тип сообщества.

    Attributes:
        _is_private: Закрытая ли группа.
        _posts_count: Число постов.
        _rules: Правила группы.
    """

    def __init__(
        self,
        community: Community,
        is_private: bool = False,
    ) -> None:
        """Создать группу.

        Args:
            community: Базовое сообщество.
            is_private: Приватность.
        """
        super().__init__(
            name=community.name,
            owner=community.owner,
            description=community._description,
        )
        self._is_private: bool = is_private
        self._posts_count: int = 0
        self._rules: str = ""

    @property
    def is_private(self) -> bool:
        """Приватность.

        Returns:
            ``True``, если закрытая.
        """
        return self._is_private

    @property
    def posts_count(self) -> int:
        """Число постов.

        Returns:
            Целое число.
        """
        return self._posts_count

    def add_post(self) -> None:
        """Добавить пост.

        Returns:
            Ничего не возвращает.
        """
        self._posts_count += 1

    def set_rules(self, rules: str) -> None:
        """Установить правила.

        Args:
            rules: Правила.

        Returns:
            Ничего не возвращает.
        """
        self._rules = rules

    def make_public(self) -> None:
        """Сделать публичной.

        Returns:
            Ничего не возвращает.
        """
        self._is_private = False

    def make_private(self) -> None:
        """Сделать приватной.

        Returns:
            Ничего не возвращает.
        """
        self._is_private = True

    def is_active(self) -> bool:
        """Проверить активность.

        Returns:
            ``True``, если есть посты.
        """
        return self._posts_count > 0
