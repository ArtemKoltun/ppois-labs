"""
Договор с клиентом.

Module: factory.domain.orders.contract
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.domain.money import Money
from factory.domain.orders.customer import Customer


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Contract(Readable, Writable):
    """Договор на поставку деталей.

    Attributes:
        _number: Номер договора.
        _customer: Клиент.
        _sign_date: Дата подписания.
        _valid_until: Срок действия.
        _total_amount: Общая сумма.
        _is_signed: Подписан ли.
    """

    def __init__(
        self,
        number: str,
        customer: Customer,
        sign_date: str,
        valid_until: str,
        total_amount: Money,
    ) -> None:
        """Создать договор.

        Args:
            number: Номер.
            customer: Клиент.
            sign_date: Дата подписания.
            valid_until: Срок действия.
            total_amount: Сумма.
        """
        self._number: str = number
        self._customer: Customer = customer
        self._sign_date: str = sign_date
        self._valid_until: str = valid_until
        self._total_amount: Money = total_amount
        self._is_signed: bool = False

    @classmethod
    def _parse(cls, text: str) -> "Contract":
        """Разобрать договор из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        customer: Customer = Customer.from_string(parts[1])
        return cls(
            number=parts[0],
            customer=customer,
            sign_date=parts[2],
            valid_until=parts[3],
            total_amount=Money(amount=float(parts[4])),
        )

    @property
    def number(self) -> str:
        """Номер договора.

        Returns:
            Строка.
        """
        return self._number

    @property
    def is_signed(self) -> bool:
        """Признак подписания.

        Returns:
            ``True``, если подписан.
        """
        return self._is_signed

    def sign(self) -> None:
        """Подписать договор.

        Returns:
            Ничего не возвращает.
        """
        self._is_signed = True

    def terminate(self) -> None:
        """Расторгнуть договор.

        Returns:
            Ничего не возвращает.
        """
        self._is_signed = False

    def is_valid(self) -> bool:
        """Проверить, действителен ли договор.

        Returns:
            ``True``, если подписан и не расторгнут.
        """
        return self._is_signed

    def __eq__(self, other: object) -> bool:
        """Сравнить два договора.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении номеров.
        """
        if not isinstance(other, Contract):
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
            f"{self._number}; {self._customer}; "
            f"{self._sign_date}; {self._valid_until}; "
            f"{self._total_amount.amount}"
        )
