"""
Тесты класса Ban.

Module: tests.social.domain.moderation.test_ban
"""

from __future__ import annotations

from social.domain.moderation.ban import Ban


class TestBan:
    """Проверки класса Ban."""

    def test_creates(self) -> None:
        """Блокировка создаётся."""
        b: Ban = Ban("spammer", "admin", "спам")
        assert b.username == "spammer"
        assert b.moderator == "admin"
        assert not b.is_permanent

    def test_change_reason(self) -> None:
        """change_reason меняет причину."""
        b: Ban = Ban("spammer", "admin", "спам")
        b.change_reason("другая")
        assert b.reason == "другая"

    def test_make_permanent(self) -> None:
        """make_permanent делает вечной."""
        b: Ban = Ban("spammer", "admin", "x")
        b.make_permanent()
        assert b.is_permanent

    def test_is_appealable(self) -> None:
        """is_appealable зависит от перманентности."""
        temp: Ban = Ban("a", "admin", "x", is_permanent=False)
        perm: Ban = Ban("a", "admin", "x", is_permanent=True)
        assert temp.is_appealable()
        assert not perm.is_appealable()

    def test_equality(self) -> None:
        """Равные по имени."""
        a: Ban = Ban("spammer", "admin", "x")
        b: Ban = Ban("spammer", "mod", "y")
        assert a == b
        assert a != "not ban"

    def test_hash(self) -> None:
        """Хеш блокировки."""
        a: Ban = Ban("spammer", "admin", "x")
        b: Ban = Ban("spammer", "mod", "y")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        b: Ban = Ban("spammer", "admin", "спам")
        assert "spammer" in str(b)

    def test_parse(self) -> None:
        """from_string разбирает блокировку."""
        b: Ban = Ban.from_string("spammer; admin; спам; true")
        assert b.username == "spammer"
        assert b.is_permanent
