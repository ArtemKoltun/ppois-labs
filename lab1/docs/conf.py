"""
Конфигурация Sphinx для документации лабораторной работы №1.

Module: docs.conf
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Path setup
# ---------------------------------------------------------------------------

sys.path.insert(
    0,
    str(Path(__file__).resolve().parent.parent / "src"),
)


# ---------------------------------------------------------------------------
# Project information
# ---------------------------------------------------------------------------

project = "PPOIS Lab 1"
copyright = "2026"
author = "Студент"
release = "0.1.0"


# ---------------------------------------------------------------------------
# Sphinx configuration
# ---------------------------------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "show-inheritance": True,
    "member-order": "bysource",
}

napoleon_google_docstring = True
napoleon_numpy_docstring = False

exclude_patterns = ["_build"]

html_theme = "alabaster"

language = "ru"
