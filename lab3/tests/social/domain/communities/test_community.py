"""
Тесты класса Community.

Module: tests.social.domain.communities.test_community
"""

from __future__ import annotations

import pytest

from common.exceptions import ContentModerationError
from social.domain.communities.community import Community


class TestCommunity:
    """Проверки класса Community."""

    def test_creates(self) -> None:
        """Сообщество создаётся."""
        c: Community = Community("Python Devs", "ivan")
        assert c.name == "Python Devs"
        assert c.owner == "ivan"
        assert c.members_count == 1
        assert not c.is_verified

    def test_empty_name_raises(self) -> None:
        """Пустое имя недопустимо."""
        with pytest.raises(ContentModerationError):
            Community("", "ivan")

    def test_empty_owner_raises(self) -> None:
        """Пустой владелец недопустим."""
        with pytest.raises(ContentModerationError):
            Community("X", "")

    def test_add_remove_member(self) -> None:
        """Добавление и удаление участников."""
        c: Community = Community("X", "ivan")
        c.add_member()
        c.add_member()
        assert c.members_count == 3
        c.remove_member()
        assert c.members_count == 2

    def test_remove_below_one(self) -> None:
        """Минимум — 1 участник."""
        c: Community = Community("X", "ivan")
        c.remove_member()
        assert c.members_count == 1

    def test_update_description(self) -> None:
        """update_description меняет описание."""
        c: Community = Community("X", "ivan")
        c.update_description("Новое описание")
        assert c._description == "Новое описание"

    def test_verify(self) -> None:
        """verify верифицирует."""
        c: Community = Community("X", "ivan")
        c.verify()
        assert c.is_verified

    def test_transfer_ownership(self) -> None:
        """transfer_ownership меняет владельца."""
        c: Community = Community("X", "ivan")
        c.transfer_ownership("petr")
        assert c.owner == "petr"

    def test_is_popular(self) -> None:
        """is_popular при >10 000."""
        c: Community = Community("X", "ivan")
        for _ in range(10001):
            c.add_member()
        assert c.is_popular()

    def test_equality(self) -> None:
        """Равные по имени."""
        a: Community = Community("X", "ivan")
        b: Community = Community("X", "petr")
        assert a == b
        assert a != "not community"

    def test_hash(self) -> None:
        """Хеш сообщества."""
        a: Community = Community("X", "ivan")
        b: Community = Community("X", "petr")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        c: Community = Community("X", "ivan", "описание")
        text: str = str(c)
        assert "X" in text
        assert "ivan" in text

    def test_parse(self) -> None:
        """from_string разбирает сообщество."""
        c: Community = Community.from_string("X; ivan; описание")
        assert c.name == "X"
        assert c.owner == "ivan"
