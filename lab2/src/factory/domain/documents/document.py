"""
Базовый документ.

Module: factory.domain.documents.document
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from factory.domain.personnel.employee import Employee

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Document(Readable, Writable):
    """Базовый документ завода.

    Attributes:
        _number: Номер документа.
        _date: Дата создания.
        _author: Автор.
        _title: Заголовок.
    """

    def __init__(
        self,
        number: str,
        date: str,
        author: Employee,
        title: str,
    ) -> None:
        """Создать документ.

        Args:
            number: Номер.
            date: Дата.
            author: Автор.
            title: Заголовок.

        Raises:
            ValueError: Если номер или заголовок пусты.
        """
        if not number or not title:
            raise ValueError("номер и заголовок не могут быть пустыми")
        self._number: str = number
        self._date: str = date
        self._author: Employee = author
        self._title: str = title

    @classmethod
    def _parse(cls, text: str) -> Document:
        """Разобрать документ из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        author: Employee = Employee.from_string(parts[2])
        return cls(
            number=parts[0],
            date=parts[1],
            author=author,
            title=parts[3],
        )

    @property
    def number(self) -> str:
        """Номер документа.

        Returns:
            Строка.
        """
        return self._number

    @property
    def title(self) -> str:
        """Заголовок.

        Returns:
            Строка.
        """
        return self._title

    @property
    def author(self) -> Employee:
        """Автор.

        Returns:
            Объект сотрудника.
        """
        return self._author

    def get_summary(self) -> str:
        """Вернуть краткую сводку.

        Returns:
            Строка вида ``"№123 от 2026-01-15: Чертёж вала"``.
        """
        return f"№{self._number} от {self._date}: {self._title}"

    def is_signed(self) -> bool:
        """Проверить подпись (базовая реализация — всегда True).

        Returns:
            ``True``.
        """
        return True

    def __eq__(self, other: object) -> bool:
        """Сравнить два документа.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении номеров.
        """
        if not isinstance(other, Document):
            return NotImplemented
        return self._number == other._number

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._number)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._number}; {self._date}; "
            f"{self._author}; {self._title}"
        )
