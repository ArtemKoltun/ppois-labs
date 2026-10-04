"""
Тесты класса Order.

Module: tests.factory.domain.orders.test_order
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.domain.money import Money
from common.enums.order_status import OrderStatus
from common.exceptions import InvalidOrderException
from factory.domain.orders.customer import Customer
from factory.domain.orders.order import Order
from factory.domain.parts.part import Part


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestOrder:
    """Проверки класса Order."""

    def test_creates(self, order: Order) -> None:
        """Заказ создаётся.

        Args:
            order: Фикстура заказа.
        """
        assert order.number == "ORD-001"
        assert order.quantity == 100
        assert order.status is OrderStatus.NEW

    def test_empty_number_raises(
        self,
        customer: Customer,
        piston_part: Part,
    ) -> None:
        """Пустой номер недопустим.

        Args:
            customer: Фикстура клиента.
            piston_part: Фикстура детали.
        """
        with pytest.raises(InvalidOrderException):
            Order(
                number="",
                customer=customer,
                part=piston_part,
                quantity=10,
                price=Money(amount=1.0),
                deadline="X",
                created_date="Y",
            )

    def test_zero_quantity_raises(
        self,
        customer: Customer,
        piston_part: Part,
    ) -> None:
        """Нулевое количество недопустимо.

        Args:
            customer: Фикстура клиента.
            piston_part: Фикстура детали.
        """
        with pytest.raises(InvalidOrderException):
            Order(
                number="X",
                customer=customer,
                part=piston_part,
                quantity=0,
                price=Money(amount=1.0),
                deadline="X",
                created_date="Y",
            )

    def test_total_price(self, order: Order) -> None:
        """total_price считает сумму.

        Args:
            order: Фикстура заказа.
        """
        total: Money = order.total_price()
        assert total.amount == 50000.0

    def test_start(self, order: Order) -> None:
        """start переводит в IN_PROGRESS.

        Args:
            order: Фикстура заказа.
        """
        order.start()
        assert order.status is OrderStatus.IN_PROGRESS

    def test_complete(self, order: Order) -> None:
        """complete переводит в COMPLETED.

        Args:
            order: Фикстура заказа.
        """
        order.complete()
        assert order.status is OrderStatus.COMPLETED

    def test_ship(self, order: Order) -> None:
        """ship переводит в SHIPPED.

        Args:
            order: Фикстура заказа.
        """
        order.ship()
        assert order.status is OrderStatus.SHIPPED

    def test_cancel(self, order: Order) -> None:
        """cancel переводит в CANCELLED.

        Args:
            order: Фикстура заказа.
        """
        order.cancel()
        assert order.status is OrderStatus.CANCELLED

    def test_is_active(self, order: Order) -> None:
        """is_active для NEW.

        Args:
            order: Фикстура заказа.
        """
        assert order.is_active()

    def test_is_not_active_after_cancel(self, order: Order) -> None:
        """Отменённый неактивен.

        Args:
            order: Фикстура заказа.
        """
        order.cancel()
        assert not order.is_active()

    def test_equality(self, order: Order) -> None:
        """Равные по номеру.

        Args:
            order: Фикстура заказа.
        """
        other: Order = Order(
            number="ORD-001",
            customer=order.customer,
            part=order._part,
            quantity=5,
            price=Money(amount=1.0),
            deadline="X",
            created_date="Y",
        )
        assert order == other

    def test_inequality(self, order: Order) -> None:
        """Разные заказы.

        Args:
            order: Фикстура заказа.
        """
        assert order != "not order"

    def test_hash(self, order: Order) -> None:
        """Хеш по номеру.

        Args:
            order: Фикстура заказа.
        """
        other: Order = Order(
            number="ORD-001",
            customer=order.customer,
            part=order._part,
            quantity=1,
            price=Money(amount=1.0),
            deadline="X",
            created_date="Y",
        )
        assert hash(order) == hash(other)

    def test_str(self, order: Order) -> None:
        """str возвращает номер.

        Args:
            order: Фикстура заказа.
        """
        assert "ORD-001" in str(order)
