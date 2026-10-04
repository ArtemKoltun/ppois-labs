"""
Тесты класса Cylinder.

Module: tests.factory.domain.parts.test_cylinder
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.parts.cylinder import Cylinder
from factory.domain.parts.part import Part

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_cylinder(
    base: Part,
    wall: float = 7.0,
) -> Cylinder:
    """Создать цилиндр с заданными параметрами.

    Args:
        base: Базовая деталь.
        wall: Толщина стенки.

    Returns:
        Объект ``Cylinder``.
    """
    return Cylinder(
        part=base,
        diameter=80.0,
        height=100.0,
        wall_thickness=wall,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestCylinder:
    """Проверки класса Cylinder."""

    def test_creates(self, piston_part: Part) -> None:
        """Цилиндр создаётся.

        Args:
            piston_part: Фикстура детали.
        """
        cylinder: Cylinder = _make_cylinder(piston_part)
        assert cylinder.name == "Поршень"

    def test_internal_volume(self, piston_part: Part) -> None:
        """internal_volume считает объём.

        Args:
            piston_part: Фикстура детали.
        """
        cylinder: Cylinder = _make_cylinder(piston_part)
        assert cylinder.internal_volume() > 0

    def test_is_thin_walled(self, piston_part: Part) -> None:
        """is_thin_walled проверяет толщину стенки.

        Args:
            piston_part: Фикстура детали.
        """
        thick: Cylinder = _make_cylinder(piston_part, wall=10.0)
        thin: Cylinder = _make_cylinder(piston_part, wall=3.0)
        assert not thick.is_thin_walled()
        assert thin.is_thin_walled()
