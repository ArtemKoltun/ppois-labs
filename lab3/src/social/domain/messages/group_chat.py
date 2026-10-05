"""
Групповой чат.

Module: social.domain.messages.group_chat
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from social.domain.messages.chat import Chat

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class GroupChat(Chat):
    """Групповой чат.

    Attributes:
        _title: Название группы.
        _participants_count: Число участников.
        _is_public: Публичный ли чат.
    """

    def __init__(
        self,
        first_user: str,
        second_user: str,
        title: str,
    ) -> None:
        """Создать групповой чат.

        Args:
            first_user: Создатель.
            second_user: Второй участник.
            title: Название группы.
        """
        super().__init__(first_user, second_user)
        self._title: str = title
        self._participants_count: int = 2
        self._is_public: bool = False

    @property
    def title(self) -> str:
        """Название группы.

        Returns:
            Строка.
        """
        return self._title

    @property
    def participants_count(self) -> int:
        """Число участников.

        Returns:
            Целое число.
        """
        return self._participants_count

    def add_participant(self) -> None:
        """Добавить участника.

        Returns:
            Ничего не возвращает.
        """
        self._participants_count += 1

    def remove_participant(self) -> None:
        """Убрать участника.

        Returns:
            Ничего не возвращает.
        """
        self._participants_count = max(
            2, self._participants_count - 1
        )

    def make_public(self) -> None:
        """Сделать чат публичным.

        Returns:
            Ничего не возвращает.
        """
        self._is_public = True

    def is_public(self) -> bool:
        """Проверить публичность.

        Returns:
            ``True``, если публичный.
        """
        return self._is_public

    def is_large(self) -> bool:
        """Проверить размер группы.

        Returns:
            ``True``, если больше 50 участников.
        """
        return self._participants_count > 50

    def rename(self, new_title: str) -> None:
        """Переименовать группу.

        Args:
            new_title: Новое название.

        Returns:
            Ничего не возвращает.
        """
        self._title = new_title
