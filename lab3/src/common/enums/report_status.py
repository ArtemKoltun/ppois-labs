"""
Статус жалобы.

Module: common.enums.report_status
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from enum import Enum

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class ReportStatus(Enum):
    """Статус рассмотрения жалобы.

    Attributes:
        PENDING: Ожидает рассмотрения.
        IN_REVIEW: На рассмотрении.
        RESOLVED: Рассмотрена.
        REJECTED: Отклонена.
    """

    PENDING = "pending"
    IN_REVIEW = "in_review"
    RESOLVED = "resolved"
    REJECTED = "rejected"

    def __str__(self) -> str:
        """Вернуть человекочитаемое название.

        Returns:
            Строка на русском.
        """
        names: dict[ReportStatus, str] = {
            ReportStatus.PENDING: "ожидает",
            ReportStatus.IN_REVIEW: "на рассмотрении",
            ReportStatus.RESOLVED: "рассмотрена",
            ReportStatus.REJECTED: "отклонена",
        }
        return names[self]
