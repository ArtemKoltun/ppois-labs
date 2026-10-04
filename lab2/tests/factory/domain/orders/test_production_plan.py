"""
Тесты класса ProductionPlan.

Module: tests.factory.domain.orders.test_production_plan
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.orders.order import Order
from factory.domain.orders.production_plan import ProductionPlan
from factory.domain.workshops.workshop import Workshop


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_plan(workshop: Workshop, target: int = 500) -> ProductionPlan:
    """Создать план.

    Args:
        workshop: Цех.
        target: Плановый выпуск.

    Returns:
        Объект ``ProductionPlan``.
    """
    return ProductionPlan(
        period="2026-Q1",
        workshop=workshop,
        target_output=target,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestProductionPlan:
    """Проверки класса ProductionPlan."""

    def test_creates(self, workshop: Workshop) -> None:
        """План создаётся.

        Args:
            workshop: Фикстура цеха.
        """
        plan: ProductionPlan = _make_plan(workshop)
        assert plan.period == "2026-Q1"
        assert plan.orders_count() == 0

    def test_add_remove_order(
        self,
        workshop: Workshop,
        order: Order,
    ) -> None:
        """Добавление и удаление заказа.

        Args:
            workshop: Фикстура цеха.
            order: Фикстура заказа.
        """
        plan: ProductionPlan = _make_plan(workshop)
        plan.add_order(order)
        assert plan.orders_count() == 1
        plan.remove_order(order)
        assert plan.orders_count() == 0

    def test_remove_nonexistent(
        self,
        workshop: Workshop,
        order: Order,
    ) -> None:
        """Удаление отсутствующего не падает.

        Args:
            workshop: Фикстура цеха.
            order: Фикстура заказа.
        """
        plan: ProductionPlan = _make_plan(workshop)
        plan.remove_order(order)

    def test_planned_quantity(
        self,
        workshop: Workshop,
        order: Order,
    ) -> None:
        """planned_quantity суммирует.

        Args:
            workshop: Фикстура цеха.
            order: Фикстура заказа.
        """
        plan: ProductionPlan = _make_plan(workshop)
        plan.add_order(order)
        assert plan.planned_quantity() == 100

    def test_is_overloaded(
        self,
        workshop: Workshop,
        order: Order,
    ) -> None:
        """is_overloaded проверяет план.

        Args:
            workshop: Фикстура цеха.
            order: Фикстура заказа.
        """
        small: ProductionPlan = _make_plan(workshop, target=50)
        big: ProductionPlan = _make_plan(workshop, target=500)
        small.add_order(order)
        big.add_order(order)
        assert small.is_overloaded()
        assert not big.is_overloaded()

    def test_equality(self, workshop: Workshop) -> None:
        """Равные планы.

        Args:
            workshop: Фикстура цеха.
        """
        a: ProductionPlan = _make_plan(workshop)
        b: ProductionPlan = _make_plan(workshop)
        assert a == b
        assert a != "not plan"

    def test_hash(self, workshop: Workshop) -> None:
        """Хеш планов.

        Args:
            workshop: Фикстура цеха.
        """
        a: ProductionPlan = _make_plan(workshop)
        b: ProductionPlan = _make_plan(workshop)
        assert hash(a) == hash(b)

    def test_str(self, workshop: Workshop) -> None:
        """str возвращает период.

        Args:
            workshop: Фикстура цеха.
        """
        plan: ProductionPlan = _make_plan(workshop)
        assert "2026-Q1" in str(plan)
