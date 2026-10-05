"""
Тесты класса Event.

Module: tests.social.domain.communities.test_event
"""

from __future__ import annotations

import pytest

from common.exceptions import ContentModerationError
from social.domain.communities.event import Event


class TestEvent:
    """Проверки класса Event."""

    def test_creates(self) -> None:
        """Событие создаётся."""
        e: Event = Event("PyMeetup", "Python Devs", "2026-06-01")
        assert e.title == "PyMeetup"
        assert e.date == "2026-06-01"
        assert e.participants_count == 0

    def test_empty_title_raises(self) -> None:
        """Пустое название недопустимо."""
        with pytest.raises(ContentModerationError):
            Event("", "Org", "2026")

    def test_add_remove_participant(self) -> None:
        """Добавление и удаление участников."""
        e: Event = Event("X", "Org", "2026")
        e.add_participant()
        e.add_participant()
        assert e.participants_count == 2
        e.remove_participant()
        assert e.participants_count == 1

    def test_remove_below_zero(self) -> None:
        """Минимум — 0 участников."""
        e: Event = Event("X", "Org", "2026")
        e.remove_participant()
        assert e.participants_count == 0

    def test_make_online(self) -> None:
        """make_online переводит в онлайн."""
        e: Event = Event("X", "Org", "2026", "Москва", False)
        e.make_online()
        assert e.is_online()

    def test_is_large(self) -> None:
        """is_large при >1000."""
        e: Event = Event("X", "Org", "2026")
        for _ in range(1001):
            e.add_participant()
        assert e.is_large()

    def test_equality(self) -> None:
        """Равные по названию и дате."""
        a: Event = Event("X", "O1", "2026")
        b: Event = Event("X", "O2", "2026")
        assert a == b
        assert a != "not event"

    def test_hash(self) -> None:
        """Хеш события."""
        a: Event = Event("X", "O1", "2026")
        b: Event = Event("X", "O2", "2026")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        e: Event = Event("X", "Org", "2026")
        assert "X" in str(e)

    def test_parse(self) -> None:
        """from_string разбирает событие."""
        e: Event = Event.from_string("X; Org; 2026; Москва; true")
        assert e.title == "X"
        assert e.is_online()
