"""
Тесты класса Contract.

Module: tests.factory.domain.orders.test_contract
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.domain.money import Money
from factory.domain.orders.contract import Contract
from factory.domain.orders.customer import Customer

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_contract(customer: Customer) -> Contract:
    """Создать договор.

    Args:
        customer: Клиент.

    Returns:
        Объект ``Contract``.
    """
    return Contract(
        number="C-001",
        customer=customer,
        sign_date="2026-01-10",
        valid_until="2026-12-31",
        total_amount=Money(amount=1000000.0),
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestContract:
    """Проверки класса Contract."""

    def test_creates(self, customer: Customer) -> None:
        """Договор создаётся.

        Args:
            customer: Фикстура клиента.
        """
        contract: Contract = _make_contract(customer)
        assert contract.number == "C-001"
        assert not contract.is_signed

    def test_sign(self, customer: Customer) -> None:
        """sign подписывает.

        Args:
            customer: Фикстура клиента.
        """
        contract: Contract = _make_contract(customer)
        contract.sign()
        assert contract.is_signed
        assert contract.is_valid()

    def test_terminate(self, customer: Customer) -> None:
        """terminate расторгает.

        Args:
            customer: Фикстура клиента.
        """
        contract: Contract = _make_contract(customer)
        contract.sign()
        contract.terminate()
        assert not contract.is_valid()

    def test_equality(self, customer: Customer) -> None:
        """Равные по номеру.

        Args:
            customer: Фикстура клиента.
        """
        a: Contract = _make_contract(customer)
        b: Contract = _make_contract(customer)
        assert a == b
        assert a != "not contract"

    def test_hash(self, customer: Customer) -> None:
        """Хеш по номеру.

        Args:
            customer: Фикстура клиента.
        """
        a: Contract = _make_contract(customer)
        b: Contract = _make_contract(customer)
        assert hash(a) == hash(b)

    def test_str(self, customer: Customer) -> None:
        """str возвращает номер.

        Args:
            customer: Фикстура клиента.
        """
        contract: Contract = _make_contract(customer)
        assert "C-001" in str(contract)
