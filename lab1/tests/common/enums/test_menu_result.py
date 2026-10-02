"""
Тесты перечисления MenuResult.

Module: tests.common.enums.test_menu_result
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.enums.menu_result import MenuResult


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestMenuResult:
    """Проверки MenuResult."""

    def test_values(self) -> None:
        """Значения соответствуют строковым меткам."""
        assert MenuResult.CONTINUE.value == "continue"
        assert MenuResult.BACK.value == "back"
        assert MenuResult.EXIT.value == "exit"

    def test_distinct_members(self) -> None:
        """Элементы перечисления попарно различны."""
        results: set[MenuResult] = {
            MenuResult.CONTINUE,
            MenuResult.BACK,
            MenuResult.EXIT,
        }
        assert len(results) == 3
