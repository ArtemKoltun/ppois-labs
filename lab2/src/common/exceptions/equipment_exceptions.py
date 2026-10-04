"""
Исключения, связанные с оборудованием.

Module: common.exceptions.equipment_exceptions
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.exceptions.base import FactoryException


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class EquipmentBrokenException(FactoryException):
    """Оборудование сломано."""


class EquipmentNotAvailableException(FactoryException):
    """Оборудование занято или недоступно."""
