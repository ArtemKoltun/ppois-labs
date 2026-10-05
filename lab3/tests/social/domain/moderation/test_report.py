"""
Тесты класса Report.

Module: tests.social.domain.moderation.test_report
"""

from __future__ import annotations

import pytest

from common.enums.report_status import ReportStatus
from common.exceptions import ContentModerationError
from social.domain.moderation.report import Report


class TestReport:
    """Проверки класса Report."""

    def test_creates(self) -> None:
        """Жалоба создаётся."""
        r: Report = Report("ivan", "post1", "спам")
        assert r.author == "ivan"
        assert r.target == "post1"
        assert r.status is ReportStatus.PENDING
        assert r.is_pending()

    def test_empty_author_raises(self) -> None:
        """Пустой автор недопустим."""
        with pytest.raises(ContentModerationError):
            Report("", "p", "x")

    def test_empty_reason_raises(self) -> None:
        """Пустая причина недопустима."""
        with pytest.raises(ContentModerationError):
            Report("ivan", "p", "")

    def test_take_in_review(self) -> None:
        """take_in_review меняет статус."""
        r: Report = Report("ivan", "p", "x")
        r.take_in_review("admin")
        assert r.status is ReportStatus.IN_REVIEW
        assert r.has_reviewer()

    def test_resolve(self) -> None:
        """resolve рассмотрит."""
        r: Report = Report("ivan", "p", "x")
        r.resolve()
        assert r.status is ReportStatus.RESOLVED

    def test_reject(self) -> None:
        """reject отклоняет."""
        r: Report = Report("ivan", "p", "x")
        r.reject()
        assert r.status is ReportStatus.REJECTED

    def test_equality(self) -> None:
        """Равные по автору и цели."""
        a: Report = Report("ivan", "p1", "x")
        b: Report = Report("ivan", "p1", "y")
        assert a == b
        assert a != "not report"

    def test_hash(self) -> None:
        """Хеш жалобы."""
        a: Report = Report("ivan", "p1", "x")
        b: Report = Report("ivan", "p1", "y")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        r: Report = Report("ivan", "p1", "спам")
        text: str = str(r)
        assert "ivan" in text
        assert "спам" in text

    def test_parse(self) -> None:
        """from_string разбирает жалобу."""
        r: Report = Report.from_string("ivan; p1; спам")
        assert r.author == "ivan"
        assert r.target == "p1"
