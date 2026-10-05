"""
Тесты класса Warning.

Module: tests.social.domain.moderation.test_warning
"""

from __future__ import annotations

from social.domain.moderation.warning import Warning


class TestWarning:
    """Проверки класса Warning."""

    def test_creates(self) -> None:
        """Предупреждение создаётся."""
        w: Warning = Warning("ivan", "admin", "нарушение")
        assert w.username == "ivan"
        assert w.moderator == "admin"
        assert not w.is_acknowledged

    def test_acknowledge(self) -> None:
        """acknowledge принимает."""
        w: Warning = Warning("ivan", "admin", "x")
        w.acknowledge()
        assert w.is_acknowledged

    def test_is_serious(self) -> None:
        """is_serious по слову в причине."""
        s: Warning = Warning("ivan", "admin", "нарушение правил")
        n: Warning = Warning("ivan", "admin", "просто так")
        assert s.is_serious()
        assert not n.is_serious()

    def test_equality(self) -> None:
        """Равные по имени и причине."""
        a: Warning = Warning("ivan", "admin", "x")
        b: Warning = Warning("ivan", "mod", "x")
        assert a == b
        assert a != "not warning"

    def test_hash(self) -> None:
        """Хеш предупреждения."""
        a: Warning = Warning("ivan", "admin", "x")
        b: Warning = Warning("ivan", "mod", "x")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        w: Warning = Warning("ivan", "admin", "x")
        assert "ivan" in str(w)

    def test_parse(self) -> None:
        """from_string разбирает предупреждение."""
        w: Warning = Warning.from_string("ivan; admin; причина")
        assert w.username == "ivan"
        assert w.reason == "причина"
