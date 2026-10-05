"""
Тесты класса Subscription.

Module: tests.social.domain.connections.test_subscription
"""

from __future__ import annotations

import pytest

from common.exceptions import FriendshipError
from social.domain.connections.subscription import Subscription


class TestSubscription:
    """Проверки класса Subscription."""

    def test_creates(self) -> None:
        """Подписка создаётся."""
        s: Subscription = Subscription("ivan", "author", 500.0)
        assert s.subscriber == "ivan"
        assert s.author == "author"
        assert s.months == 1

    def test_same_users_raises(self) -> None:
        """На себя подписаться нельзя."""
        with pytest.raises(FriendshipError):
            Subscription("ivan", "ivan", 500.0)

    def test_zero_price_raises(self) -> None:
        """Нулевая цена недопустима."""
        with pytest.raises(FriendshipError):
            Subscription("ivan", "author", 0.0)

    def test_total_price(self) -> None:
        """total_price считает."""
        s: Subscription = Subscription("ivan", "a", 500.0, 12)
        assert s.total_price() == 6000.0

    def test_extend(self) -> None:
        """extend продлевает."""
        s: Subscription = Subscription("ivan", "a", 500.0, 1)
        s.extend(11)
        assert s.months == 12

    def test_is_annual(self) -> None:
        """is_annual при >=12."""
        annual: Subscription = Subscription("i", "a", 1.0, 12)
        monthly: Subscription = Subscription("i", "a", 1.0, 1)
        assert annual.is_annual()
        assert not monthly.is_annual()

    def test_equality(self) -> None:
        """Равные по паре."""
        a: Subscription = Subscription("ivan", "a", 500.0)
        b: Subscription = Subscription("ivan", "a", 100.0)
        assert a == b
        assert a != "not subscription"

    def test_hash(self) -> None:
        """Хеш подписки."""
        a: Subscription = Subscription("ivan", "a", 500.0)
        b: Subscription = Subscription("ivan", "a", 100.0)
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        s: Subscription = Subscription("ivan", "a", 500.0)
        assert "ivan" in str(s)

    def test_parse(self) -> None:
        """from_string разбирает подписку."""
        s: Subscription = Subscription.from_string("ivan; a; 500; 3")
        assert s.months == 3
