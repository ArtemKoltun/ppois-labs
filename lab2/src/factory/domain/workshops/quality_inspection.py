"""
Проверка качества (ОТК).

Module: factory.domain.workshops.quality_inspection
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.exceptions.part_exceptions import (
    QualityControlFailedError,
)
from factory.domain.parts.part import Part

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_PASS_THRESHOLD: float = 0.95
"""Минимальная доля годных деталей для успешной проверки."""


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class QualityInspection(Readable, Writable):
    """Проверка партии деталей отделом технического контроля.

    Attributes:
        _part: Проверяемая деталь.
        _inspector_name: Имя контролёра.
        _batch_size: Размер партии.
        _passed_count: Число годных.
        _date: Дата проверки.
    """

    def __init__(
        self,
        part: Part,
        inspector_name: str,
        batch_size: int,
        date: str,
    ) -> None:
        """Создать проверку качества.

        Args:
            part: Деталь.
            inspector_name: Контролёр.
            batch_size: Размер партии.
            date: Дата.

        Raises:
            ValueError: Если размер партии не положительный.
        """
        if batch_size <= 0:
            raise ValueError("размер партии должен быть положительным")
        self._part: Part = part
        self._inspector_name: str = inspector_name
        self._batch_size: int = batch_size
        self._passed_count: int = 0
        self._date: str = date

    @classmethod
    def _parse(cls, text: str) -> QualityInspection:
        """Разобрать проверку из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        part: Part = Part.from_string(parts[0])
        return cls(
            part=part,
            inspector_name=parts[1],
            batch_size=int(parts[2]),
            date=parts[4],
        )

    @property
    def batch_size(self) -> int:
        """Размер партии.

        Returns:
            Целое число.
        """
        return self._batch_size

    @property
    def passed_count(self) -> int:
        """Число годных деталей.

        Returns:
            Целое число.
        """
        return self._passed_count

    def record_pass(self, count: int) -> None:
        """Записать число годных деталей.

        Args:
            count: Число годных.

        Returns:
            Ничего не возвращает.
        """
        self._passed_count = min(count, self._batch_size)

    def pass_rate(self) -> float:
        """Рассчитать долю годных деталей.

        Returns:
            Число от 0 до 1.
        """
        if self._batch_size == 0:
            return 0.0
        return self._passed_count / self._batch_size

    def is_successful(self) -> bool:
        """Проверить успешность проверки.

        Returns:
            ``True``, если доля годных не ниже порога.
        """
        return self.pass_rate() >= _PASS_THRESHOLD

    def raise_if_failed(self) -> None:
        """Бросить исключение, если проверка не пройдена.

        Returns:
            Ничего не возвращает.

        Raises:
            QualityControlFailedError: Если доля годных ниже порога.
        """
        if not self.is_successful():
            raise QualityControlFailedError(
                f"партия {self._part.name} не прошла ОТК: "
                f"годных {self.pass_rate():.0%}"
            )

    def __eq__(self, other: object) -> bool:
        """Сравнить две проверки.

        Args:
            other: Другой объект.

        Returns:
            ``True``, если совпадают деталь и дата.
        """
        if not isinstance(other, QualityInspection):
            return NotImplemented
        return (
            self._part == other._part
            and self._date == other._date
        )

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash((self._part, self._date))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._part}; {self._inspector_name}; "
            f"{self._batch_size}; {self._passed_count}; "
            f"{self._date}"
        )
