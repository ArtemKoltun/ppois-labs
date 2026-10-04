"""
Абстрактное оборудование завода.

Module: factory.domain.equipment.equipment
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.enums.equipment_status import EquipmentStatus
from common.exceptions.equipment_exceptions import (
    EquipmentBrokenError,
)

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Equipment(Readable, Writable):
    """Единица оборудования завода.

    Attributes:
        _name: Наименование.
        _inventory_number: Инвентарный номер.
        _status: Текущий статус.
        _purchase_year: Год покупки.
        _hours_worked: Отработано часов.
    """

    def __init__(
        self,
        name: str,
        inventory_number: str,
        purchase_year: int,
        status: EquipmentStatus = EquipmentStatus.IDLE,
    ) -> None:
        """Создать оборудование.

        Args:
            name: Наименование.
            inventory_number: Инвентарный номер.
            purchase_year: Год покупки.
            status: Начальный статус.

        Raises:
            ValueError: Если данные некорректны.
        """
        if not name or not inventory_number:
            raise ValueError("имя и номер не могут быть пустыми")
        self._name: str = name
        self._inventory_number: str = inventory_number
        self._status: EquipmentStatus = status
        self._purchase_year: int = purchase_year
        self._hours_worked: float = 0.0

    @classmethod
    def _parse(cls, text: str) -> Equipment:
        """Разобрать оборудование из строки.

        Args:
            text: Строка с полями через запятую.

        Returns:
            Новый экземпляр ``Equipment``.
        """
        parts: list[str] = [p.strip() for p in text.split(",")]
        return cls(
            name=parts[0],
            inventory_number=parts[1],
            purchase_year=int(parts[2]),
            status=EquipmentStatus(parts[3]),
        )

    @property
    def name(self) -> str:
        """Наименование.

        Returns:
            Строка.
        """
        return self._name

    @property
    def status(self) -> EquipmentStatus:
        """Текущий статус.

        Returns:
            Элемент перечисления.
        """
        return self._status

    @property
    def hours_worked(self) -> float:
        """Отработано часов.

        Returns:
            Число часов.
        """
        return self._hours_worked

    def start(self) -> None:
        """Запустить оборудование.

        Returns:
            Ничего не возвращает.

        Raises:
            EquipmentBrokenError: Если оборудование сломано.
        """
        if self._status is EquipmentStatus.BROKEN:
            raise EquipmentBrokenError(
                f"оборудование {self._name} сломано"
            )
        self._status = EquipmentStatus.WORKING

    def stop(self) -> None:
        """Остановить оборудование.

        Returns:
            Ничего не возвращает.
        """
        self._status = EquipmentStatus.IDLE

    def add_hours(self, hours: float) -> None:
        """Добавить отработанные часы.

        Args:
            hours: Число часов.

        Returns:
            Ничего не возвращает.
        """
        self._hours_worked += hours

    def mark_broken(self) -> None:
        """Пометить оборудование как сломанное.

        Returns:
            Ничего не возвращает.
        """
        self._status = EquipmentStatus.BROKEN

    def is_available(self) -> bool:
        """Проверить доступность для работы.

        Returns:
            ``True``, если статус не сломан и не на обслуживании.
        """
        return self._status in (
            EquipmentStatus.IDLE,
            EquipmentStatus.WORKING,
        )

    def __eq__(self, other: object) -> bool:
        """Сравнить две единицы оборудования.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении инвентарных номеров.
        """
        if not isinstance(other, Equipment):
            return NotImplemented
        return self._inventory_number == other._inventory_number

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._inventory_number)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через запятую.
        """
        return (
            f"{self._name}, {self._inventory_number}, "
            f"{self._purchase_year}, {self._status.value}"
        )
