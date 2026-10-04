"""
Тесты класса Piston.

Module: tests.factory.domain.parts.test_piston
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.parts.part import Part
from factory.domain.parts.piston import Piston

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_piston(base: Part, compression: float = 9.0) -> Piston:
    """Создать поршень с заданными параметрами.

    Args:
        base: Базовая деталь.
        compression: Степень сжатия.

    Returns:
        Объект ``Piston``.
    """
    return Piston(
        part=base,
        diameter=80.0,
        height=60.0,
        compression_ratio=compression,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestPiston:
    """Проверки класса Piston."""

    def test_creates(self, piston_part: Part) -> None:
        """Поршень создаётся на основе детали.

        Args:
            piston_part: Фикстура детали.
        """
        piston: Piston = _make_piston(piston_part)
        assert piston.name == "Поршень"

    def test_volume(self, piston_part: Part) -> None:
        """volume считает объём цилиндра.

        Args:
            piston_part: Фикстура детали.
        """
        piston: Piston = _make_piston(piston_part)
        volume: float = piston.volume()
        assert volume > 0

    def test_is_high_compression(self, piston_part: Part) -> None:
        """is_high_compression проверяет степень сжатия.

        Args:
            piston_part: Фикстура детали.
        """
        normal: Piston = _make_piston(piston_part, compression=9.0)
        high: Piston = _make_piston(piston_part, compression=12.0)
        assert not normal.is_high_compression()
        assert high.is_high_compression()
