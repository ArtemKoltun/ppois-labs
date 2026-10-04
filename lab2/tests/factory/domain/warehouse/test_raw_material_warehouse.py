"""
Тесты класса RawMaterialWarehouse.

Module: tests.factory.domain.warehouse.test_raw_material_warehouse
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.domain.address import Address
from factory.domain.materials.material import Material
from factory.domain.warehouse.raw_material_warehouse import (
    RawMaterialWarehouse,
)
from factory.domain.warehouse.warehouse import Warehouse


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_base(address: Address) -> Warehouse:
    """Создать базовый склад.

    Args:
        address: Адрес.

    Returns:
        Объект ``Warehouse``.
    """
    return Warehouse(
        name="Сырьевой",
        address=address,
        area=500.0,
        capacity=5000.0,
    )


def _make_raw(
    address: Address,
    temp: float = 5.0,
) -> RawMaterialWarehouse:
    """Создать склад сырья.

    Args:
        address: Адрес.
        temp: Минимальная температура.

    Returns:
        Объект ``RawMaterialWarehouse``.
    """
    return RawMaterialWarehouse(
        warehouse=_make_base(address),
        min_temperature=temp,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestRawMaterialWarehouse:
    """Проверки класса RawMaterialWarehouse."""

    def test_creates(self, address: Address) -> None:
        """Склад создаётся.

        Args:
            address: Фикстура адреса.
        """
        raw: RawMaterialWarehouse = _make_raw(address)
        assert raw.name == "Сырьевой"
        assert raw.materials_count() == 0

    def test_accept_material(
        self,
        address: Address,
        steel: Material,
    ) -> None:
        """accept_material добавляет.

        Args:
            address: Фикстура адреса.
            steel: Фикстура материала.
        """
        raw: RawMaterialWarehouse = _make_raw(address)
        raw.accept_material(steel)
        assert raw.materials_count() == 1
        assert raw.has_material(steel)

    def test_needs_heating(self, address: Address) -> None:
        """needs_heating проверяет температуру.

        Args:
            address: Фикстура адреса.
        """
        warm: RawMaterialWarehouse = _make_raw(address, temp=15.0)
        cold: RawMaterialWarehouse = _make_raw(address, temp=5.0)
        assert warm.needs_heating()
        assert not cold.needs_heating()
