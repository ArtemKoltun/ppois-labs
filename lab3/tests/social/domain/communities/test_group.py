"""
Тесты класса Group.

Module: tests.social.domain.communities.test_group
"""

from __future__ import annotations

from social.domain.communities.community import Community
from social.domain.communities.group import Group


class TestGroup:
    """Проверки класса Group."""

    def test_creates(self) -> None:
        """Группа создаётся."""
        base: Community = Community("Python", "ivan")
        g: Group = Group(base)
        assert g.name == "Python"
        assert not g.is_private
        assert g.posts_count == 0

    def test_add_post(self) -> None:
        """add_post увеличивает счётчик."""
        base: Community = Community("X", "ivan")
        g: Group = Group(base)
        g.add_post()
        assert g.posts_count == 1

    def test_make_public_private(self) -> None:
        """Изменение приватности."""
        base: Community = Community("X", "ivan")
        g: Group = Group(base, is_private=True)
        assert g.is_private
        g.make_public()
        assert not g.is_private
        g.make_private()
        assert g.is_private

    def test_set_rules(self) -> None:
        """set_rules устанавливает правила."""
        base: Community = Community("X", "ivan")
        g: Group = Group(base)
        g.set_rules("Не спамить")
        assert g._rules == "Не спамить"

    def test_is_active(self) -> None:
        """is_active при наличии постов."""
        base: Community = Community("X", "ivan")
        g: Group = Group(base)
        assert not g.is_active()
        g.add_post()
        assert g.is_active()
