"""
Исключения, связанные с материалами.

Module: common.exceptions.material_exceptions
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.exceptions.base import FactoryException


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class InvalidMaterialException(FactoryException):
    """Некорректные данные материала."""


class InsufficientMaterialException(FactoryException):
    """Недостаточно материала на складе."""
