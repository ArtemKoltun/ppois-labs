"""
Статистика завода.

Module: factory.domain.management.statistics
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from factory.domain.orders.order import Order
from factory.domain.workshops.production_order import ProductionOrder

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Statistics(Readable, Writable):
    """Статистика работы завода.

    Attributes:
        _period: Период (например, «2026-01»).
        _orders: Заказы клиентов.
        _production_orders: Заказы на производство.
        _defects_count: Число бракованных деталей.
    """

    def __init__(
        self,
        period: str,
        defects_count: int = 0,
    ) -> None:
        """Создать статистику.

        Args:
            period: Период.
            defects_count: Число бракованных деталей.
        """
        self._period: str = period
        self._orders: list[Order] = []
        self._production_orders: list[ProductionOrder] = []
        self._defects_count: int = defects_count

    @classmethod
    def _parse(cls, text: str) -> Statistics:
        """Разобрать статистику из строки.

        Args:
            text: Строка с полями через запятую.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(",")]
        return cls(
            period=parts[0],
            defects_count=int(parts[1]),
        )

    @property
    def period(self) -> str:
        """Период.

        Returns:
            Строка.
        """
        return self._period

    @property
    def defects_count(self) -> int:
        """Число бракованных деталей.

        Returns:
            Целое число.
        """
        return self._defects_count

    def add_order(self, order: Order) -> None:
        """Добавить заказ клиента.

        Args:
            order: Заказ.

        Returns:
            Ничего не возвращает.
        """
        self._orders.append(order)

    def add_production_order(
        self,
        production_order: ProductionOrder,
    ) -> None:
        """Добавить заказ на производство.

        Args:
            production_order: Заказ на производство.

        Returns:
            Ничего не возвращает.
        """
        self._production_orders.append(production_order)

    def record_defects(self, count: int) -> None:
        """Записать число бракованных деталей.

        Args:
            count: Число бракованных.

        Returns:
            Ничего не возвращает.
        """
        self._defects_count += count

    def total_orders(self) -> int:
        """Вернуть число заказов клиентов.

        Returns:
            Целое число.
        """
        return len(self._orders)

    def total_production(self) -> int:
        """Вернуть число заказов на производство.

        Returns:
            Целое число.
        """
        return len(self._production_orders)

    def total_produced_quantity(self) -> int:
        """Суммарное произведённое количество.

        Returns:
            Целое число.
        """
        return sum(
            po.quantity for po in self._production_orders
        )

    def defect_rate(self) -> float:
        """Рассчитать долю брака.

        Returns:
            Число от 0 до 1.
        """
        total: int = self.total_produced_quantity()
        if total == 0:
            return 0.0
        return self._defects_count / total

    def is_high_defect_rate(self) -> bool:
        """Проверить высокий уровень брака.

        Returns:
            ``True``, если доля брака больше 5%.
        """
        return self.defect_rate() > 0.05

    def __eq__(self, other: object) -> bool:
        """Сравнить две статистики.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении периода.
        """
        if not isinstance(other, Statistics):
            return NotImplemented
        return self._period == other._period

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._period)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через запятую.
        """
        return f"{self._period}, {self._defects_count}"
