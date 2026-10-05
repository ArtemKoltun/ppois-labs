"""
Тесты класса Follow.

Module: tests.social.domain.connections.test_follow
"""

from __future__ import annotations

import pytest

from common.exceptions import FriendshipError
from social.domain.connections.follow import Follow


class TestFollow:
    """Проверки класса Follow."""

    def test_creates(self) -> None:
        """Подписка создаётся."""
        f: Follow = Follow("ivan", "petr")
        assert f.follower == "ivan"
        assert f.following == "petr"
        assert f.is_active

    def test_same_users_raises(self) -> None:
        """На себя подписаться нельзя."""
        with pytest.raises(FriendshipError):
            Follow("ivan", "ivan")

    def test_unfollow_reactivate(self) -> None:
        """Отписка и восстановление."""
        f: Follow = Follow("ivan", "petr")
        f.unfollow()
        assert not f.is_active
        f.reactivate()
        assert f.is_active

    def test_is_mutual(self) -> None:
        """is_mutual проверяет взаимность."""
        a: Follow = Follow("ivan", "petr")
        b: Follow = Follow("petr", "ivan")
        c: Follow = Follow("ivan", "other")
        assert a.is_mutual(b)
        assert not a.is_mutual(c)

    def test_equality(self) -> None:
        """Равные по паре."""
        a: Follow = Follow("ivan", "petr")
        b: Follow = Follow("ivan", "petr")
        assert a == b
        assert a != "not follow"

    def test_hash(self) -> None:
        """Хеш подписки."""
        a: Follow = Follow("ivan", "petr")
        b: Follow = Follow("ivan", "petr")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        f: Follow = Follow("ivan", "petr")
        assert "ivan" in str(f)

    def test_parse(self) -> None:
        """from_string разбирает подписку."""
        f: Follow = Follow.from_string("ivan; petr")
        assert f.follower == "ivan"
        assert f.following == "petr"
