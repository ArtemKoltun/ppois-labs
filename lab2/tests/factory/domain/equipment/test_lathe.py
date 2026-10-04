"""
Тесты класса Lathe.

Module: tests.factory.domain.equipment.test_lathe
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.equipment.lathe import Lathe
from factory.domain.equipment.machine import Machine


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_lathe(base: Machine, diameter: float = 400.0) -> Lathe:
    """Создать токарный станок.

    Args:
        base: Базовый станок.
        diameter: Максимальный диаметр.

    Returns:
        Объект ``Lathe``.
    """
    return Lathe(
        machine=base,
        max_diameter=diameter,
        max_length=1000.0,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestLathe:
    """Проверки класса Lathe."""

    def test_creates(self, machine: Machine) -> None:
        """Станок создаётся.

        Args:
            machine: Фикстура станка.
        """
        lathe: Lathe = _make_lathe(machine)
        assert lathe.name == "Токарный 16К20"

    def test_can_process(self, machine: Machine) -> None:
        """can_process проверяет размеры.

        Args:
            machine: Фикстура станка.
        """
        lathe: Lathe = _make_lathe(machine, diameter=400.0)
        assert lathe.can_process(diameter=300.0, length=500.0)
        assert not lathe.can_process(diameter=500.0, length=500.0)

    def test_is_large_lathe(self, machine: Machine) -> None:
        """is_large_lathe проверяет диаметр.

        Args:
            machine: Фикстура станка.
        """
        small: Lathe = _make_lathe(machine, diameter=300.0)
        big: Lathe = _make_lathe(machine, diameter=500.0)
        assert not small.is_large_lathe()
        assert big.is_large_lathe()
