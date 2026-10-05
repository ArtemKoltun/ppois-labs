"""
Упоминание пользователя.

Module: social.domain.media.mention
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

class Mention(Readable, Writable):
    """Упоминание пользователя в контенте.

    Attributes:
        _content_id: Контент.
        _mentioned_user: Упомянутый пользователь.
        _is_read: Прочитано ли уведомление.
    """

    def __init__(
        self,
        content_id: str,
        mentioned_user: str,
    ) -> None:
        """Создать упоминание.

        Args:
            content_id: Идентификатор контента.
            mentioned_user: Упомянутый пользователь.
        """
        self._content_id: str = content_id
        self._mentioned_user: str = mentioned_user
        self._is_read: bool = False

    @classmethod
    def _parse(cls, text: str) -> Mention:
        """Разобрать упоминание из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            content_id=parts[0],
            mentioned_user=parts[1],
        )

    @property
    def content_id(self) -> str:
        """Контент.

        Returns:
            Строка.
        """
        return self._content_id

    @property
    def mentioned_user(self) -> str:
        """Упомянутый пользователь.

        Returns:
            Строка.
        """
        return self._mentioned_user

    @property
    def is_read(self) -> bool:
        """Прочитано ли.

        Returns:
            ``True``, если прочитано.
        """
        return self._is_read

    def mark_read(self) -> None:
        """Отметить как прочитанное.

        Returns:
            Ничего не возвращает.
        """
        self._is_read = True

    def __eq__(self, other: object) -> bool:
        """Сравнить два упоминания.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении контента и пользователя.
        """
        if not isinstance(other, Mention):
            return NotImplemented
        return (
            self._content_id == other._content_id
            and self._mentioned_user == other._mentioned_user
        )

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash((self._content_id, self._mentioned_user))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return f"{self._content_id}; {self._mentioned_user}"
