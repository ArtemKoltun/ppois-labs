"""
Тесты класса Supplier.

Module: tests.factory.domain.materials.test_supplier
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.domain.address import Address
from factory.domain.materials.supplier import Supplier

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestSupplier:
    """Проверки класса Supplier."""

    def test_creates(self, supplier: Supplier) -> None:
        """Поставщик создаётся.

        Args:
            supplier: Фикстура поставщика.
        """
        assert supplier.name == "МеталлПром"
        assert supplier.rating == 4.5

    def test_invalid_rating_raises(self, address: Address) -> None:
        """Рейтинг вне диапазона недопустим.

        Args:
            address: Фикстура адреса.
        """
        with pytest.raises(ValueError):
            Supplier(
                name="X",
                address=address,
                contact_person="X",
                phone="+7",
                rating=6.0,
            )

    def test_negative_rating_raises(self, address: Address) -> None:
        """Отрицательный рейтинг недопустим.

        Args:
            address: Фикстура адреса.
        """
        with pytest.raises(ValueError):
            Supplier(
                name="X",
                address=address,
                contact_person="X",
                phone="+7",
                rating=-1.0,
            )

    def test_update_rating(self, supplier: Supplier) -> None:
        """update_rating меняет рейтинг.

        Args:
            supplier: Фикстура поставщика.
        """
        supplier.update_rating(5.0)
        assert supplier.rating == 5.0

    def test_update_rating_invalid_raises(
        self,
        supplier: Supplier,
    ) -> None:
        """update_rating с плохим значением падает.

        Args:
            supplier: Фикстура поставщика.
        """
        with pytest.raises(ValueError):
            supplier.update_rating(10.0)

    def test_get_contact_info(self, supplier: Supplier) -> None:
        """get_contact_info возвращает контакты.

        Args:
            supplier: Фикстура поставщика.
        """
        text: str = supplier.get_contact_info()
        assert "Петров" in text
        assert "+7" in text

    def test_is_reliable(self, supplier: Supplier) -> None:
        """is_reliable проверяет рейтинг.

        Args:
            supplier: Фикстура поставщика.
        """
        assert supplier.is_reliable()

    def test_equality(self, supplier: Supplier) -> None:
        """Одинаковые по имени поставщики равны.

        Args:
            supplier: Фикстура поставщика.
        """
        other: Supplier = Supplier(
            name="МеталлПром",
            address=supplier._address,
            contact_person="Другой",
            phone="+7",
            rating=3.0,
        )
        assert supplier == other

    def test_inequality(self, supplier: Supplier) -> None:
        """Разные поставщики не равны.

        Args:
            supplier: Фикстура поставщика.
        """
        assert supplier != "not a supplier"

    def test_hash(self, supplier: Supplier) -> None:
        """Одинаковые поставщики имеют одинаковый хеш.

        Args:
            supplier: Фикстура поставщика.
        """
        other: Supplier = Supplier(
            name="МеталлПром",
            address=supplier._address,
            contact_person="X",
            phone="+7",
        )
        assert hash(supplier) == hash(other)

    def test_str(self, supplier: Supplier) -> None:
        """str возвращает поля.

        Args:
            supplier: Фикстура поставщика.
        """
        text: str = str(supplier)
        assert "МеталлПром" in text
