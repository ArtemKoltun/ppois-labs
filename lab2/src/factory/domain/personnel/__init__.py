"""
Доменные классы персонала.

Module: factory.domain.personnel
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.personnel.employee import Employee
from factory.domain.personnel.engineer import Engineer
from factory.domain.personnel.foreman import Foreman
from factory.domain.personnel.technologist import Technologist
from factory.domain.personnel.turner import Turner
from factory.domain.personnel.work_shift import WorkShift

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

__all__ = [
    "Employee",
    "Engineer",
    "Foreman",
    "Technologist",
    "Turner",
    "WorkShift",
]
