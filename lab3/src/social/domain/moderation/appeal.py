"""
Апелляция на блокировку.

Module: social.domain.moderation.appeal
"""

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable


class Appeal(Readable, Writable):
    """Апелляция на решение модератора.

    Attributes:
        _username: Кто подаёт.
        _ban_target: На кого была блокировка.
        _text: Текст апелляции.
        _is_reviewed: Рассмотрена ли.
    """

    def __init__(
        self,
        username: str,
        ban_target: str,
        text: str,
    ) -> None:
        """Создать апелляцию.

        Args:
            username: Кто подаёт.
            ban_target: Заблокированный.
            text: Текст.
        """
        self._username: str = username
        self._ban_target: str = ban_target
        self._text: str = text
        self._is_reviewed: bool = False

    @classmethod
    def _parse(cls, text: str) -> Appeal:
        """Разобрать апелляцию из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            username=parts[0],
            ban_target=parts[1],
            text=parts[2],
        )

    @property
    def username(self) -> str:
        """Кто подаёт.

        Returns:
            Строка.
        """
        return self._username

    @property
    def text(self) -> str:
        """Текст.

        Returns:
            Строка.
        """
        return self._text

    @property
    def is_reviewed(self) -> bool:
        """Рассмотрена ли.

        Returns:
            ``True``, если рассмотрена.
        """
        return self._is_reviewed

    def review(self) -> None:
        """Рассмотреть апелляцию.

        Returns:
            Ничего не возвращает.
        """
        self._is_reviewed = True

    def update_text(self, text: str) -> None:
        """Обновить текст.

        Args:
            text: Новый текст.

        Returns:
            Ничего не возвращает.
        """
        self._text = text

    def is_long(self) -> bool:
        """Проверить длину.

        Returns:
            ``True``, если текст длиннее 1000 символов.
        """
        return len(self._text) > 1000

    def __eq__(self, other: object) -> bool:
        """Сравнить две апелляции.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении автора и цели.
        """
        if not isinstance(other, Appeal):
            return NotImplemented
        return (
            self._username == other._username
            and self._ban_target == other._ban_target
        )

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash((self._username, self._ban_target))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return f"{self._username}; {self._ban_target}; {self._text}"
