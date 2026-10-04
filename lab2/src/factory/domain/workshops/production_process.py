"""
Технологический процесс производства.

Module: factory.domain.workshops.production_process
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from factory.domain.parts.part import Part
from factory.domain.workshops.workshop import Workshop

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class ProductionProcess(Readable, Writable):
    """Технологический процесс изготовления детали.

    Attributes:
        _name: Наименование процесса.
        _part: Изготавливаемая деталь.
        _workshops: Список цехов.
        _duration_hours: Длительность в часах.
    """

    def __init__(
        self,
        name: str,
        part: Part,
        workshops: list[Workshop] | None = None,
        duration_hours: float = 0.0,
    ) -> None:
        """Создать техпроцесс.

        Args:
            name: Наименование.
            part: Деталь.
            workshops: Список цехов.
            duration_hours: Длительность.
        """
        self._name: str = name
        self._part: Part = part
        self._workshops: list[Workshop] = (
            list(workshops) if workshops else []
        )
        self._duration_hours: float = duration_hours

    @classmethod
    def _parse(cls, text: str) -> ProductionProcess:
        """Разобрать процесс из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        part: Part = Part.from_string(parts[1])
        return cls(
            name=parts[0],
            part=part,
            duration_hours=float(parts[2]),
        )

    @property
    def name(self) -> str:
        """Наименование.

        Returns:
            Строка.
        """
        return self._name

    @property
    def duration_hours(self) -> float:
        """Длительность.

        Returns:
            Часы.
        """
        return self._duration_hours

    def add_workshop(self, workshop: Workshop) -> None:
        """Добавить цех в маршрут.

        Args:
            workshop: Цех.

        Returns:
            Ничего не возвращает.
        """
        self._workshops.append(workshop)

    def total_duration(self) -> float:
        """Вернуть общую длительность процесса.

        Returns:
            Часы.
        """
        return self._duration_hours

    def is_long(self) -> bool:
        """Проверить, длительный ли процесс.

        Returns:
            ``True``, если дольше 24 часов.
        """
        return self._duration_hours > 24

    def workshops_count(self) -> int:
        """Вернуть число цехов в маршруте.

        Returns:
            Целое число.
        """
        return len(self._workshops)

    def __eq__(self, other: object) -> bool:
        """Сравнить два процесса.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении имени.
        """
        if not isinstance(other, ProductionProcess):
            return NotImplemented
        return self._name == other._name

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._name)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._name}; {self._part}; "
            f"{self._duration_hours}"
        )
