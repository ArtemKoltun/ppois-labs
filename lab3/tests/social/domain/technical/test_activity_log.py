"""
Тесты класса ActivityLog.

Module: tests.social.domain.technical.test_activity_log
"""

from __future__ import annotations

from social.domain.technical.activity_log import ActivityLog


class TestActivityLog:
    """Проверки класса ActivityLog."""

    def test_creates(self) -> None:
        """Журнал создаётся."""
        log: ActivityLog = ActivityLog("ivan")
        assert log.user == "ivan"
        assert log.entries_count() == 0

    def test_record(self) -> None:
        """record добавляет."""
        log: ActivityLog = ActivityLog("ivan")
        log.record("вошёл в систему")
        log.record("опубликовал пост")
        assert log.entries_count() == 2

    def test_record_over_limit(self) -> None:
        """При превышении старые удаляются."""
        log: ActivityLog = ActivityLog("ivan", max_size=2)
        log.record("a")
        log.record("b")
        log.record("c")
        assert log.entries_count() == 2

    def test_last(self) -> None:
        """last возвращает последнюю."""
        log: ActivityLog = ActivityLog("ivan")
        log.record("first")
        log.record("last")
        assert log.last() == "last"

    def test_last_empty(self) -> None:
        """last на пустом журнале — пустая строка."""
        log: ActivityLog = ActivityLog("ivan")
        assert log.last() == ""

    def test_contains(self) -> None:
        """contains ищет ключевое слово."""
        log: ActivityLog = ActivityLog("ivan")
        log.record("вошёл в систему")
        assert log.contains("систему")
        assert not log.contains("выход")

    def test_clear(self) -> None:
        """clear очищает."""
        log: ActivityLog = ActivityLog("ivan")
        log.record("a")
        log.clear()
        assert log.entries_count() == 0

    def test_equality(self) -> None:
        """Равные по пользователю."""
        a: ActivityLog = ActivityLog("ivan")
        b: ActivityLog = ActivityLog("ivan")
        assert a == b
        assert a != "not log"

    def test_hash(self) -> None:
        """Хеш журнала."""
        a: ActivityLog = ActivityLog("ivan")
        b: ActivityLog = ActivityLog("ivan")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает пользователя."""
        log: ActivityLog = ActivityLog("ivan")
        assert "ivan" in str(log)

    def test_parse(self) -> None:
        """from_string разбирает журнал."""
        log: ActivityLog = ActivityLog.from_string("ivan; 500")
        assert log.user == "ivan"
        assert log._max_size == 500
