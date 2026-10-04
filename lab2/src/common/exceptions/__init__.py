"""
Все исключения предметной области.

Module: common.exceptions
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.exceptions.base import FactoryException
from common.exceptions.employee_exceptions import (
    EmployeeNotAvailableException,
)
from common.exceptions.equipment_exceptions import (
    EquipmentBrokenException,
)
from common.exceptions.equipment_exceptions import (
    EquipmentNotAvailableException,
)
from common.exceptions.material_exceptions import (
    InsufficientMaterialException,
)
from common.exceptions.material_exceptions import (
    InvalidMaterialException,
)
from common.exceptions.order_exceptions import (
    InvalidOrderException,
)
from common.exceptions.order_exceptions import (
    OrderNotFoundException,
)
from common.exceptions.order_exceptions import (
    ProductionDeadlineMissedException,
)
from common.exceptions.part_exceptions import (
    InvalidPartException,
)
from common.exceptions.part_exceptions import (
    InvalidSpecificationException,
)
from common.exceptions.part_exceptions import (
    QualityControlFailedException,
)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

__all__ = [
    "EmployeeNotAvailableException",
    "EquipmentBrokenException",
    "EquipmentNotAvailableException",
    "FactoryException",
    "InsufficientMaterialException",
    "InvalidMaterialException",
    "InvalidOrderException",
    "InvalidPartException",
    "InvalidSpecificationException",
    "OrderNotFoundException",
    "ProductionDeadlineMissedException",
    "QualityControlFailedException",
]
