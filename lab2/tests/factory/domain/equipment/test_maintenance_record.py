"""
Тесты класса MaintenanceRecord.

Module: tests.factory.domain.equipment.test_maintenance_record
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.equipment.equipment import Equipment
from factory.domain.equipment.maintenance_record import (
    MaintenanceRecord,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_record(
    equipment: Equipment,
    cost: float = 30000.0,
    description: str = "Замена подшипника",
) -> MaintenanceRecord:
    """Создать запись о ТО.

    Args:
        equipment: Оборудование.
        cost: Стоимость.
        description: Описание.

    Returns:
        Объект ``MaintenanceRecord``.
    """
    return MaintenanceRecord(
        equipment=equipment,
        performed_by="Петров П.П.",
        date="2026-01-15",
        description=description,
        cost=cost,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestMaintenanceRecord:
    """Проверки класса MaintenanceRecord."""

    def test_creates(self, equipment: Equipment) -> None:
        """Запись создаётся.

        Args:
            equipment: Фикстура оборудования.
        """
        record: MaintenanceRecord = _make_record(equipment)
        assert record.cost == 30000.0

    def test_is_expensive(self, equipment: Equipment) -> None:
        """is_expensive проверяет стоимость.

        Args:
            equipment: Фикстура оборудования.
        """
        cheap: MaintenanceRecord = _make_record(
            equipment, cost=10000.0
        )
        expensive: MaintenanceRecord = _make_record(
            equipment, cost=100000.0
        )
        assert not cheap.is_expensive()
        assert expensive.is_expensive()

    def test_was_planned(self, equipment: Equipment) -> None:
        """was_planned проверяет описание.

        Args:
            equipment: Фикстура оборудования.
        """
        planned: MaintenanceRecord = _make_record(
            equipment, description="Плановое ТО"
        )
        repair: MaintenanceRecord = _make_record(
            equipment, description="Аварийный ремонт"
        )
        assert planned.was_planned()
        assert not repair.was_planned()

    def test_equality(self, equipment: Equipment) -> None:
        """Равные записи.

        Args:
            equipment: Фикстура оборудования.
        """
        a: MaintenanceRecord = _make_record(equipment)
        b: MaintenanceRecord = _make_record(equipment)
        assert a == b
        assert a != "not a record"

    def test_hash(self, equipment: Equipment) -> None:
        """Хеш записей.

        Args:
            equipment: Фикстура оборудования.
        """
        a: MaintenanceRecord = _make_record(equipment)
        b: MaintenanceRecord = _make_record(equipment)
        assert hash(a) == hash(b)

    def test_str(self, equipment: Equipment) -> None:
        """str возвращает поля.

        Args:
            equipment: Фикстура оборудования.
        """
        record: MaintenanceRecord = _make_record(equipment)
        text: str = str(record)
        assert "Петров" in text
