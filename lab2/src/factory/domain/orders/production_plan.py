"""
План производства.

Module: factory.domain.orders.production_plan
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from factory.domain.orders.order import Order
from factory.domain.workshops.workshop import Workshop


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class ProductionPlan(Readable, Writable):
    """План производства на период.

    Attributes:
        _period: Период (например, «2026-Q1»).
        _orders: Список заказов.
        _workshop: Ответственный цех.
        _target_output: Плановый выпуск.
    """

    def __init__(
        self,
        period: str,
        workshop: Workshop,
        target_output: int = 0,
    ) -> None:
        """Создать план.

        Args:
            period: Период.
            workshop: Цех.
            target_output: Плановый выпуск.
        """
        self._period: str = period
        self._orders: list[Order] = []
        self._workshop: Workshop = workshop
        self._target_output: int = target_output

    @classmethod
    def _parse(cls, text: str) -> "ProductionPlan":
        """Разобрать план из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        workshop: Workshop = Workshop.from_string(parts[1])
        return cls(
            period=parts[0],
            workshop=workshop,
            target_output=int(parts[2]),
        )

    @property
    def period(self) -> str:
        """Период.

        Returns:
            Строка.
        """
        return self._period

    @property
    def target_output(self) -> int:
        """Плановый выпуск.

        Returns:
            Целое число.
        """
        return self._target_output

    def add_order(self, order: Order) -> None:
        """Добавить заказ в план.

        Args:
            order: Заказ.

        Returns:
            Ничего не возвращает.
        """
        self._orders.append(order)

    def remove_order(self, order: Order) -> None:
        """Убрать заказ из плана.

        Args:
            order: Заказ.

        Returns:
            Ничего не возвращает.
        """
        if order in self._orders:
            self._orders.remove(order)

    def orders_count(self) -> int:
        """Вернуть число заказов в плане.

        Returns:
            Целое число.
        """
        return len(self._orders)

    def planned_quantity(self) -> int:
        """Суммарное плановое количество деталей.

        Returns:
            Целое число.
        """
        return sum(order.quantity for order in self._orders)

    def is_overloaded(self) -> bool:
        """Проверить перегрузку плана.

        Returns:
            ``True``, если план превышает целевую мощность.
        """
        return self.planned_quantity() > self._target_output

    def __eq__(self, other: object) -> bool:
        """Сравнить два плана.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении периода и цеха.
        """
        if not isinstance(other, ProductionPlan):
            return NotImplemented
        return (
            self._period == other._period
            and self._workshop == other._workshop
        )

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash((self._period, self._workshop))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._period}; {self._workshop}; "
            f"{self._target_output}"
        )
