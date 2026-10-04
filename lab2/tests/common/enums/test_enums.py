"""
Тесты всех перечислений.

Module: tests.common.enums.test_enums
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.enums.equipment_status import EquipmentStatus
from common.enums.material_type import MaterialType
from common.enums.order_status import OrderStatus
from common.enums.part_type import PartType


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestOrderStatus:
    """Проверки OrderStatus."""

    def test_values(self) -> None:
        """Все статусы имеют строковые значения."""
        assert OrderStatus.NEW.value == "new"
        assert OrderStatus.IN_PROGRESS.value == "in_progress"
        assert OrderStatus.COMPLETED.value == "completed"
        assert OrderStatus.SHIPPED.value == "shipped"
        assert OrderStatus.CANCELLED.value == "cancelled"

    def test_str(self) -> None:
        """str возвращает русское название."""
        assert str(OrderStatus.NEW) == "новый"
        assert str(OrderStatus.IN_PROGRESS) == "в производстве"
        assert str(OrderStatus.COMPLETED) == "выполнен"
        assert str(OrderStatus.SHIPPED) == "отгружен"
        assert str(OrderStatus.CANCELLED) == "отменён"

    def test_distinct(self) -> None:
        """Элементы попарно различны."""
        assert len(set(OrderStatus)) == 5


class TestPartType:
    """Проверки PartType."""

    def test_values(self) -> None:
        """Значения типов деталей."""
        assert PartType.PISTON.value == "piston"
        assert PartType.CYLINDER.value == "cylinder"
        assert PartType.SHAFT.value == "shaft"
        assert PartType.GEAR.value == "gear"
        assert PartType.BEARING.value == "bearing"

    def test_str(self) -> None:
        """str возвращает русское название."""
        assert str(PartType.PISTON) == "поршень"
        assert str(PartType.CYLINDER) == "цилиндр"
        assert str(PartType.SHAFT) == "вал"
        assert str(PartType.GEAR) == "шестерня"
        assert str(PartType.BEARING) == "подшипник"

    def test_distinct(self) -> None:
        """Элементы попарно различны."""
        assert len(set(PartType)) == 5


class TestMaterialType:
    """Проверки MaterialType."""

    def test_values(self) -> None:
        """Значения типов материалов."""
        assert MaterialType.STEEL.value == "steel"
        assert MaterialType.ALUMINUM.value == "aluminum"
        assert MaterialType.PLASTIC.value == "plastic"

    def test_str(self) -> None:
        """str возвращает русское название."""
        assert str(MaterialType.STEEL) == "сталь"
        assert str(MaterialType.ALUMINUM) == "алюминий"
        assert str(MaterialType.PLASTIC) == "пластик"

    def test_distinct(self) -> None:
        """Элементы попарно различны."""
        assert len(set(MaterialType)) == 3


class TestEquipmentStatus:
    """Проверки EquipmentStatus."""

    def test_values(self) -> None:
        """Значения статусов оборудования."""
        assert EquipmentStatus.WORKING.value == "working"
        assert EquipmentStatus.IDLE.value == "idle"
        assert EquipmentStatus.BROKEN.value == "broken"
        assert EquipmentStatus.MAINTENANCE.value == "maintenance"

    def test_str(self) -> None:
        """str возвращает русское название."""
        assert str(EquipmentStatus.WORKING) == "работает"
        assert str(EquipmentStatus.IDLE) == "простаивает"
        assert str(EquipmentStatus.BROKEN) == "сломано"
        assert str(EquipmentStatus.MAINTENANCE) == "на обслуживании"

    def test_distinct(self) -> None:
        """Элементы попарно различны."""
        assert len(set(EquipmentStatus)) == 4
