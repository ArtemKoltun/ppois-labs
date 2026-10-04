"""
Тесты класса Invoice.

Module: tests.factory.domain.orders.test_invoice
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.domain.money import Money
from factory.domain.orders.customer import Customer
from factory.domain.orders.invoice import Invoice
from factory.domain.orders.order import Order


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestInvoice:
    """Проверки класса Invoice."""

    def test_creates(self, invoice: Invoice) -> None:
        """Счёт создаётся.

        Args:
            invoice: Фикстура счёта.
        """
        assert invoice.number == "INV-001"
        assert invoice.amount.amount == 50000.0
        assert not invoice.is_paid

    def test_mark_paid(self, invoice: Invoice) -> None:
        """mark_paid отмечает оплату.

        Args:
            invoice: Фикстура счёта.
        """
        invoice.mark_paid()
        assert invoice.is_paid

    def test_cancel(self, invoice: Invoice) -> None:
        """cancel отменяет.

        Args:
            invoice: Фикстура счёта.
        """
        invoice.mark_paid()
        invoice.cancel()
        assert not invoice.is_paid

    def test_is_overdue(self, invoice: Invoice) -> None:
        """is_overdue проверяет просрочку.

        Args:
            invoice: Фикстура счёта.
        """
        assert invoice.is_overdue("2026-02-01")
        assert not invoice.is_overdue("2026-01-10")

    def test_is_not_overdue_if_paid(self, invoice: Invoice) -> None:
        """Оплаченный не просрочен.

        Args:
            invoice: Фикстура счёта.
        """
        invoice.mark_paid()
        assert not invoice.is_overdue("2026-02-01")

    def test_equality(self, invoice: Invoice) -> None:
        """Равные по номеру.

        Args:
            invoice: Фикстура счёта.
        """
        other: Invoice = Invoice(
            number="INV-001",
            order=invoice._order,
            customer=invoice._customer,
            amount=Money(amount=1.0),
            issue_date="X",
        )
        assert invoice == other
        assert invoice != "not invoice"

    def test_hash(self, invoice: Invoice) -> None:
        """Хеш по номеру.

        Args:
            invoice: Фикстура счёта.
        """
        other: Invoice = Invoice(
            number="INV-001",
            order=invoice._order,
            customer=invoice._customer,
            amount=Money(amount=1.0),
            issue_date="X",
        )
        assert hash(invoice) == hash(other)

    def test_str(self, invoice: Invoice) -> None:
        """str возвращает номер.

        Args:
            invoice: Фикстура счёта.
        """
        assert "INV-001" in str(invoice)
