"""
Тесты класса Gear.

Module: tests.factory.domain.parts.test_gear
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.parts.gear import Gear
from factory.domain.parts.part import Part

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_gear(base: Part, teeth: int = 20) -> Gear:
    """Создать шестерню.

    Args:
        base: Базовая деталь.
        teeth: Число зубьев.

    Returns:
        Объект ``Gear``.
    """
    return Gear(
        part=base,
        teeth_count=teeth,
        module=2.0,
        outer_diameter=44.0,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestGear:
    """Проверки класса Gear."""

    def test_creates(self, piston_part: Part) -> None:
        """Шестерня создаётся.

        Args:
            piston_part: Фикстура детали.
        """
        gear: Gear = _make_gear(piston_part)
        assert gear.name == "Поршень"

    def test_pitch_diameter(self, piston_part: Part) -> None:
        """pitch_diameter считает делительный диаметр.

        Args:
            piston_part: Фикстура детали.
        """
        gear: Gear = _make_gear(piston_part, teeth=20)
        assert gear.pitch_diameter() == 40.0

    def test_is_reduction_gear(self, piston_part: Part) -> None:
        """is_reduction_gear сравнивает число зубьев.

        Args:
            piston_part: Фикстура детали.
        """
        big: Gear = _make_gear(piston_part, teeth=40)
        small: Gear = _make_gear(piston_part, teeth=20)
        assert big.is_reduction_gear(small)
        assert not small.is_reduction_gear(big)
