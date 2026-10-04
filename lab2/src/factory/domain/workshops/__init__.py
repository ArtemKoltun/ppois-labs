"""
Доменные классы цехов и производства.

Module: factory.domain.workshops
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.workshops.assembly_shop import AssemblyShop
from factory.domain.workshops.foundry_shop import FoundryShop
from factory.domain.workshops.machining_shop import MachiningShop
from factory.domain.workshops.production_order import ProductionOrder
from factory.domain.workshops.production_process import (
    ProductionProcess,
)
from factory.domain.workshops.quality_inspection import (
    QualityInspection,
)
from factory.domain.workshops.workshop import Workshop

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

__all__ = [
    "AssemblyShop",
    "FoundryShop",
    "MachiningShop",
    "ProductionOrder",
    "ProductionProcess",
    "QualityInspection",
    "Workshop",
]
