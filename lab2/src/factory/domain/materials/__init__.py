"""
Доменные классы материалов.

Module: factory.domain.materials
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.materials.aluminum import Aluminum
from factory.domain.materials.material import Material
from factory.domain.materials.material_batch import MaterialBatch
from factory.domain.materials.plastic import Plastic
from factory.domain.materials.steel import Steel
from factory.domain.materials.supplier import Supplier

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

__all__ = [
    "Aluminum",
    "Material",
    "MaterialBatch",
    "Plastic",
    "Steel",
    "Supplier",
]
