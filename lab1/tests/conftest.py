"""
Общие фикстуры тестов.

Module: tests.conftest
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_EXAMPLES_ROOT: Path = (
    Path(__file__).resolve().parent.parent / "examples"
)
"""Корень папки с примерами."""


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def examples_root() -> Path:
    """Корень папки с примерами.

    Returns:
        Путь ``lab1/examples``.
    """
    return _EXAMPLES_ROOT


@pytest.fixture
def turing_examples(examples_root: Path) -> Path:
    """Папка с примерами машин Тьюринга.

    Args:
        examples_root: Корень папки с примерами.

    Returns:
        Путь ``lab1/examples/turing_machine``.
    """
    return examples_root / "turing_machine"


@pytest.fixture
def markov_examples(examples_root: Path) -> Path:
    """Папка с примерами нормальных алгорифмов Маркова.

    Args:
        examples_root: Корень папки с примерами.

    Returns:
        Путь ``lab1/examples/markov_algorithms``.
    """
    return examples_root / "markov_algorithms"
