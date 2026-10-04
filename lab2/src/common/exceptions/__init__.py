"""
Все исключения предметной области.

Module: common.exceptions
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.exceptions.base import FactoryError
from common.exceptions.employee_exceptions import (
    EmployeeNotAvailableError,
)
from common.exceptions.equipment_exceptions import (
    EquipmentBrokenError,
    EquipmentNotAvailableError,
)
from common.exceptions.material_exceptions import (
    InsufficientMaterialError,
    InvalidMaterialError,
)
from common.exceptions.order_exceptions import (
    InvalidOrderError,
    OrderNotFoundError,
    ProductionDeadlineMissedError,
)
from common.exceptions.part_exceptions import (
    InvalidPartError,
    InvalidSpecificationError,
    QualityControlFailedError,
)

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

__all__ = [
    "EmployeeNotAvailableError",
    "EquipmentBrokenError",
    "EquipmentNotAvailableError",
    "FactoryError",
    "InsufficientMaterialError",
    "InvalidMaterialError",
    "InvalidOrderError",
    "InvalidPartError",
    "InvalidSpecificationError",
    "OrderNotFoundError",
    "ProductionDeadlineMissedError",
    "QualityControlFailedError",
]
