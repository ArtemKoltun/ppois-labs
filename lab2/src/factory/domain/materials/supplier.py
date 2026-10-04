"""
Поставщик материалов.

Module: factory.domain.materials.supplier
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

class Supplier(Readable, Writable):
    """Поставщик материалов.

    Attributes:
        _name: Наименование.
        _address: Адрес.
        _contact_person: Контактное лицо.
        _phone: Телефон.
        _rating: Рейтинг от 0 до 5.
    """

    def __init__(
        self,
        name: str,
        address: Address,
        contact_person: str,
        phone: str,
        rating: float = 0.0,
    ) -> None:
        """Создать поставщика.

        Args:
            name: Наименование.
            address: Адрес.
            contact_person: Контактное лицо.
            phone: Телефон.
            rating: Рейтинг.

        Raises:
            ValueError: Если рейтинг вне диапазона.
        """
        if not 0 <= rating <= 5:
            raise ValueError("рейтинг должен быть от 0 до 5")
        self._name: str = name
        self._address: Address = address
        self._contact_person: str = contact_person
        self._phone: str = phone
        self._rating: float = rating

    @classmethod
    def _parse(cls, text: str) -> Supplier:
        """Разобрать поставщика из строки.

        Args:
            text: Строка с полями через запятую.

        Returns:
            Новый экземпляр ``Supplier``.
        """
        parts: list[str] = [p.strip() for p in text.split(",")]
        address: Address = Address(
            country=parts[1], city=parts[2],
            street=parts[3], building=parts[4],
            postal_code=parts[5],
        )
        return cls(
            name=parts[0],
            address=address,
            contact_person=parts[6],
            phone=parts[7],
            rating=float(parts[8]),
        )

    @property
    def name(self) -> str:
        """Наименование.

        Returns:
            Строка.
        """
        return self._name

    @property
    def rating(self) -> float:
        """Рейтинг.

        Returns:
            Число от 0 до 5.
        """
        return self._rating

    def update_rating(self, new_rating: float) -> None:
        """Обновить рейтинг.

        Args:
            new_rating: Новый рейтинг.

        Returns:
            Ничего не возвращает.

        Raises:
            ValueError: Если рейтинг вне диапазона.
        """
        if not 0 <= new_rating <= 5:
            raise ValueError("рейтинг должен быть от 0 до 5")
        self._rating = new_rating

    def get_contact_info(self) -> str:
        """Вернуть контактную информацию.

        Returns:
            Строка с контактами.
        """
        return f"{self._contact_person}, {self._phone}"

    def is_reliable(self) -> bool:
        """Проверить, надёжен ли поставщик.

        Returns:
            ``True``, если рейтинг не ниже 4.
        """
        return self._rating >= 4.0

    def __eq__(self, other: object) -> bool:
        """Сравнить двух поставщиков.

        Args:
            other: Другой объект.

        Returns:
            ``True``, если совпадают имена.
        """
        if not isinstance(other, Supplier):
            return NotImplemented
        return self._name == other._name

    def __hash__(self) -> int:
        """Вернуть хеш поставщика.

        Returns:
            Целое число.
        """
        return hash(self._name)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через запятую.
        """
        return (
            f"{self._name}, {self._address.country}, "
            f"{self._address.city}, {self._address.street}, "
            f"{self._address.building}, {self._address.postal_code}, "
            f"{self._contact_person}, {self._phone}, {self._rating}"
        )
