"""
Платёж по счёту.

Module: factory.domain.orders.payment
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.domain.money import Money
from factory.domain.orders.invoice import Invoice


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Payment(Readable, Writable):
    """Платёж по счёту.

    Attributes:
        _invoice: Счёт.
        _amount: Сумма платежа.
        _date: Дата платежа.
        _method: Способ оплаты.
    """

    def __init__(
        self,
        invoice: Invoice,
        amount: Money,
        date: str,
        method: str = "bank_transfer",
    ) -> None:
        """Создать платёж.

        Args:
            invoice: Счёт.
            amount: Сумма.
            date: Дата.
            method: Способ оплаты.
        """
        self._invoice: Invoice = invoice
        self._amount: Money = amount
        self._date: str = date
        self._method: str = method

    @classmethod
    def _parse(cls, text: str) -> "Payment":
        """Разобрать платёж из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        invoice: Invoice = Invoice.from_string(parts[0])
        return cls(
            invoice=invoice,
            amount=Money(amount=float(parts[1])),
            date=parts[2],
            method=parts[3],
        )

    @property
    def amount(self) -> Money:
        """Сумма платежа.

        Returns:
            Денежная сумма.
        """
        return self._amount

    @property
    def method(self) -> str:
        """Способ оплаты.

        Returns:
            Строка.
        """
        return self._method

    def covers_invoice(self) -> bool:
        """Проверить, покрывает ли платёж счёт.

        Returns:
            ``True``, если сумма не меньше суммы счёта.
        """
        return self._amount.amount >= self._invoice.amount.amount

    def is_electronic(self) -> bool:
        """Проверить, электронный ли платёж.

        Returns:
            ``True``, если способ не «cash».
        """
        return self._method != "cash"

    def __eq__(self, other: object) -> bool:
        """Сравнить два платежа.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении счёта и даты.
        """
        if not isinstance(other, Payment):
            return NotImplemented
        return (
            self._invoice == other._invoice
            and self._date == other._date
        )

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash((self._invoice, self._date))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._invoice}; {self._amount.amount}; "
            f"{self._date}; {self._method}"
        )
