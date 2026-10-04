"""
Тесты класса MachiningShop.

Module: tests.factory.domain.workshops.test_machining_shop
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.workshops.machining_shop import MachiningShop
from factory.domain.workshops.workshop import Workshop

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_machining(
    base: Workshop,
    machines: int = 10,
    shifts: int = 2,
) -> MachiningShop:
    """Создать механический цех.

    Args:
        base: Базовый цех.
        machines: Число станков.
        shifts: Число смен.

    Returns:
        Объект ``MachiningShop``.
    """
    return MachiningShop(
        workshop=base,
        machine_count=machines,
        shifts=shifts,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestMachiningShop:
    """Проверки класса MachiningShop."""

    def test_creates(self, workshop: Workshop) -> None:
        """Цех создаётся.

        Args:
            workshop: Фикстура цеха.
        """
        shop: MachiningShop = _make_machining(workshop)
        assert shop.name == "Механический"

    def test_daily_capacity(self, workshop: Workshop) -> None:
        """daily_capacity считает производительность.

        Args:
            workshop: Фикстура цеха.
        """
        shop: MachiningShop = _make_machining(
            workshop, machines=10, shifts=2
        )
        assert shop.daily_capacity() == 160

    def test_is_round_the_clock(self, workshop: Workshop) -> None:
        """is_round_the_clock проверяет смены.

        Args:
            workshop: Фикстура цеха.
        """
        three: MachiningShop = _make_machining(workshop, shifts=3)
        two: MachiningShop = _make_machining(workshop, shifts=2)
        assert three.is_round_the_clock()
        assert not two.is_round_the_clock()

    def test_is_highly_automated(self, workshop: Workshop) -> None:
        """is_highly_automated проверяет станки.

        Args:
            workshop: Фикстура цеха.
        """
        many: MachiningShop = _make_machining(workshop, machines=30)
        few: MachiningShop = _make_machining(workshop, machines=5)
        assert many.is_highly_automated()
        assert not few.is_highly_automated()
