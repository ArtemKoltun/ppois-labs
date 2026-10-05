"""
Геолокация пользователя.

Module: social.domain.technical.location
"""

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable


class Location(Readable, Writable):
    """Геолокация пользователя.

    Attributes:
        _country: Страна.
        _city: Город.
        _latitude: Широта.
        _longitude: Долгота.
    """

    def __init__(
        self,
        country: str,
        city: str,
        latitude: float = 0.0,
        longitude: float = 0.0,
    ) -> None:
        """Создать локацию.

        Args:
            country: Страна.
            city: Город.
            latitude: Широта.
            longitude: Долгота.

        Raises:
            ValueError: Если координаты вне диапазонов.
        """
        if not -90 <= latitude <= 90:
            raise ValueError("широта должна быть от -90 до 90")
        if not -180 <= longitude <= 180:
            raise ValueError(
                "долгота должна быть от -180 до 180"
            )
        self._country: str = country
        self._city: str = city
        self._latitude: float = latitude
        self._longitude: float = longitude

    @classmethod
    def _parse(cls, text: str) -> Location:
        """Разобрать локацию из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            country=parts[0],
            city=parts[1],
            latitude=float(parts[2]),
            longitude=float(parts[3]),
        )

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

    def full(self) -> str:
        """Полное название.

        Returns:
            Строка.
        """
        return f"{self._country}, {self._city}"

    def has_coordinates(self) -> bool:
        """Проверить наличие координат.

        Returns:
            ``True``, если координаты заданы.
        """
        return self._latitude != 0.0 or self._longitude != 0.0

    def distance_to(self, other: Location) -> float:
        """Приблизительное расстояние по прямой.

        Args:
            other: Другая локация.

        Returns:
            Условное расстояние в градусах.
        """
        dlat: float = self._latitude - other._latitude
        dlon: float = self._longitude - other._longitude
        result: float = (dlat * dlat + dlon * dlon) ** 0.5
        return result

    def __eq__(self, other: object) -> bool:
        """Сравнить две локации.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении страны и города.
        """
        if not isinstance(other, Location):
            return NotImplemented
        return (
            self._country == other._country
            and self._city == other._city
        )

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash((self._country, self._city))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._country}; {self._city}; "
            f"{self._latitude}; {self._longitude}"
        )
