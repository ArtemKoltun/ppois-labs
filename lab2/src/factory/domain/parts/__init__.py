"""
Доменные классы деталей.

Module: factory.domain.parts
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.parts.bearing import Bearing
from factory.domain.parts.cylinder import Cylinder
from factory.domain.parts.gear import Gear
from factory.domain.parts.part import Part
from factory.domain.parts.piston import Piston
from factory.domain.parts.shaft import Shaft
from factory.domain.parts.specification import Specification

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

__all__ = [
    "Bearing",
    "Cylinder",
    "Gear",
    "Part",
    "Piston",
    "Shaft",
    "Specification",
]
