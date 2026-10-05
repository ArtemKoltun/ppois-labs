"""
Жалоба на контент или пользователя.

Module: social.domain.moderation.report
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.enums.report_status import ReportStatus
from common.exceptions.content_exceptions import ContentModerationError

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Report(Readable, Writable):
    """Жалоба на контент или пользователя.

    Attributes:
        _author: Автор жалобы.
        _target: На что жалуются.
        _reason: Причина.
        _status: Статус.
        _reviewer: Проверяющий.
    """

    def __init__(
        self,
        author: str,
        target: str,
        reason: str,
    ) -> None:
        """Создать жалобу.

        Args:
            author: Автор.
            target: Цель.
            reason: Причина.

        Raises:
            ContentModerationError: Если данные некорректны.
        """
        if not author or not target or not reason:
            raise ContentModerationError(
                "все поля жалобы обязательны"
            )
        self._author: str = author
        self._target: str = target
        self._reason: str = reason
        self._status: ReportStatus = ReportStatus.PENDING
        self._reviewer: str = ""

    @classmethod
    def _parse(cls, text: str) -> Report:
        """Разобрать жалобу из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            author=parts[0],
            target=parts[1],
            reason=parts[2],
        )

    @property
    def author(self) -> str:
        """Автор.

        Returns:
            Строка.
        """
        return self._author

    @property
    def target(self) -> str:
        """Цель жалобы.

        Returns:
            Строка.
        """
        return self._target

    @property
    def status(self) -> ReportStatus:
        """Статус.

        Returns:
            Элемент перечисления.
        """
        return self._status

    def take_in_review(self, reviewer: str) -> None:
        """Взять в рассмотрение.

        Args:
            reviewer: Модератор.

        Returns:
            Ничего не возвращает.
        """
        self._status = ReportStatus.IN_REVIEW
        self._reviewer = reviewer

    def resolve(self) -> None:
        """Рассмотреть.

        Returns:
            Ничего не возвращает.
        """
        self._status = ReportStatus.RESOLVED

    def reject(self) -> None:
        """Отклонить.

        Returns:
            Ничего не возвращает.
        """
        self._status = ReportStatus.REJECTED

    def is_pending(self) -> bool:
        """Проверить, что жалоба в ожидании.

        Returns:
            ``True``, если PENDING.
        """
        return self._status is ReportStatus.PENDING

    def has_reviewer(self) -> bool:
        """Проверить наличие проверяющего.

        Returns:
            ``True``, если назначен.
        """
        return bool(self._reviewer)

    def __eq__(self, other: object) -> bool:
        """Сравнить две жалобы.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении автора и цели.
        """
        if not isinstance(other, Report):
            return NotImplemented
        return (
            self._author == other._author
            and self._target == other._target
        )

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash((self._author, self._target))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return f"{self._author}; {self._target}; {self._reason}"
