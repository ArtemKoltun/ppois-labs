"""
Тесты класса GroupRole.

Module: tests.social.domain.communities.test_group_role
"""

from __future__ import annotations

from social.domain.communities.group_role import GroupRole


class TestGroupRole:
    """Проверки класса GroupRole."""

    def test_creates(self) -> None:
        """Роль создаётся."""
        r: GroupRole = GroupRole("Member")
        assert r.name == "Member"

    def test_grant_revoke_moderation(self) -> None:
        """Выдача и отзыв модерации."""
        r: GroupRole = GroupRole("M")
        assert not r._can_moderate
        r.grant_moderation()
        assert r._can_moderate
        r.revoke_moderation()
        assert not r._can_moderate

    def test_is_admin(self) -> None:
        """is_admin при обоих правах."""
        admin: GroupRole = GroupRole(
            "A", can_post=True, can_moderate=True
        )
        member: GroupRole = GroupRole("M", can_post=True)
        assert admin.is_admin()
        assert not member.is_admin()

    def test_can_interact(self) -> None:
        """can_interact при хотя бы одном праве."""
        ok: GroupRole = GroupRole("X", can_post=True)
        nope: GroupRole = GroupRole("Y", can_post=False)
        assert ok.can_interact()
        assert not nope.can_interact()

    def test_equality(self) -> None:
        """Равные по имени."""
        a: GroupRole = GroupRole("X")
        b: GroupRole = GroupRole("X", can_post=False)
        assert a == b
        assert a != "not role"

    def test_hash(self) -> None:
        """Хеш роли."""
        a: GroupRole = GroupRole("X")
        b: GroupRole = GroupRole("X")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает имя."""
        assert "Admin" in str(GroupRole("Admin"))

    def test_parse(self) -> None:
        """from_string разбирает роль."""
        r: GroupRole = GroupRole.from_string("Admin; true; true")
        assert r.name == "Admin"
        assert r._can_moderate
