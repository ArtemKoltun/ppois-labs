"""
Тесты класса GroupMember.

Module: tests.social.domain.communities.test_group_member
"""

from __future__ import annotations

from social.domain.communities.group_member import GroupMember
from social.domain.communities.group_role import GroupRole


class TestGroupMember:
    """Проверки класса GroupMember."""

    def test_creates(self) -> None:
        """Участник создаётся."""
        role: GroupRole = GroupRole("Member")
        m: GroupMember = GroupMember("ivan", "Python", role)
        assert m.username == "ivan"
        assert m.role == role

    def test_change_role(self) -> None:
        """change_role меняет роль."""
        role: GroupRole = GroupRole("Member")
        admin: GroupRole = GroupRole("Admin", True, True)
        m: GroupMember = GroupMember("ivan", "G", role)
        m.change_role(admin)
        assert m.role == admin

    def test_leave_rejoin(self) -> None:
        """Выход и возврат."""
        role: GroupRole = GroupRole("M")
        m: GroupMember = GroupMember("ivan", "G", role)
        m.leave()
        assert not m._is_active
        m.rejoin()
        assert m._is_active

    def test_can_moderate(self) -> None:
        """can_moderate через роль."""
        admin: GroupRole = GroupRole("A", True, True)
        member: GroupRole = GroupRole("M", True)
        m1: GroupMember = GroupMember("ivan", "G", admin)
        m2: GroupMember = GroupMember("petr", "G", member)
        assert m1.can_moderate()
        assert not m2.can_moderate()

    def test_equality(self) -> None:
        """Равные по (участник, группа)."""
        role: GroupRole = GroupRole("M")
        a: GroupMember = GroupMember("ivan", "G1", role)
        b: GroupMember = GroupMember("ivan", "G1", role)
        assert a == b
        assert a != "not member"

    def test_hash(self) -> None:
        """Хеш участника."""
        role: GroupRole = GroupRole("M")
        a: GroupMember = GroupMember("ivan", "G1", role)
        b: GroupMember = GroupMember("ivan", "G1", role)
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        role: GroupRole = GroupRole("M")
        m: GroupMember = GroupMember("ivan", "G1", role)
        assert "ivan" in str(m)

    def test_parse(self) -> None:
        """from_string разбирает участника."""
        m: GroupMember = GroupMember.from_string("ivan; G; M; true; false")
        assert m.username == "ivan"
