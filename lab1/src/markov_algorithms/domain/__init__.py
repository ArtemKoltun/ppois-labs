"""
Доменные классы нормальных алгорифмов Маркова.

Module: markov_algorithms.domain
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from markov_algorithms.domain.algorithm import MarkovAlgorithm
from markov_algorithms.domain.program import Program
from markov_algorithms.domain.substitution import Substitution
from markov_algorithms.domain.word import Word

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

__all__ = ["MarkovAlgorithm", "Program", "Substitution", "Word"]
