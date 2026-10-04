"""
Тесты класса FoundryShop.

Module: tests.factory.domain.workshops.test_foundry_shop
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.workshops.foundry_shop import FoundryShop
from factory.domain.workshops.workshop import Workshop


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_foundry(
    base: Workshop,
    furnaces: int = 3,
    temp: float = 1600.0,
) -> FoundryShop:
    """Создать литейный цех.

    Args:
        base: Базовый цех.
        furnaces: Число печей.
        temp: Максимальная температура.

    Returns:
        Объект ``FoundryShop``.
    """
    return FoundryShop(
        workshop=base,
        furnace_count=furnaces,
        max_temperature=temp,
        daily_capacity=10.0,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestFoundryShop:
    """Проверки класса FoundryShop."""

    def test_creates(self, workshop: Workshop) -> None:
        """Цех создаётся.

        Args:
            workshop: Фикстура цеха.
        """
        shop: FoundryShop = _make_foundry(workshop)
        assert shop.name == "Механический"

    def test_can_melt_steel(self, workshop: Workshop) -> None:
        """can_melt_steel проверяет температуру.

        Args:
            workshop: Фикстура цеха.
        """
        hot: FoundryShop = _make_foundry(workshop, temp=1600.0)
        cold: FoundryShop = _make_foundry(workshop, temp=1000.0)
        assert hot.can_melt_steel()
        assert not cold.can_melt_steel()

    def test_produce(self, workshop: Workshop) -> None:
        """produce считает выпуск.

        Args:
            workshop: Фикстура цеха.
        """
        shop: FoundryShop = _make_foundry(workshop)
        assert shop.produce(5) == 50.0

    def test_is_large(self, workshop: Workshop) -> None:
        """is_large проверяет число печей.

        Args:
            workshop: Фикстура цеха.
        """
        small: FoundryShop = _make_foundry(workshop, furnaces=2)
        big: FoundryShop = _make_foundry(workshop, furnaces=5)
        assert not small.is_large()
        assert big.is_large()
