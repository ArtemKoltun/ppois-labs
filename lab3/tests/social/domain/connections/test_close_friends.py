"""
Тесты класса CloseFriends.

Module: tests.social.domain.connections.test_close_friends
"""

from __future__ import annotations

from social.domain.connections.close_friends import CloseFriends


class TestCloseFriends:
    """Проверки класса CloseFriends."""

    def test_creates(self) -> None:
        """Список создаётся."""
        cf: CloseFriends = CloseFriends("ivan")
        assert cf.owner == "ivan"
        assert cf.size() == 0

    def test_add(self) -> None:
        """add добавляет."""
        cf: CloseFriends = CloseFriends("ivan")
        assert cf.add("petr")
        assert cf.size() == 1

    def test_add_duplicate_returns_false(self) -> None:
        """Повторное добавление — False."""
        cf: CloseFriends = CloseFriends("ivan")
        cf.add("petr")
        assert not cf.add("petr")

    def test_add_over_limit_returns_false(self) -> None:
        """Превышение — False."""
        cf: CloseFriends = CloseFriends("ivan", max_size=1)
        cf.add("petr")
        assert not cf.add("anna")

    def test_remove(self) -> None:
        """remove удаляет."""
        cf: CloseFriends = CloseFriends("ivan")
        cf.add("petr")
        cf.remove("petr")
        assert cf.size() == 0

    def test_remove_missing(self) -> None:
        """Удаление отсутствующего не падает."""
        cf: CloseFriends = CloseFriends("ivan")
        cf.remove("nobody")

    def test_contains(self) -> None:
        """contains проверяет."""
        cf: CloseFriends = CloseFriends("ivan")
        cf.add("petr")
        assert cf.contains("petr")

    def test_is_full(self) -> None:
        """is_full при заполнении."""
        cf: CloseFriends = CloseFriends("ivan", max_size=1)
        assert not cf.is_full()
        cf.add("petr")
        assert cf.is_full()

    def test_equality(self) -> None:
        """Равные по владельцу."""
        a: CloseFriends = CloseFriends("ivan")
        b: CloseFriends = CloseFriends("ivan")
        assert a == b
        assert a != "not cf"

    def test_hash(self) -> None:
        """Хеш списка."""
        a: CloseFriends = CloseFriends("ivan")
        b: CloseFriends = CloseFriends("ivan")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает владельца."""
        cf: CloseFriends = CloseFriends("ivan")
        assert "ivan" in str(cf)

    def test_parse(self) -> None:
        """from_string разбирает список."""
        cf: CloseFriends = CloseFriends.from_string("ivan; 50")
        assert cf._max_size == 50
