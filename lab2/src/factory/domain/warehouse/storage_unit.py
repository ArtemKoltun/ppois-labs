"""
Единица хранения.

Module: factory.domain.warehouse.storage_unit
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

class StorageUnit(Readable, Writable):
    """Единица хранения на складе — стеллаж, ячейка, паллета.

    Attributes:
        _code: Код единицы.
        _type: Тип единицы.
        _max_weight: Максимальный вес.
        _current_weight: Текущий вес.
    """

    def __init__(
        self,
        code: str,
        unit_type: str,
        max_weight: float,
        current_weight: float = 0.0,
    ) -> None:
        """Создать единицу хранения.

        Args:
            code: Код.
            unit_type: Тип.
            max_weight: Максимальный вес.
            current_weight: Текущий вес.

        Raises:
            ValueError: Если данные некорректны.
        """
        if not code:
            raise ValueError("код не может быть пустым")
        if max_weight <= 0:
            raise ValueError("вес должен быть положительным")
        self._code: str = code
        self._type: str = unit_type
        self._max_weight: float = max_weight
        self._current_weight: float = current_weight

    @classmethod
    def _parse(cls, text: str) -> "StorageUnit":
        """Разобрать единицу из строки.

        Args:
            text: Строка с полями через запятую.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(",")]
        return cls(
            code=parts[0],
            unit_type=parts[1],
            max_weight=float(parts[2]),
            current_weight=float(parts[3]),
        )

    @property
    def code(self) -> str:
        """Код единицы.

        Returns:
            Строка.
        """
        return self._code

    @property
    def current_weight(self) -> float:
        """Текущий вес.

        Returns:
            Число.
        """
        return self._current_weight

    def load(self, weight: float) -> None:
        """Загрузить груз.

        Args:
            weight: Вес.

        Returns:
            Ничего не возвращает.

        Raises:
            ValueError: Если превышен максимальный вес.
        """
        if self._current_weight + weight > self._max_weight:
            raise ValueError("превышен максимальный вес")
        self._current_weight += weight

    def unload(self) -> None:
        """Разгрузить единицу.

        Returns:
            Ничего не возвращает.
        """
        self._current_weight = 0.0

    def is_empty(self) -> bool:
        """Проверить пустоту.

        Returns:
            ``True``, если вес нулевой.
        """
        return self._current_weight == 0.0

    def is_overloaded(self) -> bool:
        """Проверить перегрузку.

        Returns:
            ``True``, если вес превышает максимум.
        """
        return self._current_weight > self._max_weight

    def __eq__(self, other: object) -> bool:
        """Сравнить две единицы.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении кода.
        """
        if not isinstance(other, StorageUnit):
            return NotImplemented
        return self._code == other._code

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._code)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через запятую.
        """
        return (
            f"{self._code}, {self._type}, {self._max_weight}, "
            f"{self._current_weight}"
        )
