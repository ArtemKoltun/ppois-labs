"""
Склад сырья.

Module: factory.domain.warehouse.raw_material_warehouse
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from factory.domain.materials.material import Material
from factory.domain.warehouse.warehouse import Warehouse


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class RawMaterialWarehouse(Warehouse):
    """Склад сырья и материалов.

    Attributes:
        _materials: Список хранимых материалов.
        _min_temperature: Минимальная температура хранения.
    """

    def __init__(
        self,
        warehouse: Warehouse,
        min_temperature: float = 0.0,
    ) -> None:
        """Создать склад сырья.

        Args:
            warehouse: Базовый склад.
            min_temperature: Минимальная температура.
        """
        super().__init__(
            name=warehouse.name,
            address=warehouse._address,
            area=warehouse._area,
            capacity=warehouse._capacity,
        )
        self._materials: list[Material] = []
        self._min_temperature: float = min_temperature

    def accept_material(self, material: Material) -> None:
        """Принять материал на склад.

        Args:
            material: Материал.

        Returns:
            Ничего не возвращает.
        """
        self._materials.append(material)

    def materials_count(self) -> int:
        """Вернуть число видов материалов.

        Returns:
            Целое число.
        """
        return len(self._materials)

    def has_material(self, material: Material) -> bool:
        """Проверить наличие материала.

        Args:
            material: Материал.

        Returns:
            ``True``, если есть.
        """
        return material in self._materials

    def needs_heating(self) -> bool:
        """Проверить, нужно ли отопление.

        Returns:
            ``True``, если минимальная температура выше 10.
        """
        return self._min_temperature > 10
