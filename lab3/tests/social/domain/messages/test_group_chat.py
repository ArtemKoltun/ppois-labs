"""
Тесты класса GroupChat.

Module: tests.social.domain.messages.test_group_chat
"""

from __future__ import annotations

from social.domain.messages.group_chat import GroupChat


class TestGroupChat:
    """Проверки класса GroupChat."""

    def test_creates(self) -> None:
        """Групповой чат создаётся."""
        g: GroupChat = GroupChat("ivan", "petr", "Друзья")
        assert g.title == "Друзья"
        assert g.participants_count == 2
        assert not g.is_public()

    def test_add_participant(self) -> None:
        """add_participant увеличивает счётчик."""
        g: GroupChat = GroupChat("ivan", "petr", "X")
        g.add_participant()
        assert g.participants_count == 3

    def test_remove_participant(self) -> None:
        """remove_participant уменьшает."""
        g: GroupChat = GroupChat("ivan", "petr", "X")
        g.add_participant()
        g.remove_participant()
        assert g.participants_count == 2

    def test_remove_below_min(self) -> None:
        """Минимум — 2 участника."""
        g: GroupChat = GroupChat("ivan", "petr", "X")
        g.remove_participant()
        assert g.participants_count == 2

    def test_make_public(self) -> None:
        """make_public делает публичным."""
        g: GroupChat = GroupChat("ivan", "petr", "X")
        g.make_public()
        assert g.is_public()

    def test_is_large(self) -> None:
        """is_large при >50 участниках."""
        g: GroupChat = GroupChat("ivan", "petr", "X")
        for _ in range(50):
            g.add_participant()
        assert g.is_large()

    def test_rename(self) -> None:
        """rename меняет название."""
        g: GroupChat = GroupChat("ivan", "petr", "X")
        g.rename("Y")
        assert g.title == "Y"
