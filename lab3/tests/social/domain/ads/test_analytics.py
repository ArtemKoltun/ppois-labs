"""
Тесты класса Analytics.

Module: tests.social.domain.ads.test_analytics
"""

from __future__ import annotations

from social.domain.ads.analytics import Analytics


class TestAnalytics:
    """Проверки класса Analytics."""

    def test_creates(self) -> None:
        """Аналитика создаётся."""
        a: Analytics = Analytics("ivan")
        assert a.user == "ivan"
        assert a.views == 0

    def test_add_view(self) -> None:
        """add_view увеличивает."""
        a: Analytics = Analytics("ivan")
        a.add_view()
        assert a.views == 1

    def test_add_like(self) -> None:
        """add_like увеличивает."""
        a: Analytics = Analytics("ivan")
        a.add_like()
        assert a._likes == 1

    def test_add_share(self) -> None:
        """add_share увеличивает."""
        a: Analytics = Analytics("ivan")
        a.add_share()
        assert a._shares == 1

    def test_add_session(self) -> None:
        """add_session добавляет минуты."""
        a: Analytics = Analytics("ivan")
        a.add_session(30)
        assert a._session_minutes == 30

    def test_engagement_rate(self) -> None:
        """engagement_rate считает."""
        a: Analytics = Analytics("ivan")
        for _ in range(100):
            a.add_view()
        for _ in range(3):
            a.add_like()
        for _ in range(2):
            a.add_share()
        assert a.engagement_rate() == 0.05

    def test_engagement_rate_zero(self) -> None:
        """Без просмотров — 0."""
        a: Analytics = Analytics("ivan")
        assert a.engagement_rate() == 0.0

    def test_is_engaged(self) -> None:
        """is_engaged при >5%."""
        a: Analytics = Analytics("ivan")
        for _ in range(100):
            a.add_view()
        for _ in range(10):
            a.add_like()
        assert a.is_engaged()

    def test_equality(self) -> None:
        """Равные по пользователю."""
        a: Analytics = Analytics("ivan")
        b: Analytics = Analytics("ivan")
        assert a == b
        assert a != "not analytics"

    def test_hash(self) -> None:
        """Хеш аналитики."""
        a: Analytics = Analytics("ivan")
        b: Analytics = Analytics("ivan")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает пользователя."""
        a: Analytics = Analytics("ivan")
        assert "ivan" in str(a)

    def test_parse(self) -> None:
        """from_string разбирает аналитику."""
        a: Analytics = Analytics.from_string("ivan")
        assert a.user == "ivan"
