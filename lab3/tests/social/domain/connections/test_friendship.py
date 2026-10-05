"""
Тесты класса Friendship.

Module: tests.social.domain.connections.test_friendship
"""

from __future__ import annotations

import pytest

from common.exceptions import FriendshipError
from social.domain.connections.friendship import Friendship


class TestFriendship:
    """Проверки класса Friendship."""

    def test_creates(self) -> None:
        """Дружба создаётся."""
        f: Friendship = Friendship("ivan", "petr")
        assert f.first_user == "ivan"
        assert f.second_user == "petr"
        assert not f.is_confirmed

    def test_same_users_raises(self) -> None:
        """С собой дружить нельзя."""
        with pytest.raises(FriendshipError):
            Friendship("ivan", "ivan")

    def test_confirm(self) -> None:
        """confirm подтверждает."""
        f: Friendship = Friendship("ivan", "petr")
        f.confirm()
        assert f.is_confirmed

    def test_increment_days(self) -> None:
        """increment_days увеличивает."""
        f: Friendship = Friendship("ivan", "petr")
        f.increment_days()
        f.increment_days(10)
        assert f._days_friends == 11

    def test_has_user(self) -> None:
        """has_user проверяет участника."""
        f: Friendship = Friendship("ivan", "petr")
        assert f.has_user("ivan")
        assert f.has_user("petr")
        assert not f.has_user("other")

    def test_is_long_term(self) -> None:
        """is_long_term при >365 дней."""
        f: Friendship = Friendship("ivan", "petr")
        f.increment_days(400)
        assert f.is_long_term()

    def test_equality_symmetric(self) -> None:
        """Симметричность."""
        a: Friendship = Friendship("ivan", "petr")
        b: Friendship = Friendship("petr", "ivan")
        assert a == b
        assert a != "not friendship"

    def test_hash_symmetric(self) -> None:
        """Хеш симметричен."""
        a: Friendship = Friendship("ivan", "petr")
        b: Friendship = Friendship("petr", "ivan")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        f: Friendship = Friendship("ivan", "petr")
        text: str = str(f)
        assert "ivan" in text
        assert "petr" in text

    def test_parse(self) -> None:
        """from_string разбирает дружбу."""
        f: Friendship = Friendship.from_string("ivan; petr")
        assert f.first_user == "ivan"
