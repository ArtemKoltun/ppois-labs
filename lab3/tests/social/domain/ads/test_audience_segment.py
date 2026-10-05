"""
Тесты класса AudienceSegment.

Module: tests.social.domain.ads.test_audience_segment
"""

from __future__ import annotations

import pytest

from social.domain.ads.audience_segment import AudienceSegment


class TestAudienceSegment:
    """Проверки класса AudienceSegment."""

    def test_creates(self) -> None:
        """Сегмент создаётся."""
        s: AudienceSegment = AudienceSegment("Молодёжь", 18, 25)
        assert s.name == "Молодёжь"
        assert s.users_count == 0

    def test_bad_ages_raise(self) -> None:
        """Плохие возрасты недопустимы."""
        with pytest.raises(ValueError):
            AudienceSegment("X", 30, 20)

    def test_add_users(self) -> None:
        """add_users увеличивает."""
        s: AudienceSegment = AudienceSegment("X", 18, 25)
        s.add_users(1000)
        assert s.users_count == 1000

    def test_matches_age(self) -> None:
        """matches_age проверяет диапазон."""
        s: AudienceSegment = AudienceSegment("X", 18, 25)
        assert s.matches_age(20)
        assert not s.matches_age(30)
        assert not s.matches_age(15)

    def test_is_large(self) -> None:
        """is_large при >100 000."""
        s: AudienceSegment = AudienceSegment("X", 18, 25)
        s.add_users(100_001)
        assert s.is_large()

    def test_equality(self) -> None:
        """Равные по имени."""
        a: AudienceSegment = AudienceSegment("X", 18, 25)
        b: AudienceSegment = AudienceSegment("X", 30, 40)
        assert a == b
        assert a != "not segment"

    def test_hash(self) -> None:
        """Хеш сегмента."""
        a: AudienceSegment = AudienceSegment("X", 18, 25)
        b: AudienceSegment = AudienceSegment("X", 30, 40)
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        s: AudienceSegment = AudienceSegment("X", 18, 25)
        text: str = str(s)
        assert "X" in text
        assert "18" in text

    def test_parse(self) -> None:
        """from_string разбирает сегмент."""
        s: AudienceSegment = AudienceSegment.from_string("X; 18; 25")
        assert s.name == "X"
        assert s._age_min == 18
