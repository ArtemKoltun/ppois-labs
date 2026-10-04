"""
Тесты класса Steel.

Module: tests.factory.domain.materials.test_steel
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.materials.material import Material
from factory.domain.materials.steel import Steel

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_steel(
    base: Material,
    grade: str = "45",
    hardness: float = 60.0,
) -> Steel:
    """Создать сталь.

    Args:
        base: Базовый материал.
        grade: Марка.
        hardness: Твёрдость.

    Returns:
        Объект ``Steel``.
    """
    return Steel(material=base, grade=grade, hardness=hardness)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestSteel:
    """Проверки класса Steel."""

    def test_creates(self, steel: Material) -> None:
        """Сталь создаётся.

        Args:
            steel: Фикстура материала.
        """
        s: Steel = _make_steel(steel)
        assert s.name == "Сталь 45"

    def test_is_hardened(self, steel: Material) -> None:
        """is_hardened проверяет твёрдость.

        Args:
            steel: Фикстура материала.
        """
        hard: Steel = _make_steel(steel, hardness=60.0)
        soft: Steel = _make_steel(steel, hardness=30.0)
        assert hard.is_hardened()
        assert not soft.is_hardened()

    def test_is_stainless(self, steel: Material) -> None:
        """is_stainless проверяет марку.

        Args:
            steel: Фикстура материала.
        """
        stainless: Steel = _make_steel(steel, grade="12Х18Н10Т")
        normal: Steel = _make_steel(steel, grade="45")
        assert stainless.is_stainless()
        assert not normal.is_stainless()
