"""
Тесты класса Warehouse.

Module: tests.factory.domain.warehouse.test_warehouse
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.domain.address import Address
from factory.domain.personnel.employee import Employee
from factory.domain.warehouse.warehouse import Warehouse


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_warehouse(address: Address) -> Warehouse:
    """Создать склад.

    Args:
        address: Адрес.

    Returns:
        Объект ``Warehouse``.
    """
    return Warehouse(
        name="Главный склад",
        address=address,
        area=1000.0,
        capacity=10000.0,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestWarehouse:
    """Проверки класса Warehouse."""

    def test_creates(self, address: Address) -> None:
        """Склад создаётся.

        Args:
            address: Фикстура адреса.
        """
        w: Warehouse = _make_warehouse(address)
        assert w.name == "Главный склад"
        assert w.current_load == 0.0

    def test_empty_name_raises(self, address: Address) -> None:
        """Пустое имя недопустимо.

        Args:
            address: Фикстура адреса.
        """
        with pytest.raises(ValueError):
            Warehouse(
                name="",
                address=address,
                area=1000.0,
                capacity=1000.0,
            )

    def test_zero_capacity_raises(self, address: Address) -> None:
        """Нулевая ёмкость недопустима.

        Args:
            address: Фикстура адреса.
        """
        with pytest.raises(ValueError):
            Warehouse(
                name="X",
                address=address,
                area=1000.0,
                capacity=0.0,
            )

    def test_assign_manager(
        self,
        address: Address,
        employee: Employee,
    ) -> None:
        """assign_manager назначает.

        Args:
            address: Фикстура адреса.
            employee: Фикстура сотрудника.
        """
        w: Warehouse = _make_warehouse(address)
        assert not w.has_manager()
        w.assign_manager(employee)
        assert w.has_manager()

    def test_add_load(self, address: Address) -> None:
        """add_load увеличивает загрузку.

        Args:
            address: Фикстура адреса.
        """
        w: Warehouse = _make_warehouse(address)
        w.add_load(5000.0)
        assert w.current_load == 5000.0

    def test_add_load_over_capacity_raises(
        self,
        address: Address,
    ) -> None:
        """Превышение ёмкости падает.

        Args:
            address: Фикстура адреса.
        """
        w: Warehouse = _make_warehouse(address)
        with pytest.raises(ValueError):
            w.add_load(20000.0)

    def test_remove_load(self, address: Address) -> None:
        """remove_load уменьшает.

        Args:
            address: Фикстура адреса.
        """
        w: Warehouse = _make_warehouse(address)
        w.add_load(5000.0)
        w.remove_load(3000.0)
        assert w.current_load == 2000.0

    def test_remove_load_below_zero(self, address: Address) -> None:
        """Не уходит в минус.

        Args:
            address: Фикстура адреса.
        """
        w: Warehouse = _make_warehouse(address)
        w.remove_load(5000.0)
        assert w.current_load == 0.0

    def test_fill_ratio(self, address: Address) -> None:
        """fill_ratio считает долю.

        Args:
            address: Фикстура адреса.
        """
        w: Warehouse = _make_warehouse(address)
        w.add_load(5000.0)
        assert w.fill_ratio() == 0.5

    def test_is_full(self, address: Address) -> None:
        """is_full проверяет заполненность.

        Args:
            address: Фикстура адреса.
        """
        w: Warehouse = _make_warehouse(address)
        w.add_load(9600.0)
        assert w.is_full()

    def test_equality(self, address: Address) -> None:
        """Равные по имени.

        Args:
            address: Фикстура адреса.
        """
        a: Warehouse = _make_warehouse(address)
        b: Warehouse = _make_warehouse(address)
        assert a == b
        assert a != "not warehouse"

    def test_hash(self, address: Address) -> None:
        """Хеш по имени.

        Args:
            address: Фикстура адреса.
        """
        a: Warehouse = _make_warehouse(address)
        b: Warehouse = _make_warehouse(address)
        assert hash(a) == hash(b)

    def test_str(self, address: Address) -> None:
        """str возвращает имя.

        Args:
            address: Фикстура адреса.
        """
        w: Warehouse = _make_warehouse(address)
        assert "Главный склад" in str(w)

    def test_parse(self) -> None:
        """from_string разбирает склад."""
        w: Warehouse = Warehouse.from_string(
            "Склад; Россия; Москва; Ленина; 5; 101000; 500; 1000"
        )
        assert w.name == "Склад"
