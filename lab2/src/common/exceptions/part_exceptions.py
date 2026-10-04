"""
Исключения, связанные с деталями.

Module: common.exceptions.part_exceptions
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.exceptions.base import FactoryError

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class InvalidPartError(FactoryError):
    """Некорректные данные детали."""


class InvalidSpecificationError(FactoryError):
    """Некорректная спецификация детали."""


class QualityControlFailedError(FactoryError):
    """Деталь не прошла контроль качества."""
