"""
Клиент завода.

Module: factory.domain.orders.customer
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.domain.address import Address

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Customer(Readable, Writable):
    """Клиент завода — покупатель деталей.

    Attributes:
        _name: Наименование организации.
        _address: Юридический адрес.
        _inn: ИНН.
        _contact_person: Контактное лицо.
        _phone: Телефон.
    """

    def __init__(
        self,
        name: str,
        address: Address,
        inn: str,
        contact_person: str,
        phone: str,
    ) -> None:
        """Создать клиента.

        Args:
            name: Наименование.
            address: Адрес.
            inn: ИНН.
            contact_person: Контактное лицо.
            phone: Телефон.

        Raises:
            ValueError: Если имя или ИНН пусты.
        """
        if not name:
            raise ValueError("имя клиента не может быть пустым")
        if not inn:
            raise ValueError("ИНН не может быть пустым")
        self._name: str = name
        self._address: Address = address
        self._inn: str = inn
        self._contact_person: str = contact_person
        self._phone: str = phone

    @classmethod
    def _parse(cls, text: str) -> Customer:
        """Разобрать клиента из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        address: Address = Address(
            country=parts[1],
            city=parts[2],
            street=parts[3],
            building=parts[4],
            postal_code=parts[5],
        )
        return cls(
            name=parts[0],
            address=address,
            inn=parts[6],
            contact_person=parts[7],
            phone=parts[8],
        )

    @property
    def name(self) -> str:
        """Наименование.

        Returns:
            Строка.
        """
        return self._name

    @property
    def inn(self) -> str:
        """ИНН.

        Returns:
            Строка.
        """
        return self._inn

    def is_company(self) -> bool:
        """Проверить, юридическое ли лицо.

        Returns:
            ``True``, если ИНН длиной 10 цифр.
        """
        return len(self._inn) == 10

    def update_contact(self, person: str, phone: str) -> None:
        """Обновить контактные данные.

        Args:
            person: Контактное лицо.
            phone: Телефон.

        Returns:
            Ничего не возвращает.
        """
        self._contact_person = person
        self._phone = phone

    def __eq__(self, other: object) -> bool:
        """Сравнить двух клиентов.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении ИНН.
        """
        if not isinstance(other, Customer):
            return NotImplemented
        return self._inn == other._inn

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._inn)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._name}; {self._address.country}; "
            f"{self._address.city}; {self._address.street}; "
            f"{self._address.building}; {self._address.postal_code}; "
            f"{self._inn}; {self._contact_person}; {self._phone}"
        )
