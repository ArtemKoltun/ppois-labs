"""
Тесты класса Session.

Module: tests.social.domain.technical.test_session
"""

from __future__ import annotations

from social.domain.technical.device import Device
from social.domain.technical.session import Session


class TestSession:
    """Проверки класса Session."""

    def test_creates(self) -> None:
        """Сессия создаётся."""
        d: Device = Device("ivan", "mobile", "Android")
        s: Session = Session("ivan", d, "token123")
        assert s.user == "ivan"
        assert s.token == "token123"
        assert s.is_active()

    def test_terminate_reactivate(self) -> None:
        """Завершение и возобновление."""
        d: Device = Device("ivan", "mobile", "Android")
        s: Session = Session("ivan", d, "token123")
        s.terminate()
        assert not s.is_active()
        s.reactivate()
        assert s.is_active()

    def test_belongs_to(self) -> None:
        """belongs_to проверяет владельца."""
        d: Device = Device("ivan", "mobile", "Android")
        s: Session = Session("ivan", d, "token123")
        assert s.belongs_to("ivan")
        assert not s.belongs_to("petr")

    def test_equality(self) -> None:
        """Равные по токену."""
        d: Device = Device("ivan", "mobile", "Android")
        a: Session = Session("ivan", d, "token123")
        b: Session = Session("petr", d, "token123")
        assert a == b
        assert a != "not session"

    def test_hash(self) -> None:
        """Хеш сессии."""
        d: Device = Device("ivan", "mobile", "Android")
        a: Session = Session("ivan", d, "token123")
        b: Session = Session("ivan", d, "token123")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        d: Device = Device("ivan", "mobile", "Android")
        s: Session = Session("ivan", d, "token123")
        text: str = str(s)
        assert "ivan" in text
        assert "token123" in text

    def test_parse(self) -> None:
        """from_string разбирает сессию."""
        s: Session = Session.from_string("ivan; token123; mobile; Android")
        assert s.user == "ivan"
        assert s.token == "token123"
