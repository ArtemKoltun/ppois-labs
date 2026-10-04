"""
Исключения, связанные с заказами.

Module: common.exceptions.order_exceptions
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.exceptions.base import FactoryException


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class OrderNotFoundException(FactoryException):
    """Заказ не найден."""


class InvalidOrderException(FactoryException):
    """Некорректные данные заказа."""


class ProductionDeadlineMissedException(FactoryException):
    """Срок производства заказа пропущен."""
