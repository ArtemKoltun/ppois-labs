"""
Тесты класса Bearing.

Module: tests.factory.domain.parts.test_bearing
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.parts.bearing import Bearing
from factory.domain.parts.part import Part


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_bearing(
    base: Part,
    inner: float = 50.0,
    outer: float = 80.0,
) -> Bearing:
    """Создать подшипник.

    Args:
        base: Базовая деталь.
        inner: Внутренний диаметр.
        outer: Внешний диаметр.

    Returns:
        Объект ``Bearing``.
    """
    return Bearing(
        part=base,
        inner_diameter=inner,
        outer_diameter=outer,
        bearing_type="роликовый",
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestBearing:
    """Проверки класса Bearing."""

    def test_creates(self, piston_part: Part) -> None:
        """Подшипник создаётся.

        Args:
            piston_part: Фикстура детали.
        """
        bearing: Bearing = _make_bearing(piston_part)
        assert bearing.name == "Поршень"

    def test_is_small(self, piston_part: Part) -> None:
        """is_small проверяет внутренний диаметр.

        Args:
            piston_part: Фикстура детали.
        """
        small: Bearing = _make_bearing(piston_part, inner=50.0)
        large: Bearing = _make_bearing(piston_part, inner=150.0)
        assert small.is_small()
        assert not large.is_small()

    def test_ring_thickness(self, piston_part: Part) -> None:
        """ring_thickness считает толщину кольца.

        Args:
            piston_part: Фикстура детали.
        """
        bearing: Bearing = _make_bearing(
            piston_part, inner=50.0, outer=80.0
        )
        assert bearing.ring_thickness() == 15.0
