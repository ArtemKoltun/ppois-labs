"""
Доменные классы оборудования.

Module: factory.domain.equipment
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.equipment.cnc_machine import CNCMachine
from factory.domain.equipment.equipment import Equipment
from factory.domain.equipment.lathe import Lathe
from factory.domain.equipment.machine import Machine
from factory.domain.equipment.maintenance_record import (
    MaintenanceRecord,
)
from factory.domain.equipment.milling_machine import MillingMachine


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

__all__ = [
    "CNCMachine",
    "Equipment",
    "Lathe",
    "Machine",
    "MaintenanceRecord",
    "MillingMachine",
]
