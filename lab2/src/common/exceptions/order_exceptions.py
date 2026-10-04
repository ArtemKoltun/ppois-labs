"""
Исключения, связанные с заказами.

Module: common.exceptions.order_exceptions
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.exceptions.base import FactoryError

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class OrderNotFoundError(FactoryError):
    """Заказ не найден."""


class InvalidOrderError(FactoryError):
    """Некорректные данные заказа."""


class ProductionDeadlineMissedError(FactoryError):
    """Срок производства заказа пропущен."""
