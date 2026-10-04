"""
Тесты класса Equipment.

Module: tests.factory.domain.equipment.test_equipment
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.enums.equipment_status import EquipmentStatus
from common.exceptions import EquipmentBrokenError
from factory.domain.equipment.equipment import Equipment

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestEquipment:
    """Проверки класса Equipment."""

    def test_creates(self, equipment: Equipment) -> None:
        """Оборудование создаётся.

        Args:
            equipment: Фикстура оборудования.
        """
        assert equipment.name == "Токарный 16К20"
        assert equipment.status is EquipmentStatus.IDLE
        assert equipment.hours_worked == 0.0

    def test_empty_name_raises(self) -> None:
        """Пустое имя недопустимо."""
        with pytest.raises(ValueError):
            Equipment(name="", inventory_number="X", purchase_year=2020)

    def test_empty_inventory_raises(self) -> None:
        """Пустой инвентарный номер недопустим."""
        with pytest.raises(ValueError):
            Equipment(name="X", inventory_number="", purchase_year=2020)

    def test_start(self, equipment: Equipment) -> None:
        """start переводит в WORKING.

        Args:
            equipment: Фикстура оборудования.
        """
        equipment.start()
        assert equipment.status is EquipmentStatus.WORKING

    def test_start_broken_raises(self, equipment: Equipment) -> None:
        """start сломанного падает.

        Args:
            equipment: Фикстура оборудования.
        """
        equipment.mark_broken()
        with pytest.raises(EquipmentBrokenError):
            equipment.start()

    def test_stop(self, equipment: Equipment) -> None:
        """stop переводит в IDLE.

        Args:
            equipment: Фикстура оборудования.
        """
        equipment.start()
        equipment.stop()
        assert equipment.status is EquipmentStatus.IDLE

    def test_add_hours(self, equipment: Equipment) -> None:
        """add_hours увеличивает счётчик.

        Args:
            equipment: Фикстура оборудования.
        """
        equipment.add_hours(100.0)
        assert equipment.hours_worked == 100.0

    def test_mark_broken(self, equipment: Equipment) -> None:
        """mark_broken переводит в BROKEN.

        Args:
            equipment: Фикстура оборудования.
        """
        equipment.mark_broken()
        assert equipment.status is EquipmentStatus.BROKEN

    def test_is_available(self, equipment: Equipment) -> None:
        """is_available для IDLE.

        Args:
            equipment: Фикстура оборудования.
        """
        assert equipment.is_available()

    def test_is_available_broken(self, equipment: Equipment) -> None:
        """is_available для BROKEN — False.

        Args:
            equipment: Фикстура оборудования.
        """
        equipment.mark_broken()
        assert not equipment.is_available()

    def test_equality(self, equipment: Equipment) -> None:
        """Оборудование сравнивается по инвентарному номеру.

        Args:
            equipment: Фикстура оборудования.
        """
        other: Equipment = Equipment(
            name="Другое",
            inventory_number="INV-001",
            purchase_year=2021,
        )
        assert equipment == other

    def test_inequality(self, equipment: Equipment) -> None:
        """Разные номера — не равны.

        Args:
            equipment: Фикстура оборудования.
        """
        assert equipment != "not equipment"

    def test_hash(self, equipment: Equipment) -> None:
        """Одинаковые номера — одинаковый хеш.

        Args:
            equipment: Фикстура оборудования.
        """
        other: Equipment = Equipment(
            name="X", inventory_number="INV-001", purchase_year=2021
        )
        assert hash(equipment) == hash(other)

    def test_str(self, equipment: Equipment) -> None:
        """str возвращает поля.

        Args:
            equipment: Фикстура оборудования.
        """
        text: str = str(equipment)
        assert "Токарный 16К20" in text
        assert "INV-001" in text

    def test_parse(self) -> None:
        """from_string разбирает оборудование."""
        eq: Equipment = Equipment.from_string(
            "Станок, INV-42, 2019, working"
        )
        assert eq.name == "Станок"
        assert eq.status is EquipmentStatus.WORKING
