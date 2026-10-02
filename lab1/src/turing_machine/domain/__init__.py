"""
Доменные классы машины Тьюринга.

Module: turing_machine.domain
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.domain.alphabet import Alphabet
from turing_machine.domain.direction import Direction
from turing_machine.domain.head import Head
from turing_machine.domain.machine import TuringMachine
from turing_machine.domain.program import Program
from turing_machine.domain.transition import Transition
from turing_machine.domain.unbounded_tape import UnboundedTape


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

__all__ = [
    "Alphabet",
    "Direction",
    "Head",
    "Program",
    "Transition",
    "TuringMachine",
    "UnboundedTape",
]