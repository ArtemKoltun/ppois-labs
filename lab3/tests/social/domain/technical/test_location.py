"""
Тесты класса Location.

Module: tests.social.domain.technical.test_location
"""

from __future__ import annotations

import pytest

from social.domain.technical.location import Location


class TestLocation:
    """Проверки класса Location."""

    def test_creates(self) -> None:
        """Локация создаётся."""
        loc: Location = Location("Россия", "Москва")
        assert loc.country == "Россия"
        assert loc.city == "Москва"
        assert not loc.has_coordinates()

    def test_bad_latitude_raises(self) -> None:
        """Плохая широта недопустима."""
        with pytest.raises(ValueError):
            Location("X", "Y", 100.0, 0.0)

    def test_bad_longitude_raises(self) -> None:
        """Плохая долгота недопустима."""
        with pytest.raises(ValueError):
            Location("X", "Y", 0.0, 200.0)

    def test_full(self) -> None:
        """full возвращает название."""
        loc: Location = Location("Россия", "Москва")
        assert loc.full() == "Россия, Москва"

    def test_has_coordinates(self) -> None:
        """has_coordinates при заданных координатах."""
        with_coords: Location = Location("X", "Y", 55.75, 37.62)
        without: Location = Location("X", "Y")
        assert with_coords.has_coordinates()
        assert not without.has_coordinates()

    def test_distance_to(self) -> None:
        """distance_to считает расстояние."""
        moscow: Location = Location("Россия", "Москва", 55.75, 37.62)
        spb: Location = Location("Россия", "СПб", 59.94, 30.31)
        assert moscow.distance_to(spb) > 0

    def test_equality(self) -> None:
        """Равные по стране и городу."""
        a: Location = Location("Россия", "Москва")
        b: Location = Location("Россия", "Москва", 55.0, 37.0)
        assert a == b
        assert a != "not location"

    def test_hash(self) -> None:
        """Хеш локации."""
        a: Location = Location("Россия", "Москва")
        b: Location = Location("Россия", "Москва")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        loc: Location = Location("Россия", "Москва")
        text: str = str(loc)
        assert "Россия" in text
        assert "Москва" in text

    def test_parse(self) -> None:
        """from_string разбирает локацию."""
        loc: Location = Location.from_string("Россия; Москва; 55.75; 37.62")
        assert loc.country == "Россия"
        assert loc.city == "Москва"
