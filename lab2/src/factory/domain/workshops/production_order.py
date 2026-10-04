"""
Заказ на производство.

Module: factory.domain.workshops.production_order
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.enums.order_status import OrderStatus
from factory.domain.parts.part import Part
from factory.domain.workshops.production_process import ProductionProcess


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class ProductionOrder(Readable, Writable):
    """Заказ на изготовление партии деталей.

    Attributes:
        _number: Номер заказа.
        _part: Изготавливаемая деталь.
        _quantity: Количество деталей.
        _process: Технологический процесс.
        _status: Статус заказа.
        _deadline: Срок выполнения.
    """

    def __init__(
        self,
        number: str,
        part: Part,
        quantity: int,
        process: ProductionProcess,
        deadline: str,
    ) -> None:
        """Создать заказ на производство.

        Args:
            number: Номер.
            part: Деталь.
            quantity: Количество.
            process: Техпроцесс.
            deadline: Срок.

        Raises:
            ValueError: Если данные некорректны.
        """
        if quantity <= 0:
            raise ValueError("количество должно быть положительным")
        self._number: str = number
        self._part: Part = part
        self._quantity: int = quantity
        self._process: ProductionProcess = process
        self._status: OrderStatus = OrderStatus.NEW
        self._deadline: str = deadline

    @classmethod
    def _parse(cls, text: str) -> "ProductionOrder":
        """Разобрать заказ из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        part: Part = Part.from_string(parts[1])
        process: ProductionProcess = ProductionProcess.from_string(
            parts[3]
        )
        return cls(
            number=parts[0],
            part=part,
            quantity=int(parts[2]),
            process=process,
            deadline=parts[4],
        )

    @property
    def number(self) -> str:
        """Номер заказа.

        Returns:
            Строка.
        """
        return self._number

    @property
    def status(self) -> OrderStatus:
        """Статус заказа.

        Returns:
            Элемент перечисления.
        """
        return self._status

    @property
    def quantity(self) -> int:
        """Количество деталей.

        Returns:
            Целое число.
        """
        return self._quantity

    def start(self) -> None:
        """Запустить заказ в производство.

        Returns:
            Ничего не возвращает.
        """
        self._status = OrderStatus.IN_PROGRESS

    def complete(self) -> None:
        """Завершить заказ.

        Returns:
            Ничего не возвращает.
        """
        self._status = OrderStatus.COMPLETED

    def cancel(self) -> None:
        """Отменить заказ.

        Returns:
            Ничего не возвращает.
        """
        self._status = OrderStatus.CANCELLED

    def is_active(self) -> bool:
        """Проверить, активен ли заказ.

        Returns:
            ``True``, если заказ не завершён и не отменён.
        """
        return self._status in (
            OrderStatus.NEW,
            OrderStatus.IN_PROGRESS,
        )

    def estimated_hours(self) -> float:
        """Рассчитать оценку времени изготовления.

        Returns:
            Часы.
        """
        return self._process.total_duration() * self._quantity

    def __eq__(self, other: object) -> bool:
        """Сравнить два заказа.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении номеров.
        """
        if not isinstance(other, ProductionOrder):
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
            f"{self._number}; {self._part}; {self._quantity}; "
            f"{self._process}; {self._deadline}"
        )
