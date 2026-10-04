"""
Статус заказа на производство.

Module: common.enums.order_status
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from enum import Enum

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class OrderStatus(Enum):
    """Статус заказа на производство.

    Attributes:
        NEW: Заказ создан, но не запущен.
        IN_PROGRESS: Заказ в производстве.
        COMPLETED: Заказ выполнен.
        SHIPPED: Заказ отгружен клиенту.
        CANCELLED: Заказ отменён.
    """

    NEW = "new"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"

    def __str__(self) -> str:
        """Вернуть человекочитаемое название статуса.

        Returns:
            Строка на русском.
        """
        names: dict[OrderStatus, str] = {
            OrderStatus.NEW: "новый",
            OrderStatus.IN_PROGRESS: "в производстве",
            OrderStatus.COMPLETED: "выполнен",
            OrderStatus.SHIPPED: "отгружен",
            OrderStatus.CANCELLED: "отменён",
        }
        return names[self]
