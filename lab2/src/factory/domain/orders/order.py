"""
Заказ клиента.

Module: factory.domain.orders.order
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.domain.money import Money
from common.enums.order_status import OrderStatus
from common.exceptions.order_exceptions import InvalidOrderException
from factory.domain.orders.customer import Customer
from factory.domain.parts.part import Part


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Order(Readable, Writable):
    """Заказ клиента на изготовление деталей.

    Attributes:
        _number: Номер заказа.
        _customer: Клиент.
        _part: Деталь.
        _quantity: Количество.
        _price: Цена за единицу.
        _status: Статус.
        _deadline: Срок.
        _created_date: Дата создания.
        _notes: Примечания.
    """

    def __init__(
        self,
        number: str,
        customer: Customer,
        part: Part,
        quantity: int,
        price: Money,
        deadline: str,
        created_date: str,
    ) -> None:
        """Создать заказ.

        Args:
            number: Номер.
            customer: Клиент.
            part: Деталь.
            quantity: Количество.
            price: Цена за единицу.
            deadline: Срок.
            created_date: Дата создания.

        Raises:
            InvalidOrderException: Если данные некорректны.
        """
        if not number:
            raise InvalidOrderException("номер не может быть пустым")
        if quantity <= 0:
            raise InvalidOrderException(
                "количество должно быть положительным"
            )
        self._number: str = number
        self._customer: Customer = customer
        self._part: Part = part
        self._quantity: int = quantity
        self._price: Money = price
        self._status: OrderStatus = OrderStatus.NEW
        self._deadline: str = deadline
        self._created_date: str = created_date
        self._notes: str = ""

    @classmethod
    def _parse(cls, text: str) -> "Order":
        """Разобрать заказ из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        customer: Customer = Customer.from_string(parts[1])
        part: Part = Part.from_string(parts[2])
        price: Money = Money(amount=float(parts[4]))
        return cls(
            number=parts[0],
            customer=customer,
            part=part,
            quantity=int(parts[3]),
            price=price,
            deadline=parts[5],
            created_date=parts[6],
        )

    @property
    def number(self) -> str:
        """Номер заказа.

        Returns:
            Строка.
        """
        return self._number

    @property
    def customer(self) -> Customer:
        """Клиент.

        Returns:
            Объект клиента.
        """
        return self._customer

    @property
    def quantity(self) -> int:
        """Количество деталей.

        Returns:
            Целое число.
        """
        return self._quantity

    @property
    def status(self) -> OrderStatus:
        """Статус заказа.

        Returns:
            Элемент перечисления.
        """
        return self._status

    def total_price(self) -> Money:
        """Рассчитать полную стоимость заказа.

        Returns:
            Денежная сумма.
        """
        return self._price.multiply(float(self._quantity))

    def start(self) -> None:
        """Запустить заказ в производство.

        Returns:
            Ничего не возвращает.
        """
        self._status = OrderStatus.IN_PROGRESS

    def complete(self) -> None:
        """Завершить заказ.

        Returns:
            Ничего не возвращает.
        """
        self._status = OrderStatus.COMPLETED

    def ship(self) -> None:
        """Отгрузить заказ.

        Returns:
            Ничего не возвращает.
        """
        self._status = OrderStatus.SHIPPED

    def cancel(self) -> None:
        """Отменить заказ.

        Returns:
            Ничего не возвращает.
        """
        self._status = OrderStatus.CANCELLED

    def is_active(self) -> bool:
        """Проверить, активен ли заказ.

        Returns:
            ``True``, если заказ не завершён.
        """
        return self._status in (
            OrderStatus.NEW,
            OrderStatus.IN_PROGRESS,
        )

    def __eq__(self, other: object) -> bool:
        """Сравнить два заказа.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении номеров.
        """
        if not isinstance(other, Order):
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
            f"{self._number}; {self._customer}; {self._part}; "
            f"{self._quantity}; {self._price.amount}; "
            f"{self._deadline}; {self._created_date}"
        )
