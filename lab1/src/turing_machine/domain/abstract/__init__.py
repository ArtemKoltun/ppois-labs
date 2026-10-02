"""
Абстрактные интерфейсы доменных классов машины Тьюринга.

Module: turing_machine.domain.abstract
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from turing_machine.domain.abstract.rule import AbstractRule
from turing_machine.domain.abstract.tape import AbstractTape


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

__all__ = ["AbstractRule", "AbstractTape"]
