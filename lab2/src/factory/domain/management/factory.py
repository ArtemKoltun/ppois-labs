"""
Завод.

Module: factory.domain.management.factory
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.domain.address import Address
from factory.domain.management.department import Department
from factory.domain.orders.order import Order
from factory.domain.warehouse.warehouse import Warehouse
from factory.domain.workshops.workshop import Workshop


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Factory(Readable, Writable):
    """Завод по изготовлению автомобильных деталей.

    Attributes:
        _name: Наименование завода.
        _address: Адрес.
        _workshops: Список цехов.
        _warehouses: Список складов.
        _departments: Список отделов.
        _orders: Список заказов.
    """

    def __init__(
        self,
        name: str,
        address: Address,
    ) -> None:
        """Создать завод.

        Args:
            name: Наименование.
            address: Адрес.

        Raises:
            ValueError: Если имя пустое.
        """
        if not name:
            raise ValueError("имя завода не может быть пустым")
        self._name: str = name
        self._address: Address = address
        self._workshops: list[Workshop] = []
        self._warehouses: list[Warehouse] = []
        self._departments: list[Department] = []
        self._orders: list[Order] = []

    @classmethod
    def _parse(cls, text: str) -> "Factory":
        """Разобрать завод из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        address: Address = Address(
            country=parts[1],
            city=parts[2],
            street=parts[3],
            building=parts[4],
            postal_code=parts[5],
        )
        return cls(name=parts[0], address=address)

    @property
    def name(self) -> str:
        """Наименование завода.

        Returns:
            Строка.
        """
        return self._name

    @property
    def address(self) -> Address:
        """Адрес завода.

        Returns:
            Объект адреса.
        """
        return self._address

    def add_workshop(self, workshop: Workshop) -> None:
        """Добавить цех.

        Args:
            workshop: Цех.

        Returns:
            Ничего не возвращает.
        """
        self._workshops.append(workshop)

    def add_warehouse(self, warehouse: Warehouse) -> None:
        """Добавить склад.

        Args:
            warehouse: Склад.

        Returns:
            Ничего не возвращает.
        """
        self._warehouses.append(warehouse)

    def add_department(self, department: Department) -> None:
        """Добавить отдел.

        Args:
            department: Отдел.

        Returns:
            Ничего не возвращает.
        """
        self._departments.append(department)

    def accept_order(self, order: Order) -> None:
        """Принять заказ от клиента.

        Args:
            order: Заказ.

        Returns:
            Ничего не возвращает.
        """
        self._orders.append(order)

    def workshops_count(self) -> int:
        """Вернуть число цехов.

        Returns:
            Целое число.
        """
        return len(self._workshops)

    def warehouses_count(self) -> int:
        """Вернуть число складов.

        Returns:
            Целое число.
        """
        return len(self._warehouses)

    def departments_count(self) -> int:
        """Вернуть число отделов.

        Returns:
            Целое число.
        """
        return len(self._departments)

    def orders_count(self) -> int:
        """Вернуть число принятых заказов.

        Returns:
            Целое число.
        """
        return len(self._orders)

    def active_orders_count(self) -> int:
        """Вернуть число активных заказов.

        Returns:
            Целое число.
        """
        return sum(1 for order in self._orders if order.is_active())

    def __eq__(self, other: object) -> bool:
        """Сравнить два завода.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении имени.
        """
        if not isinstance(other, Factory):
            return NotImplemented
        return self._name == other._name

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._name)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._name}; {self._address.country}; "
            f"{self._address.city}; {self._address.street}; "
            f"{self._address.building}; {self._address.postal_code}"
        )
