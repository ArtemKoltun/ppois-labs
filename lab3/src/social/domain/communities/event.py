"""
Событие.

Module: social.domain.communities.event
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

class Event(Readable, Writable):
    """Событие, организованное сообществом.

    Attributes:
        _title: Название.
        _organizer: Организатор.
        _date: Дата.
        _location: Место.
        _participants_count: Число участников.
        _is_online: Онлайн ли.
    """

    def __init__(
        self,
        title: str,
        organizer: str,
        date: str,
        location: str = "",
        is_online: bool = False,
    ) -> None:
        """Создать событие.

        Args:
            title: Название.
            organizer: Организатор.
            date: Дата.
            location: Место.
            is_online: Онлайн ли.

        Raises:
            ContentModerationError: Если данные некорректны.
        """
        if not title or not organizer:
            raise ContentModerationError(
                "название и организатор не могут быть пустыми"
            )
        self._title: str = title
        self._organizer: str = organizer
        self._date: str = date
        self._location: str = location
        self._participants_count: int = 0
        self._is_online: bool = is_online

    @classmethod
    def _parse(cls, text: str) -> Event:
        """Разобрать событие из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            title=parts[0],
            organizer=parts[1],
            date=parts[2],
            location=parts[3] if len(parts) > 3 else "",
            is_online=(
                parts[4].lower() == "true" if len(parts) > 4 else False
            ),
        )

    @property
    def title(self) -> str:
        """Название.

        Returns:
            Строка.
        """
        return self._title

    @property
    def date(self) -> str:
        """Дата.

        Returns:
            Строка.
        """
        return self._date

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
            0, self._participants_count - 1
        )

    def make_online(self) -> None:
        """Перевести в онлайн-формат.

        Returns:
            Ничего не возвращает.
        """
        self._is_online = True
        self._location = ""

    def is_online(self) -> bool:
        """Проверить формат.

        Returns:
            ``True``, если онлайн.
        """
        return self._is_online

    def is_large(self) -> bool:
        """Проверить размер.

        Returns:
            ``True``, если больше 1000 участников.
        """
        return self._participants_count > 1000

    def __eq__(self, other: object) -> bool:
        """Сравнить два события.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении названия и даты.
        """
        if not isinstance(other, Event):
            return NotImplemented
        return (
            self._title == other._title
            and self._date == other._date
        )

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash((self._title, self._date))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._title}; {self._organizer}; "
            f"{self._date}; {self._location}; {self._is_online}"
        )
