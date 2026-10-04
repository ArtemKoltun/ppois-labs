"""
Тесты класса Statistics.

Module: tests.factory.domain.management.test_statistics
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.management.statistics import Statistics
from factory.domain.orders.order import Order
from factory.domain.parts.part import Part
from factory.domain.workshops.production_order import ProductionOrder
from factory.domain.workshops.production_process import (
    ProductionProcess,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_production_order(
    part: Part,
    quantity: int = 10,
) -> ProductionOrder:
    """Создать заказ на производство.

    Args:
        part: Деталь.
        quantity: Количество.

    Returns:
        Объект ``ProductionOrder``.
    """
    process: ProductionProcess = ProductionProcess(
        name="Процесс", part=part, duration_hours=1.0
    )
    return ProductionOrder(
        number="PO-X",
        part=part,
        quantity=quantity,
        process=process,
        deadline="X",
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestStatistics:
    """Проверки класса Statistics."""

    def test_creates(self, statistics: Statistics) -> None:
        """Статистика создаётся.

        Args:
            statistics: Фикстура статистики.
        """
        assert statistics.period == "2026-01"
        assert statistics.defects_count == 0

    def test_add_order(
        self,
        statistics: Statistics,
        order: Order,
    ) -> None:
        """add_order считает заказ.

        Args:
            statistics: Фикстура статистики.
            order: Фикстура заказа.
        """
        statistics.add_order(order)
        assert statistics.total_orders() == 1

    def test_add_production_order(
        self,
        statistics: Statistics,
        piston_part: Part,
    ) -> None:
        """add_production_order считает производство.

        Args:
            statistics: Фикстура статистики.
            piston_part: Фикстура детали.
        """
        statistics.add_production_order(
            _make_production_order(piston_part)
        )
        assert statistics.total_production() == 1

    def test_total_produced_quantity(
        self,
        statistics: Statistics,
        piston_part: Part,
    ) -> None:
        """total_produced_quantity суммирует.

        Args:
            statistics: Фикстура статистики.
            piston_part: Фикстура детали.
        """
        statistics.add_production_order(
            _make_production_order(piston_part, quantity=10)
        )
        statistics.add_production_order(
            _make_production_order(piston_part, quantity=20)
        )
        assert statistics.total_produced_quantity() == 30

    def test_record_defects(self, statistics: Statistics) -> None:
        """record_defects увеличивает брак.

        Args:
            statistics: Фикстура статистики.
        """
        statistics.record_defects(5)
        assert statistics.defects_count == 5

    def test_defect_rate(
        self,
        statistics: Statistics,
        piston_part: Part,
    ) -> None:
        """defect_rate считает долю брака.

        Args:
            statistics: Фикстура статистики.
            piston_part: Фикстура детали.
        """
        statistics.add_production_order(
            _make_production_order(piston_part, quantity=100)
        )
        statistics.record_defects(10)
        assert statistics.defect_rate() == 0.1

    def test_defect_rate_zero(self, statistics: Statistics) -> None:
        """defect_rate без производства равен 0.

        Args:
            statistics: Фикстура статистики.
        """
        assert statistics.defect_rate() == 0.0

    def test_is_high_defect_rate(
        self,
        statistics: Statistics,
        piston_part: Part,
    ) -> None:
        """is_high_defect_rate проверяет порог.

        Args:
            statistics: Фикстура статистики.
            piston_part: Фикстура детали.
        """
        statistics.add_production_order(
            _make_production_order(piston_part, quantity=100)
        )
        statistics.record_defects(10)
        assert statistics.is_high_defect_rate()

    def test_equality(self, statistics: Statistics) -> None:
        """Равные по периоду.

        Args:
            statistics: Фикстура статистики.
        """
        other: Statistics = Statistics(period="2026-01")
        assert statistics == other
        assert statistics != "not statistics"

    def test_hash(self, statistics: Statistics) -> None:
        """Хеш по периоду.

        Args:
            statistics: Фикстура статистики.
        """
        other: Statistics = Statistics(period="2026-01")
        assert hash(statistics) == hash(other)

    def test_str(self, statistics: Statistics) -> None:
        """str возвращает период.

        Args:
            statistics: Фикстура статистики.
        """
        assert "2026-01" in str(statistics)

    def test_parse(self) -> None:
        """from_string разбирает статистику."""
        s: Statistics = Statistics.from_string("2026-02, 5")
        assert s.period == "2026-02"
        assert s.defects_count == 5
