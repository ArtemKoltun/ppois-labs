"""
Склад готовой продукции.

Module: factory.domain.warehouse.finished_goods_warehouse
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from factory.domain.parts.part import Part
from factory.domain.warehouse.warehouse import Warehouse


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class FinishedGoodsWarehouse(Warehouse):
    """Склад готовой продукции.

    Attributes:
        _finished_parts: Список готовых деталей.
        _shipping_dock: Наличие отгрузочной площадки.
    """

    def __init__(
        self,
        warehouse: Warehouse,
        shipping_dock: bool = True,
    ) -> None:
        """Создать склад готовой продукции.

        Args:
            warehouse: Базовый склад.
            shipping_dock: Наличие отгрузочной площадки.
        """
        super().__init__(
            name=warehouse.name,
            address=warehouse._address,
            area=warehouse._area,
            capacity=warehouse._capacity,
        )
        self._finished_parts: list[Part] = []
        self._shipping_dock: bool = shipping_dock

    def accept_part(self, part: Part) -> None:
        """Принять готовую деталь.

        Args:
            part: Деталь.

        Returns:
            Ничего не возвращает.
        """
        self._finished_parts.append(part)

    def parts_count(self) -> int:
        """Вернуть число готовых деталей.

        Returns:
            Целое число.
        """
        return len(self._finished_parts)

    def ship(self, part: Part) -> bool:
        """Отгрузить деталь.

        Args:
            part: Деталь.

        Returns:
            ``True``, если деталь найдена и отгружена.
        """
        if part in self._finished_parts:
            self._finished_parts.remove(part)
            return True
        return False

    def can_ship(self) -> bool:
        """Проверить возможность отгрузки.

        Returns:
            ``True``, если есть отгрузочная площадка.
        """
        return self._shipping_dock
