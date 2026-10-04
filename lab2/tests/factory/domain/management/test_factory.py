"""
Тесты класса Factory.

Module: tests.factory.domain.management.test_factory
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.domain.address import Address
from factory.domain.management.department import Department
from factory.domain.management.factory import Factory
from factory.domain.orders.order import Order
from factory.domain.warehouse.warehouse import Warehouse
from factory.domain.workshops.workshop import Workshop


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_factory(address: Address) -> Factory:
    """Создать завод.

    Args:
        address: Адрес.

    Returns:
        Объект ``Factory``.
    """
    return Factory(name="Автодеталь", address=address)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestFactory:
    """Проверки класса Factory."""

    def test_creates(self, address: Address) -> None:
        """Завод создаётся.

        Args:
            address: Фикстура адреса.
        """
        factory: Factory = _make_factory(address)
        assert factory.name == "Автодеталь"

    def test_empty_name_raises(self, address: Address) -> None:
        """Пустое имя недопустимо.

        Args:
            address: Фикстура адреса.
        """
        with pytest.raises(ValueError):
            Factory(name="", address=address)

    def test_add_workshop(
        self,
        address: Address,
        workshop: Workshop,
    ) -> None:
        """add_workshop добавляет.

        Args:
            address: Фикстура адреса.
            workshop: Фикстура цеха.
        """
        factory: Factory = _make_factory(address)
        factory.add_workshop(workshop)
        assert factory.workshops_count() == 1

    def test_add_warehouse(
        self,
        address: Address,
        employee: object,
    ) -> None:
        """add_warehouse добавляет.

        Args:
            address: Фикстура адреса.
            employee: Фикстура сотрудника (не используется).
        """
        factory: Factory = _make_factory(address)
        warehouse: Warehouse = Warehouse(
            name="Склад",
            address=address,
            area=100.0,
            capacity=1000.0,
        )
        factory.add_warehouse(warehouse)
        assert factory.warehouses_count() == 1

    def test_add_department(
        self,
        address: Address,
        department: Department,
    ) -> None:
        """add_department добавляет.

        Args:
            address: Фикстура адреса.
            department: Фикстура отдела.
        """
        factory: Factory = _make_factory(address)
        factory.add_department(department)
        assert factory.departments_count() == 1

    def test_accept_order(
        self,
        address: Address,
        order: Order,
    ) -> None:
        """accept_order принимает заказ.

        Args:
            address: Фикстура адреса.
            order: Фикстура заказа.
        """
        factory: Factory = _make_factory(address)
        factory.accept_order(order)
        assert factory.orders_count() == 1

    def test_active_orders_count(
        self,
        address: Address,
        order: Order,
    ) -> None:
        """active_orders_count считает активные.

        Args:
            address: Фикстура адреса.
            order: Фикстура заказа.
        """
        factory: Factory = _make_factory(address)
        factory.accept_order(order)
        assert factory.active_orders_count() == 1
        order.cancel()
        assert factory.active_orders_count() == 0

    def test_equality(self, address: Address) -> None:
        """Равные по имени.

        Args:
            address: Фикстура адреса.
        """
        a: Factory = _make_factory(address)
        b: Factory = _make_factory(address)
        assert a == b
        assert a != "not factory"

    def test_hash(self, address: Address) -> None:
        """Хеш по имени.

        Args:
            address: Фикстура адреса.
        """
        a: Factory = _make_factory(address)
        b: Factory = _make_factory(address)
        assert hash(a) == hash(b)

    def test_str(self, address: Address) -> None:
        """str содержит имя.

        Args:
            address: Фикстура адреса.
        """
        factory: Factory = _make_factory(address)
        assert "Автодеталь" in str(factory)
