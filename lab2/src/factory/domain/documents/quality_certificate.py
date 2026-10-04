"""
Сертификат качества.

Module: factory.domain.documents.quality_certificate
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from factory.domain.documents.document import Document
from factory.domain.parts.part import Part
from factory.domain.workshops.quality_inspection import (
    QualityInspection,
)

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class QualityCertificate(Document):
    """Сертификат качества на партию деталей.

    Attributes:
        _part: Деталь.
        _inspection: Проверка ОТК.
        _valid_until: Срок действия.
    """

    def __init__(
        self,
        document: Document,
        part: Part,
        inspection: QualityInspection,
        valid_until: str,
    ) -> None:
        """Создать сертификат.

        Args:
            document: Базовый документ.
            part: Деталь.
            inspection: Проверка ОТК.
            valid_until: Срок действия.
        """
        super().__init__(
            number=document.number,
            date=document._date,
            author=document.author,
            title=document.title,
        )
        self._part: Part = part
        self._inspection: QualityInspection = inspection
        self._valid_until: str = valid_until

    def is_valid_for(self, date: str) -> bool:
        """Проверить, действителен ли сертификат на дату.

        Args:
            date: Дата проверки.

        Returns:
            ``True``, если дата не позже срока действия.
        """
        return date <= self._valid_until

    def passed_all_checks(self) -> bool:
        """Проверить, прошла ли партия ОТК.

        Returns:
            ``True``, если проверка успешна.
        """
        return self._inspection.is_successful()

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка.
        """
        return (
            f"Сертификат {self._number} на {self._part.name}, "
            f"действителен до {self._valid_until}"
        )
