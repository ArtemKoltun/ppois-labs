"""
Тесты класса Payment.

Module: tests.factory.domain.orders.test_payment
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.domain.money import Money
from factory.domain.orders.invoice import Invoice
from factory.domain.orders.payment import Payment

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_payment(
    invoice: Invoice,
    amount: float = 50000.0,
    method: str = "bank_transfer",
) -> Payment:
    """Создать платёж.

    Args:
        invoice: Счёт.
        amount: Сумма.
        method: Способ оплаты.

    Returns:
        Объект ``Payment``.
    """
    return Payment(
        invoice=invoice,
        amount=Money(amount=amount),
        date="2026-01-25",
        method=method,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestPayment:
    """Проверки класса Payment."""

    def test_creates(self, invoice: Invoice) -> None:
        """Платёж создаётся.

        Args:
            invoice: Фикстура счёта.
        """
        payment: Payment = _make_payment(invoice)
        assert payment.amount.amount == 50000.0
        assert payment.method == "bank_transfer"

    def test_covers_invoice(self, invoice: Invoice) -> None:
        """covers_invoice проверяет сумму.

        Args:
            invoice: Фикстура счёта.
        """
        full: Payment = _make_payment(invoice, amount=50000.0)
        partial: Payment = _make_payment(invoice, amount=10000.0)
        assert full.covers_invoice()
        assert not partial.covers_invoice()

    def test_is_electronic(self, invoice: Invoice) -> None:
        """is_electronic проверяет способ.

        Args:
            invoice: Фикстура счёта.
        """
        electronic: Payment = _make_payment(invoice, method="card")
        cash: Payment = _make_payment(invoice, method="cash")
        assert electronic.is_electronic()
        assert not cash.is_electronic()

    def test_equality(self, invoice: Invoice) -> None:
        """Равные платежи.

        Args:
            invoice: Фикстура счёта.
        """
        a: Payment = _make_payment(invoice)
        b: Payment = _make_payment(invoice)
        assert a == b
        assert a != "not payment"

    def test_hash(self, invoice: Invoice) -> None:
        """Хеш платежей.

        Args:
            invoice: Фикстура счёта.
        """
        a: Payment = _make_payment(invoice)
        b: Payment = _make_payment(invoice)
        assert hash(a) == hash(b)

    def test_str(self, invoice: Invoice) -> None:
        """str возвращает сумму.

        Args:
            invoice: Фикстура счёта.
        """
        payment: Payment = _make_payment(invoice)
        text: str = str(payment)
        assert "50000" in text
