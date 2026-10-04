"""
Тесты класса Address.

Module: tests.common.domain.test_address
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.domain.address import Address

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestAddress:
    """Проверки класса Address."""

    def test_creates(self, address: Address) -> None:
        """Адрес создаётся с полями.

        Args:
            address: Фикстура адреса.
        """
        assert address.country == "Россия"
        assert address.city == "Москва"
        assert address.street == "Тверская"
        assert address.building == "1"
        assert address.postal_code == "101000"

    def test_full(self, address: Address) -> None:
        """full возвращает полный адрес.

        Args:
            address: Фикстура адреса.
        """
        assert address.full() == (
            "Россия, Москва, Тверская, 1, 101000"
        )

    @pytest.mark.parametrize(
        "field",
        ["country", "city", "street", "building", "postal_code"],
    )
    def test_empty_field_raises(self, field: str) -> None:
        """Пустое поле приводит к ValueError.

        Args:
            field: Имя поля для проверки.
        """
        kwargs: dict[str, str] = {
            "country": "Россия",
            "city": "Москва",
            "street": "Тверская",
            "building": "1",
            "postal_code": "101000",
        }
        kwargs[field] = ""
        with pytest.raises(ValueError):
            Address(**kwargs)

    def test_equality(self, address: Address) -> None:
        """Одинаковые адреса равны.

        Args:
            address: Фикстура адреса.
        """
        other: Address = Address(
            country="Россия",
            city="Москва",
            street="Тверская",
            building="1",
            postal_code="101000",
        )
        assert address == other

    def test_inequality(self, address: Address) -> None:
        """Разные адреса не равны.

        Args:
            address: Фикстура адреса.
        """
        other: Address = Address(
            country="Россия",
            city="СПб",
            street="Невский",
            building="1",
            postal_code="101000",
        )
        assert address != other

    def test_equality_with_other_type(self, address: Address) -> None:
        """Сравнение с не-Address возвращает False.

        Args:
            address: Фикстура адреса.
        """
        assert address != "not an address"

    def test_hash(self, address: Address) -> None:
        """Одинаковые адреса имеют одинаковый хеш.

        Args:
            address: Фикстура адреса.
        """
        other: Address = Address(
            country="Россия",
            city="Москва",
            street="Тверская",
            building="1",
            postal_code="101000",
        )
        assert hash(address) == hash(other)

    def test_str(self, address: Address) -> None:
        """str возвращает полный адрес.

        Args:
            address: Фикстура адреса.
        """
        assert str(address) == "Россия, Москва, Тверская, 1, 101000"
