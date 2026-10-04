"""
Склад.

Module: factory.domain.warehouse.warehouse
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.domain.address import Address
from factory.domain.personnel.employee import Employee


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Warehouse(Readable, Writable):
    """Склад завода.

    Attributes:
        _name: Наименование.
        _address: Адрес.
        _area: Площадь в м².
        _manager: Заведующий складом.
        _capacity: Максимальная ёмкость.
    """

    def __init__(
        self,
        name: str,
        address: Address,
        area: float,
        capacity: float,
        manager: Employee | None = None,
    ) -> None:
        """Создать склад.

        Args:
            name: Наименование.
            address: Адрес.
            area: Площадь.
            capacity: Ёмкость.
            manager: Заведующий.

        Raises:
            ValueError: Если данные некорректны.
        """
        if not name:
            raise ValueError("имя склада не может быть пустым")
        if area <= 0 or capacity <= 0:
            raise ValueError(
                "площадь и ёмкость должны быть положительными"
            )
        self._name: str = name
        self._address: Address = address
        self._area: float = area
        self._manager: Employee | None = manager
        self._capacity: float = capacity
        self._current_load: float = 0.0

    @classmethod
    def _parse(cls, text: str) -> "Warehouse":
        """Разобрать склад из строки.

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
        return cls(
            name=parts[0],
            address=address,
            area=float(parts[6]),
            capacity=float(parts[7]),
        )

    @property
    def name(self) -> str:
        """Наименование.

        Returns:
            Строка.
        """
        return self._name

    @property
    def capacity(self) -> float:
        """Ёмкость.

        Returns:
            Число.
        """
        return self._capacity

    @property
    def current_load(self) -> float:
        """Текущая загрузка.

        Returns:
            Число.
        """
        return self._current_load

    def assign_manager(self, manager: Employee) -> None:
        """Назначить заведующего.

        Args:
            manager: Сотрудник.

        Returns:
            Ничего не возвращает.
        """
        self._manager = manager

    def has_manager(self) -> bool:
        """Проверить наличие заведующего.

        Returns:
            ``True``, если назначен.
        """
        return self._manager is not None

    def add_load(self, amount: float) -> None:
        """Добавить груз на склад.

        Args:
            amount: Количество.

        Returns:
            Ничего не возвращает.

        Raises:
            ValueError: Если превышена ёмкость.
        """
        if self._current_load + amount > self._capacity:
            raise ValueError("превышена ёмкость склада")
        self._current_load += amount

    def remove_load(self, amount: float) -> None:
        """Убрать груз со склада.

        Args:
            amount: Количество.

        Returns:
            Ничего не возвращает.
        """
        self._current_load = max(0.0, self._current_load - amount)

    def fill_ratio(self) -> float:
        """Рассчитать заполненность склада.

        Returns:
            Число от 0 до 1.
        """
        if self._capacity == 0:
            return 0.0
        return self._current_load / self._capacity

    def is_full(self) -> bool:
        """Проверить, полон ли склад.

        Returns:
            ``True``, если загрузка выше 95%.
        """
        return self.fill_ratio() >= 0.95

    def __eq__(self, other: object) -> bool:
        """Сравнить два склада.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении имени.
        """
        if not isinstance(other, Warehouse):
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
            f"{self._address.building}; {self._address.postal_code}; "
            f"{self._area}; {self._capacity}"
        )
