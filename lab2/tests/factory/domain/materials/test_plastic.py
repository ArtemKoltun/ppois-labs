"""
Тесты класса Plastic.

Module: tests.factory.domain.materials.test_plastic
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.enums.material_type import MaterialType
from factory.domain.materials.material import Material
from factory.domain.materials.plastic import Plastic

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_plastic_base() -> Material:
    """Создать базовый пластиковый материал.

    Returns:
        Объект ``Material``.
    """
    return Material(
        name="Полипропилен",
        material_type=MaterialType.PLASTIC.value,
        density=900.0,
        cost_per_kg=150.0,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestPlastic:
    """Проверки класса Plastic."""

    def test_creates(self) -> None:
        """Пластик создаётся."""
        p: Plastic = Plastic(
            material=_make_plastic_base(),
            polymer_type="PP",
            melting_point=170.0,
        )
        assert p.name == "Полипропилен"

    def test_is_thermoplastic(self) -> None:
        """is_thermoplastic проверяет температуру плавления."""
        p: Plastic = Plastic(
            material=_make_plastic_base(),
            polymer_type="PP",
            melting_point=170.0,
        )
        assert p.is_thermoplastic()

    def test_is_recyclable(self) -> None:
        """is_recyclable проверяет тип полимера."""
        recyclable: Plastic = Plastic(
            material=_make_plastic_base(),
            polymer_type="PP",
            melting_point=170.0,
        )
        not_recyclable: Plastic = Plastic(
            material=_make_plastic_base(),
            polymer_type="PVC",
            melting_point=170.0,
        )
        assert recyclable.is_recyclable()
        assert not not_recyclable.is_recyclable()
