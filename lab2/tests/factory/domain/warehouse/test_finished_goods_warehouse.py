"""
Тесты класса FinishedGoodsWarehouse.

Module: tests.factory.domain.warehouse.test_finished_goods_warehouse
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.domain.address import Address
from factory.domain.parts.part import Part
from factory.domain.warehouse.finished_goods_warehouse import (
    FinishedGoodsWarehouse,
)
from factory.domain.warehouse.warehouse import Warehouse


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_finished(
    address: Address,
    dock: bool = True,
) -> FinishedGoodsWarehouse:
    """Создать склад готовой продукции.

    Args:
        address: Адрес.
        dock: Наличие отгрузочной площадки.

    Returns:
        Объект ``FinishedGoodsWarehouse``.
    """
    base: Warehouse = Warehouse(
        name="Готовой продукции",
        address=address,
        area=800.0,
        capacity=8000.0,
    )
    return FinishedGoodsWarehouse(
        warehouse=base,
        shipping_dock=dock,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestFinishedGoodsWarehouse:
    """Проверки класса FinishedGoodsWarehouse."""

    def test_creates(self, address: Address) -> None:
        """Склад создаётся.

        Args:
            address: Фикстура адреса.
        """
        f: FinishedGoodsWarehouse = _make_finished(address)
        assert f.parts_count() == 0

    def test_accept_part(
        self,
        address: Address,
        piston_part: Part,
    ) -> None:
        """accept_part добавляет деталь.

        Args:
            address: Фикстура адреса.
            piston_part: Фикстура детали.
        """
        f: FinishedGoodsWarehouse = _make_finished(address)
        f.accept_part(piston_part)
        assert f.parts_count() == 1

    def test_ship(self, address: Address, piston_part: Part) -> None:
        """ship отгружает.

        Args:
            address: Фикстура адреса.
            piston_part: Фикстура детали.
        """
        f: FinishedGoodsWarehouse = _make_finished(address)
        f.accept_part(piston_part)
        assert f.ship(piston_part)
        assert f.parts_count() == 0

    def test_ship_missing(self, address: Address, piston_part: Part) -> None:
        """ship отсутствующей детали.

        Args:
            address: Фикстура адреса.
            piston_part: Фикстура детали.
        """
        f: FinishedGoodsWarehouse = _make_finished(address)
        assert not f.ship(piston_part)

    def test_can_ship(self, address: Address) -> None:
        """can_ship проверяет площадку.

        Args:
            address: Фикстура адреса.
        """
        with_dock: FinishedGoodsWarehouse = _make_finished(
            address, dock=True
        )
        without: FinishedGoodsWarehouse = _make_finished(
            address, dock=False
        )
        assert with_dock.can_ship()
        assert not without.can_ship()
