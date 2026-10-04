"""
Тесты класса ProductionOrder.

Module: tests.factory.domain.workshops.test_production_order
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.enums.order_status import OrderStatus
from factory.domain.parts.part import Part
from factory.domain.workshops.production_order import ProductionOrder
from factory.domain.workshops.production_process import (
    ProductionProcess,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_process(part: Part) -> ProductionProcess:
    """Создать техпроцесс.

    Args:
        part: Деталь.

    Returns:
        Объект ``ProductionProcess``.
    """
    return ProductionProcess(
        name="Изготовление",
        part=part,
        duration_hours=2.0,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestProductionOrder:
    """Проверки класса ProductionOrder."""

    def test_creates(self, piston_part: Part) -> None:
        """Заказ создаётся.

        Args:
            piston_part: Фикстура детали.
        """
        order: ProductionOrder = ProductionOrder(
            number="PO-001",
            part=piston_part,
            quantity=10,
            process=_make_process(piston_part),
            deadline="2026-03-01",
        )
        assert order.number == "PO-001"
        assert order.quantity == 10
        assert order.status is OrderStatus.NEW

    def test_zero_quantity_raises(self, piston_part: Part) -> None:
        """Нулевое количество недопустимо.

        Args:
            piston_part: Фикстура детали.
        """
        with pytest.raises(ValueError):
            ProductionOrder(
                number="X",
                part=piston_part,
                quantity=0,
                process=_make_process(piston_part),
                deadline="2026-03-01",
            )

    def test_start(self, piston_part: Part) -> None:
        """start переводит в IN_PROGRESS.

        Args:
            piston_part: Фикстура детали.
        """
        order: ProductionOrder = ProductionOrder(
            number="X",
            part=piston_part,
            quantity=5,
            process=_make_process(piston_part),
            deadline="2026-03-01",
        )
        order.start()
        assert order.status is OrderStatus.IN_PROGRESS

    def test_complete(self, piston_part: Part) -> None:
        """complete переводит в COMPLETED.

        Args:
            piston_part: Фикстура детали.
        """
        order: ProductionOrder = ProductionOrder(
            number="X",
            part=piston_part,
            quantity=5,
            process=_make_process(piston_part),
            deadline="2026-03-01",
        )
        order.complete()
        assert order.status is OrderStatus.COMPLETED

    def test_cancel(self, piston_part: Part) -> None:
        """cancel переводит в CANCELLED.

        Args:
            piston_part: Фикстура детали.
        """
        order: ProductionOrder = ProductionOrder(
            number="X",
            part=piston_part,
            quantity=5,
            process=_make_process(piston_part),
            deadline="2026-03-01",
        )
        order.cancel()
        assert order.status is OrderStatus.CANCELLED

    def test_is_active(self, piston_part: Part) -> None:
        """is_active для NEW.

        Args:
            piston_part: Фикстура детали.
        """
        order: ProductionOrder = ProductionOrder(
            number="X",
            part=piston_part,
            quantity=5,
            process=_make_process(piston_part),
            deadline="2026-03-01",
        )
        assert order.is_active()

    def test_estimated_hours(self, piston_part: Part) -> None:
        """estimated_hours считает время.

        Args:
            piston_part: Фикстура детали.
        """
        order: ProductionOrder = ProductionOrder(
            number="X",
            part=piston_part,
            quantity=10,
            process=_make_process(piston_part),
            deadline="2026-03-01",
        )
        assert order.estimated_hours() == 20.0

    def test_equality(self, piston_part: Part) -> None:
        """Равные заказы по номеру.

        Args:
            piston_part: Фикстура детали.
        """
        a: ProductionOrder = ProductionOrder(
            number="PO-001",
            part=piston_part,
            quantity=5,
            process=_make_process(piston_part),
            deadline="X",
        )
        b: ProductionOrder = ProductionOrder(
            number="PO-001",
            part=piston_part,
            quantity=10,
            process=_make_process(piston_part),
            deadline="Y",
        )
        assert a == b
        assert a != "not an order"

    def test_hash(self, piston_part: Part) -> None:
        """Хеш по номеру.

        Args:
            piston_part: Фикстура детали.
        """
        a: ProductionOrder = ProductionOrder(
            number="PO-001",
            part=piston_part,
            quantity=5,
            process=_make_process(piston_part),
            deadline="X",
        )
        b: ProductionOrder = ProductionOrder(
            number="PO-001",
            part=piston_part,
            quantity=1,
            process=_make_process(piston_part),
            deadline="Y",
        )
        assert hash(a) == hash(b)

    def test_str(self, piston_part: Part) -> None:
        """str возвращает номер.

        Args:
            piston_part: Фикстура детали.
        """
        order: ProductionOrder = ProductionOrder(
            number="PO-42",
            part=piston_part,
            quantity=5,
            process=_make_process(piston_part),
            deadline="X",
        )
        assert "PO-42" in str(order)
