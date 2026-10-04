"""
Тесты класса Shaft.

Module: tests.factory.domain.parts.test_shaft
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.parts.part import Part
from factory.domain.parts.shaft import Shaft

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_shaft(
    base: Part,
    length: float = 100.0,
    diameter: float = 20.0,
) -> Shaft:
    """Создать вал.

    Args:
        base: Базовая деталь.
        length: Длина.
        diameter: Диаметр.

    Returns:
        Объект ``Shaft``.
    """
    return Shaft(
        part=base,
        length=length,
        diameter=diameter,
        material_grade="40Х",
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestShaft:
    """Проверки класса Shaft."""

    def test_creates(self, piston_part: Part) -> None:
        """Вал создаётся.

        Args:
            piston_part: Фикстура детали.
        """
        shaft: Shaft = _make_shaft(piston_part)
        assert shaft.name == "Поршень"

    def test_aspect_ratio(self, piston_part: Part) -> None:
        """aspect_ratio считает отношение длины к диаметру.

        Args:
            piston_part: Фикстура детали.
        """
        shaft: Shaft = _make_shaft(
            piston_part, length=100.0, diameter=20.0
        )
        assert shaft.aspect_ratio() == 5.0

    def test_is_flexible(self, piston_part: Part) -> None:
        """is_flexible проверяет гибкость.

        Args:
            piston_part: Фикстура детали.
        """
        rigid: Shaft = _make_shaft(
            piston_part, length=100.0, diameter=20.0
        )
        flexible: Shaft = _make_shaft(
            piston_part, length=500.0, diameter=20.0
        )
        assert not rigid.is_flexible()
        assert flexible.is_flexible()
