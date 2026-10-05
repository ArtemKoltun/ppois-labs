"""
Тесты класса Statistics.

Module: tests.social.domain.ads.test_statistics
"""

from __future__ import annotations

from social.domain.ads.advertisement import Advertisement
from social.domain.ads.statistics import Statistics


class TestStatistics:
    """Проверки класса Statistics."""

    def test_creates(self) -> None:
        """Статистика создаётся."""
        s: Statistics = Statistics("2026-Q1")
        assert s.period == "2026-Q1"
        assert s.advertisements_count() == 0

    def test_add_advertisement(self) -> None:
        """add_advertisement учитывает."""
        s: Statistics = Statistics("2026-Q1")
        a: Advertisement = Advertisement("X", "Z", 100.0)
        for _ in range(10):
            a.show()
        for _ in range(3):
            a.click()
        s.add_advertisement(a)
        assert s.advertisements_count() == 1
        assert s._total_impressions == 10
        assert s._total_clicks == 3

    def test_total_ctr(self) -> None:
        """total_ctr считает."""
        s: Statistics = Statistics("X")
        a: Advertisement = Advertisement("X", "Z", 100.0)
        for _ in range(100):
            a.show()
        for _ in range(10):
            a.click()
        s.add_advertisement(a)
        assert s.total_ctr() == 0.1

    def test_total_ctr_zero(self) -> None:
        """Без показов — 0."""
        s: Statistics = Statistics("X")
        assert s.total_ctr() == 0.0

    def test_is_profitable(self) -> None:
        """is_profitable при CTR > 3%."""
        s: Statistics = Statistics("X")
        a: Advertisement = Advertisement("X", "Z", 100.0)
        for _ in range(100):
            a.show()
        for _ in range(5):
            a.click()
        s.add_advertisement(a)
        assert s.is_profitable()

    def test_best_advertisement_none(self) -> None:
        """best без объявлений — None."""
        s: Statistics = Statistics("X")
        assert s.best_advertisement() is None

    def test_best_advertisement(self) -> None:
        """best возвращает лучшее."""
        s: Statistics = Statistics("X")
        good: Advertisement = Advertisement("Good", "Z", 100.0)
        bad: Advertisement = Advertisement("Bad", "Z", 100.0)
        for _ in range(100):
            good.show()
            bad.show()
        for _ in range(10):
            good.click()
        s.add_advertisement(good)
        s.add_advertisement(bad)
        assert s.best_advertisement() == good

    def test_equality(self) -> None:
        """Равные по периоду."""
        a: Statistics = Statistics("X")
        b: Statistics = Statistics("X")
        assert a == b
        assert a != "not statistics"

    def test_hash(self) -> None:
        """Хеш статистики."""
        a: Statistics = Statistics("X")
        b: Statistics = Statistics("X")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает период."""
        s: Statistics = Statistics("X")
        assert "X" in str(s)

    def test_parse(self) -> None:
        """from_string разбирает статистику."""
        s: Statistics = Statistics.from_string("X")
        assert s.period == "X"
