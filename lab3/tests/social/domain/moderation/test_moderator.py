"""
Тесты класса Moderator.

Module: tests.social.domain.moderation.test_moderator
"""

from __future__ import annotations

import pytest

from social.domain.moderation.moderator import Moderator


class TestModerator:
    """Проверки класса Moderator."""

    def test_creates(self) -> None:
        """Модератор создаётся."""
        m: Moderator = Moderator("admin", level=1)
        assert m.username == "admin"
        assert m.level == 1
        assert m.processed_reports == 0

    def test_bad_level_raises(self) -> None:
        """Плохой уровень недопустим."""
        with pytest.raises(ValueError):
            Moderator("admin", level=10)

    def test_process_report(self) -> None:
        """process_report увеличивает."""
        m: Moderator = Moderator("admin")
        m.process_report()
        assert m.processed_reports == 1

    def test_promote_demote(self) -> None:
        """Повышение и понижение."""
        m: Moderator = Moderator("admin", level=2)
        m.promote()
        assert m.level == 3
        m.demote()
        assert m.level == 2

    def test_promote_at_max(self) -> None:
        """Уровень не выше 5."""
        m: Moderator = Moderator("admin", level=5)
        m.promote()
        assert m.level == 5

    def test_demote_at_min(self) -> None:
        """Уровень не ниже 1."""
        m: Moderator = Moderator("admin", level=1)
        m.demote()
        assert m.level == 1

    def test_deactivate(self) -> None:
        """deactivate отключает."""
        m: Moderator = Moderator("admin")
        m.deactivate()
        assert not m._is_active

    def test_can_ban(self) -> None:
        """can_ban при уровне >= 3."""
        boss: Moderator = Moderator("admin", level=4)
        newbie: Moderator = Moderator("mod", level=1)
        assert boss.can_ban()
        assert not newbie.can_ban()

    def test_equality(self) -> None:
        """Равные по имени."""
        a: Moderator = Moderator("admin", 1)
        b: Moderator = Moderator("admin", 5)
        assert a == b
        assert a != "not moderator"

    def test_hash(self) -> None:
        """Хеш модератора."""
        a: Moderator = Moderator("admin")
        b: Moderator = Moderator("admin")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        m: Moderator = Moderator("admin", 3)
        assert "admin" in str(m)

    def test_parse(self) -> None:
        """from_string разбирает модератора."""
        m: Moderator = Moderator.from_string("admin; 4")
        assert m.username == "admin"
        assert m.level == 4
