"""
Тесты класса Aluminum.

Module: tests.factory.domain.materials.test_aluminum
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.enums.material_type import MaterialType
from factory.domain.materials.aluminum import Aluminum
from factory.domain.materials.material import Material

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_aluminum_base() -> Material:
    """Создать базовый алюминиевый материал.

    Returns:
        Объект ``Material``.
    """
    return Material(
        name="Алюминий АД31",
        material_type=MaterialType.ALUMINUM.value,
        density=2700.0,
        cost_per_kg=200.0,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestAluminum:
    """Проверки класса Aluminum."""

    def test_creates(self) -> None:
        """Алюминий создаётся."""
        al: Aluminum = Aluminum(
            material=_make_aluminum_base(),
            alloy="АД31",
            temper="T1",
        )
        assert al.name == "Алюминий АД31"

    def test_is_heat_treated(self) -> None:
        """is_heat_treated проверяет состояние."""
        treated: Aluminum = Aluminum(
            material=_make_aluminum_base(),
            alloy="АД31",
            temper="T6",
        )
        not_treated: Aluminum = Aluminum(
            material=_make_aluminum_base(),
            alloy="АД31",
            temper="O",
        )
        assert treated.is_heat_treated()
        assert not not_treated.is_heat_treated()

    def test_is_lightweight(self) -> None:
        """is_lightweight проверяет плотность."""
        al: Aluminum = Aluminum(
            material=_make_aluminum_base(),
            alloy="АД31",
            temper="T1",
        )
        assert al.is_lightweight()
