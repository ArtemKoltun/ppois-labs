"""
Тесты класса Customer.

Module: tests.factory.domain.orders.test_customer
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.domain.address import Address
from factory.domain.orders.customer import Customer


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestCustomer:
    """Проверки класса Customer."""

    def test_creates(self, customer: Customer) -> None:
        """Клиент создаётся.

        Args:
            customer: Фикстура клиента.
        """
        assert customer.name == "ООО АвтоПром"
        assert customer.inn == "7701234567"

    def test_empty_name_raises(self, address: Address) -> None:
        """Пустое имя недопустимо.

        Args:
            address: Фикстура адреса.
        """
        with pytest.raises(ValueError):
            Customer(
                name="",
                address=address,
                inn="123",
                contact_person="X",
                phone="+7",
            )

    def test_empty_inn_raises(self, address: Address) -> None:
        """Пустой ИНН недопустим.

        Args:
            address: Фикстура адреса.
        """
        with pytest.raises(ValueError):
            Customer(
                name="X",
                address=address,
                inn="",
                contact_person="X",
                phone="+7",
            )

    def test_is_company(self, customer: Customer) -> None:
        """is_company проверяет длину ИНН.

        Args:
            customer: Фикстура клиента.
        """
        assert customer.is_company()

    def test_not_company(self, address: Address) -> None:
        """Физлицо с коротким ИНН.

        Args:
            address: Фикстура адреса.
        """
        person: Customer = Customer(
            name="Иванов",
            address=address,
            inn="123456789012",
            contact_person="X",
            phone="+7",
        )
        assert not person.is_company()

    def test_update_contact(self, customer: Customer) -> None:
        """update_contact меняет контакты.

        Args:
            customer: Фикстура клиента.
        """
        customer.update_contact("Новый", "+7-999")
        assert customer._contact_person == "Новый"

    def test_equality(self, customer: Customer) -> None:
        """Равные по ИНН.

        Args:
            customer: Фикстура клиента.
        """
        other: Customer = Customer(
            name="Другое",
            address=customer._address,
            inn="7701234567",
            contact_person="X",
            phone="+7",
        )
        assert customer == other

    def test_inequality(self, customer: Customer) -> None:
        """Разные клиенты.

        Args:
            customer: Фикстура клиента.
        """
        assert customer != "not customer"

    def test_hash(self, customer: Customer) -> None:
        """Хеш по ИНН.

        Args:
            customer: Фикстура клиента.
        """
        other: Customer = Customer(
            name="X",
            address=customer._address,
            inn="7701234567",
            contact_person="X",
            phone="+7",
        )
        assert hash(customer) == hash(other)

    def test_str(self, customer: Customer) -> None:
        """str возвращает поля.

        Args:
            customer: Фикстура клиента.
        """
        text: str = str(customer)
        assert "ООО АвтоПром" in text
        assert "7701234567" in text
