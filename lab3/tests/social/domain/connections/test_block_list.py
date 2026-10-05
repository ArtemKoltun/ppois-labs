"""
Тесты класса BlockList.

Module: tests.social.domain.connections.test_block_list
"""

from __future__ import annotations

from social.domain.connections.block_list import BlockList


class TestBlockList:
    """Проверки класса BlockList."""

    def test_creates(self) -> None:
        """Список создаётся."""
        bl: BlockList = BlockList("ivan")
        assert bl.owner == "ivan"
        assert bl.blocked_count() == 0

    def test_add_remove(self) -> None:
        """Добавление и удаление."""
        bl: BlockList = BlockList("ivan")
        bl.add("spammer")
        assert bl.blocked_count() == 1
        bl.remove("spammer")
        assert bl.blocked_count() == 0

    def test_add_twice_no_duplicate(self) -> None:
        """Повторное добавление не дублирует."""
        bl: BlockList = BlockList("ivan")
        bl.add("spammer")
        bl.add("spammer")
        assert bl.blocked_count() == 1

    def test_remove_missing(self) -> None:
        """Удаление отсутствующего не падает."""
        bl: BlockList = BlockList("ivan")
        bl.remove("x")

    def test_contains(self) -> None:
        """contains проверяет наличие."""
        bl: BlockList = BlockList("ivan")
        bl.add("spammer")
        assert bl.contains("spammer")
        assert not bl.contains("friend")

    def test_clear(self) -> None:
        """clear очищает."""
        bl: BlockList = BlockList("ivan")
        bl.add("a")
        bl.add("b")
        bl.clear()
        assert bl.blocked_count() == 0

    def test_equality(self) -> None:
        """Равные по владельцу."""
        a: BlockList = BlockList("ivan")
        b: BlockList = BlockList("ivan", "reason")
        assert a == b
        assert a != "not blocklist"

    def test_hash(self) -> None:
        """Хеш списка."""
        a: BlockList = BlockList("ivan")
        b: BlockList = BlockList("ivan")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает владельца."""
        bl: BlockList = BlockList("ivan", "причина")
        text: str = str(bl)
        assert "ivan" in text
        assert "причина" in text

    def test_parse(self) -> None:
        """from_string разбирает список."""
        bl: BlockList = BlockList.from_string("ivan; причина")
        assert bl.owner == "ivan"
