"""
Адрес.

Module: common.domain.address
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Address:
    """Почтовый адрес.

    Attributes:
        _country: Страна.
        _city: Город.
        _street: Улица.
        _building: Номер дома.
        _postal_code: Почтовый индекс.
    """

    # -----------------------------------------------------------------------
    # Constructors
    # -----------------------------------------------------------------------

    def __init__(
        self,
        country: str,
        city: str,
        street: str,
        building: str,
        postal_code: str,
    ) -> None:
        """Создать адрес.

        Args:
            country: Страна.
            city: Город.
            street: Улица.
            building: Номер дома.
            postal_code: Почтовый индекс.

        Raises:
            ValueError: Если любое поле пустое.
        """
        for name, value in (
            ("country", country),
            ("city", city),
            ("street", street),
            ("building", building),
            ("postal_code", postal_code),
        ):
            if not value:
                raise ValueError(f"поле {name} не может быть пустым")
        self._country: str = country
        self._city: str = city
        self._street: str = street
        self._building: str = building
        self._postal_code: str = postal_code

    # -----------------------------------------------------------------------
    # Properties
    # -----------------------------------------------------------------------

    @property
    def country(self) -> str:
        """Страна.

        Returns:
            Строка.
        """
        return self._country

    @property
    def city(self) -> str:
        """Город.

        Returns:
            Строка.
        """
        return self._city

    @property
    def street(self) -> str:
        """Улица.

        Returns:
            Строка.
        """
        return self._street

    @property
    def building(self) -> str:
        """Номер дома.

        Returns:
            Строка.
        """
        return self._building

    @property
    def postal_code(self) -> str:
        """Почтовый индекс.

        Returns:
            Строка.
        """
        return self._postal_code

    # -----------------------------------------------------------------------
    # Public methods
    # -----------------------------------------------------------------------

    def full(self) -> str:
        """Вернуть полный адрес одной строкой.

        Returns:
            Строка вида ``"Россия, Москва, Тверская, 1, 101000"``.
        """
        return (
            f"{self._country}, {self._city}, "
            f"{self._street}, {self._building}, "
            f"{self._postal_code}"
        )

    # -----------------------------------------------------------------------
    # Magic methods
    # -----------------------------------------------------------------------

    def __eq__(self, other: object) -> bool:
        """Сравнить два адреса.

        Args:
            other: Другой объект.

        Returns:
            ``True``, если все поля совпадают.
        """
        if not isinstance(other, Address):
            return NotImplemented
        return (
            self._country == other._country
            and self._city == other._city
            and self._street == other._street
            and self._building == other._building
            and self._postal_code == other._postal_code
        )

    def __hash__(self) -> int:
        """Вернуть хеш адреса.

        Returns:
            Целое число.
        """
        return hash((
            self._country,
            self._city,
            self._street,
            self._building,
            self._postal_code,
        ))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Полный адрес одной строкой.
        """
        return self.full()
