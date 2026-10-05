"""
Тесты класса Advertisement.

Module: tests.social.domain.ads.test_advertisement
"""

from __future__ import annotations

import pytest

from common.exceptions import AdCampaignError
from social.domain.ads.advertisement import Advertisement


class TestAdvertisement:
    """Проверки класса Advertisement."""

    def test_creates(self) -> None:
        """Объявление создаётся."""
        a: Advertisement = Advertisement("Купи слона", "Зоомаг", 1000.0)
        assert a.title == "Купи слона"
        assert a.budget == 1000.0
        assert a.impressions == 0
        assert a.clicks == 0

    def test_empty_title_raises(self) -> None:
        """Пустой заголовок недопустим."""
        with pytest.raises(AdCampaignError):
            Advertisement("", "Зоомаг", 1000.0)

    def test_zero_budget_raises(self) -> None:
        """Нулевой бюджет недопустим."""
        with pytest.raises(AdCampaignError):
            Advertisement("X", "Z", 0.0)

    def test_show_click(self) -> None:
        """show и click увеличивают."""
        a: Advertisement = Advertisement("X", "Z", 100.0)
        a.show()
        a.show()
        a.click()
        assert a.impressions == 2
        assert a.clicks == 1

    def test_pause_resume(self) -> None:
        """Пауза и возобновление."""
        a: Advertisement = Advertisement("X", "Z", 100.0)
        a.pause()
        assert not a._is_active
        a.resume()
        assert a._is_active

    def test_ctr(self) -> None:
        """ctr считает."""
        a: Advertisement = Advertisement("X", "Z", 100.0)
        for _ in range(100):
            a.show()
        for _ in range(5):
            a.click()
        assert a.ctr() == 0.05

    def test_ctr_zero_impressions(self) -> None:
        """ctr без показов — 0."""
        a: Advertisement = Advertisement("X", "Z", 100.0)
        assert a.ctr() == 0.0

    def test_cost_per_click(self) -> None:
        """cost_per_click считает."""
        a: Advertisement = Advertisement("X", "Z", 100.0)
        for _ in range(10):
            a.click()
        assert a.cost_per_click() == 10.0

    def test_cost_per_click_zero(self) -> None:
        """Без кликов — 0."""
        a: Advertisement = Advertisement("X", "Z", 100.0)
        assert a.cost_per_click() == 0.0

    def test_is_effective(self) -> None:
        """is_effective при CTR > 2%."""
        good: Advertisement = Advertisement("A", "Z", 100.0)
        bad: Advertisement = Advertisement("B", "Z", 100.0)
        for _ in range(100):
            good.show()
            bad.show()
        for _ in range(5):
            good.click()
        for _ in range(1):
            bad.click()
        assert good.is_effective()
        assert not bad.is_effective()

    def test_equality(self) -> None:
        """Равные по заголовку."""
        a: Advertisement = Advertisement("X", "Z1", 100.0)
        b: Advertisement = Advertisement("X", "Z2", 200.0)
        assert a == b
        assert a != "not ad"

    def test_hash(self) -> None:
        """Хеш объявления."""
        a: Advertisement = Advertisement("X", "Z1", 100.0)
        b: Advertisement = Advertisement("X", "Z2", 200.0)
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        a: Advertisement = Advertisement("X", "Z", 100.0)
        text: str = str(a)
        assert "X" in text
        assert "Z" in text

    def test_parse(self) -> None:
        """from_string разбирает объявление."""
        a: Advertisement = Advertisement.from_string("X; Z; 100")
        assert a.title == "X"
        assert a.budget == 100.0
