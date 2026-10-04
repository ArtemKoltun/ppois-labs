"""
Тесты класса AssemblyShop.

Module: tests.factory.domain.workshops.test_assembly_shop
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.workshops.assembly_shop import AssemblyShop
from factory.domain.workshops.workshop import Workshop


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_assembly(
    base: Workshop,
    conveyors: int = 3,
    lines: int = 2,
) -> AssemblyShop:
    """Создать сборочный цех.

    Args:
        base: Базовый цех.
        conveyors: Число конвейеров.
        lines: Число линий.

    Returns:
        Объект ``AssemblyShop``.
    """
    return AssemblyShop(
        workshop=base,
        conveyor_count=conveyors,
        assembly_lines=lines,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestAssemblyShop:
    """Проверки класса AssemblyShop."""

    def test_creates(self, workshop: Workshop) -> None:
        """Цех создаётся.

        Args:
            workshop: Фикстура цеха.
        """
        shop: AssemblyShop = _make_assembly(workshop)
        assert shop.name == "Механический"

    def test_total_lines(self, workshop: Workshop) -> None:
        """total_lines суммирует.

        Args:
            workshop: Фикстура цеха.
        """
        shop: AssemblyShop = _make_assembly(
            workshop, conveyors=3, lines=2
        )
        assert shop.total_lines() == 5

    def test_is_conveyor_type(self, workshop: Workshop) -> None:
        """is_conveyor_type проверяет конвейеры.

        Args:
            workshop: Фикстура цеха.
        """
        many: AssemblyShop = _make_assembly(workshop, conveyors=10)
        few: AssemblyShop = _make_assembly(workshop, conveyors=2)
        assert many.is_conveyor_type()
        assert not few.is_conveyor_type()

    def test_can_produce_in_parallel(self, workshop: Workshop) -> None:
        """can_produce_in_parallel проверяет линии.

        Args:
            workshop: Фикстура цеха.
        """
        multi: AssemblyShop = _make_assembly(workshop, lines=3)
        single: AssemblyShop = _make_assembly(workshop, lines=1)
        assert multi.can_produce_in_parallel()
        assert not single.can_produce_in_parallel()
