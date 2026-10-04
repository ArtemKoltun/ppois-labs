"""
Запись о техническом обслуживании.

Module: factory.domain.equipment.maintenance_record
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from factory.domain.equipment.equipment import Equipment

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class MaintenanceRecord(Readable, Writable):
    """Запись о проведённом ТО.

    Attributes:
        _equipment: Обслуживаемое оборудование.
        _performed_by: Имя исполнителя.
        _date: Дата проведения.
        _description: Описание работ.
        _cost: Стоимость работ.
    """

    def __init__(
        self,
        equipment: Equipment,
        performed_by: str,
        date: str,
        description: str,
        cost: float,
    ) -> None:
        """Создать запись о ТО.

        Args:
            equipment: Оборудование.
            performed_by: Исполнитель.
            date: Дата.
            description: Описание.
            cost: Стоимость.
        """
        self._equipment: Equipment = equipment
        self._performed_by: str = performed_by
        self._date: str = date
        self._description: str = description
        self._cost: float = cost

    @classmethod
    def _parse(cls, text: str) -> MaintenanceRecord:
        """Разобрать запись из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        equipment: Equipment = Equipment.from_string(parts[0])
        return cls(
            equipment=equipment,
            performed_by=parts[1],
            date=parts[2],
            description=parts[3],
            cost=float(parts[4]),
        )

    @property
    def cost(self) -> float:
        """Стоимость работ.

        Returns:
            Рубли.
        """
        return self._cost

    def is_expensive(self) -> bool:
        """Проверить, дорогое ли ТО.

        Returns:
            ``True``, если стоимость больше 50 000.
        """
        return self._cost > 50000

    def was_planned(self) -> bool:
        """Проверить, плановое ли ТО.

        Returns:
            ``True``, если описание содержит «планов».
        """
        return "планов" in self._description.lower()

    def __eq__(self, other: object) -> bool:
        """Сравнить две записи.

        Args:
            other: Другой объект.

        Returns:
            ``True``, если совпадают оборудование и дата.
        """
        if not isinstance(other, MaintenanceRecord):
            return NotImplemented
        return (
            self._equipment == other._equipment
            and self._date == other._date
        )

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash((self._equipment, self._date))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._equipment}; {self._performed_by}; "
            f"{self._date}; {self._description}; {self._cost}"
        )
