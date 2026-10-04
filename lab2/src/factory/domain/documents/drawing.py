"""
Чертёж детали.

Module: factory.domain.documents.drawing
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from factory.domain.documents.document import Document
from factory.domain.parts.part import Part
from factory.domain.personnel.employee import Employee


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Drawing(Document):
    """Чертёж детали.

    Attributes:
        _part: Деталь.
        _scale: Масштаб.
        _format: Формат листа.
    """

    def __init__(
        self,
        document: Document,
        part: Part,
        scale: str,
        format_: str,
    ) -> None:
        """Создать чертёж.

        Args:
            document: Базовый документ.
            part: Деталь.
            scale: Масштаб.
            format_: Формат листа.
        """
        super().__init__(
            number=document.number,
            date=document._date,
            author=document.author,
            title=document.title,
        )
        self._part: Part = part
        self._scale: str = scale
        self._format: str = format_

    def is_large_format(self) -> bool:
        """Проверить крупный формат.

        Returns:
            ``True``, если формат A0 или A1.
        """
        return self._format in ("A0", "A1")

    def is_zoomed(self) -> bool:
        """Проверить увеличенный масштаб.

        Returns:
            ``True``, если масштаб содержит увеличение.
        """
        return self._scale.startswith("2") or self._scale.startswith("5")

    def matches_part(self, part: Part) -> bool:
        """Проверить соответствие детали.

        Args:
            part: Деталь.

        Returns:
            ``True``, если чертёж для этой детали.
        """
        return self._part == part

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка.
        """
        return (
            f"Чертёж {self._number} для {self._part.name}, "
            f"масштаб {self._scale}, формат {self._format}"
        )
