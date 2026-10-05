"""
Тесты класса AdCampaign.

Module: tests.social.domain.ads.test_ad_campaign
"""

from __future__ import annotations

import pytest

from common.exceptions import AdCampaignError
from social.domain.ads.ad_campaign import AdCampaign
from social.domain.ads.advertisement import Advertisement


class TestAdCampaign:
    """Проверки класса AdCampaign."""

    def test_creates(self) -> None:
        """Кампания создаётся."""
        c: AdCampaign = AdCampaign("Лето 2026", 100000.0)
        assert c.name == "Лето 2026"
        assert c.total_budget == 100000.0
        assert not c.is_running()

    def test_empty_name_raises(self) -> None:
        """Пустое имя недопустимо."""
        with pytest.raises(AdCampaignError):
            AdCampaign("", 100.0)

    def test_zero_budget_raises(self) -> None:
        """Нулевой бюджет недопустим."""
        with pytest.raises(AdCampaignError):
            AdCampaign("X", 0.0)

    def test_negative_age_raises(self) -> None:
        """Отрицательный возраст недопустим."""
        with pytest.raises(AdCampaignError):
            AdCampaign("X", 100.0, target_age_min=-1)

    def test_add_advertisement(self) -> None:
        """add_advertisement добавляет."""
        c: AdCampaign = AdCampaign("X", 100.0)
        c.add_advertisement(Advertisement("A", "Z", 50.0))
        assert c.advertisements_count() == 1

    def test_start_without_ads_raises(self) -> None:
        """Запуск без объявлений падает."""
        c: AdCampaign = AdCampaign("X", 100.0)
        with pytest.raises(AdCampaignError):
            c.start()

    def test_start_stop(self) -> None:
        """Запуск и остановка."""
        c: AdCampaign = AdCampaign("X", 100.0)
        c.add_advertisement(Advertisement("A", "Z", 50.0))
        c.start()
        assert c.is_running()
        c.stop()
        assert not c.is_running()

    def test_total_clicks(self) -> None:
        """total_clicks суммирует."""
        c: AdCampaign = AdCampaign("X", 100.0)
        a: Advertisement = Advertisement("A", "Z", 50.0)
        for _ in range(3):
            a.click()
        c.add_advertisement(a)
        assert c.total_clicks() == 3

    def test_equality(self) -> None:
        """Равные по имени."""
        a: AdCampaign = AdCampaign("X", 100.0)
        b: AdCampaign = AdCampaign("X", 200.0)
        assert a == b
        assert a != "not campaign"

    def test_hash(self) -> None:
        """Хеш кампании."""
        a: AdCampaign = AdCampaign("X", 100.0)
        b: AdCampaign = AdCampaign("X", 200.0)
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        c: AdCampaign = AdCampaign("X", 100.0)
        assert "X" in str(c)

    def test_parse(self) -> None:
        """from_string разбирает кампанию."""
        c: AdCampaign = AdCampaign.from_string("X; 100; 18")
        assert c.name == "X"
        assert c._target_age_min == 18
