"""
Виджеты консольного интерфейса, общие для модулей проекта.

Module: common.ui
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.ui.menu import Menu
from common.ui.menu import MenuItem
from common.ui.prompts import ask_int
from common.ui.prompts import ask_str
from common.ui.prompts import confirm


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

__all__ = ["Menu", "MenuItem", "ask_int", "ask_str", "confirm"]
