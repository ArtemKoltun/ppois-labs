"""
Реакция на контент.

Module: social.domain.content.reaction
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

class Reaction(Readable, Writable):
    """Реакция пользователя на контент.

    Attributes:
        _user: Пользователь.
        _content_id: Идентификатор контента.
        _reaction_type: Тип реакции.
    """

    def __init__(
        self,
        user: str,
        content_id: str,
        reaction_type: str = "like",
    ) -> None:
        """Создать реакцию.

        Args:
            user: Пользователь.
            content_id: Контент.
            reaction_type: Тип.
        """
        self._user: str = user
        self._content_id: str = content_id
        self._reaction_type: str = reaction_type

    @classmethod
    def _parse(cls, text: str) -> Reaction:
        """Разобрать реакцию из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            user=parts[0],
            content_id=parts[1],
            reaction_type=parts[2],
        )

    @property
    def user(self) -> str:
        """Пользователь.

        Returns:
            Строка.
        """
        return self._user

    @property
    def reaction_type(self) -> str:
        """Тип реакции.

        Returns:
            Строка.
        """
        return self._reaction_type

    def change_type(self, new_type: str) -> None:
        """Сменить тип реакции.

        Args:
            new_type: Новый тип.

        Returns:
            Ничего не возвращает.
        """
        self._reaction_type = new_type

    def is_positive(self) -> bool:
        """Проверить положительная ли реакция.

        Returns:
            ``True``, если тип — like или love.
        """
        return self._reaction_type in ("like", "love")

    def __eq__(self, other: object) -> bool:
        """Сравнить две реакции.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении пары (пользователь, контент).
        """
        if not isinstance(other, Reaction):
            return NotImplemented
        return (
            self._user == other._user
            and self._content_id == other._content_id
        )

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash((self._user, self._content_id))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._user}; {self._content_id}; "
            f"{self._reaction_type}"
        )
