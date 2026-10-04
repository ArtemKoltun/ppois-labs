"""
Исключения, связанные с деталями.

Module: common.exceptions.part_exceptions
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.exceptions.base import FactoryException


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class InvalidPartException(FactoryException):
    """Некорректные данные детали."""


class InvalidSpecificationException(FactoryException):
    """Некорректная спецификация детали."""


class QualityControlFailedException(FactoryException):
    """Деталь не прошла контроль качества."""
