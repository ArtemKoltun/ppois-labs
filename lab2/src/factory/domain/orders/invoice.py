"""
Счёт на оплату.

Module: factory.domain.orders.invoice
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.domain.money import Money
from factory.domain.orders.customer import Customer
from factory.domain.orders.order import Order

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Invoice(Readable, Writable):
    """Счёт на оплату заказа.

    Attributes:
        _number: Номер счёта.
        _order: Заказ.
        _customer: Клиент.
        _amount: Сумма.
        _issue_date: Дата выставления.
        _is_paid: Признак оплаты.
    """

    def __init__(
        self,
        number: str,
        order: Order,
        customer: Customer,
        amount: Money,
        issue_date: str,
    ) -> None:
        """Создать счёт.

        Args:
            number: Номер.
            order: Заказ.
            customer: Клиент.
            amount: Сумма.
            issue_date: Дата.
        """
        self._number: str = number
        self._order: Order = order
        self._customer: Customer = customer
        self._amount: Money = amount
        self._issue_date: str = issue_date
        self._is_paid: bool = False

    @classmethod
    def _parse(cls, text: str) -> Invoice:
        """Разобрать счёт из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        order: Order = Order.from_string(parts[1])
        customer: Customer = Customer.from_string(parts[2])
        return cls(
            number=parts[0],
            order=order,
            customer=customer,
            amount=Money(amount=float(parts[3])),
            issue_date=parts[4],
        )

    @property
    def number(self) -> str:
        """Номер счёта.

        Returns:
            Строка.
        """
        return self._number

    @property
    def amount(self) -> Money:
        """Сумма счёта.

        Returns:
            Денежная сумма.
        """
        return self._amount

    @property
    def is_paid(self) -> bool:
        """Признак оплаты.

        Returns:
            ``True``, если оплачен.
        """
        return self._is_paid

    def mark_paid(self) -> None:
        """Отметить счёт как оплаченный.

        Returns:
            Ничего не возвращает.
        """
        self._is_paid = True

    def cancel(self) -> None:
        """Отменить счёт.

        Returns:
            Ничего не возвращает.
        """
        self._is_paid = False

    def is_overdue(self, current_date: str) -> bool:
        """Проверить, просрочен ли счёт.

        Args:
            current_date: Текущая дата.

        Returns:
            ``True``, если не оплачен и дата позже.

        Note:
            Простое сравнение строк в формате ISO работает
            корректно для дат в формате ``"YYYY-MM-DD"``.
        """
        return not self._is_paid and current_date > self._issue_date

    def __eq__(self, other: object) -> bool:
        """Сравнить два счёта.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении номеров.
        """
        if not isinstance(other, Invoice):
            return NotImplemented
        return self._number == other._number

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._number)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._number}; {self._order}; {self._customer}; "
            f"{self._amount.amount}; {self._issue_date}"
        )
