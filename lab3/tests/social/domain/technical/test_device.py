"""
Тесты класса Device.

Module: tests.social.domain.technical.test_device
"""

from __future__ import annotations

from social.domain.technical.device import Device


class TestDevice:
    """Проверки класса Device."""

    def test_creates(self) -> None:
        """Устройство создаётся."""
        d: Device = Device("ivan", "mobile", "Android")
        assert d.user == "ivan"
        assert d.device_type == "mobile"
        assert not d.is_trusted()

    def test_trust_untrust(self) -> None:
        """Доверие и снятие."""
        d: Device = Device("ivan", "mobile", "Android")
        d.trust()
        assert d.is_trusted()
        d.untrust()
        assert not d.is_trusted()

    def test_is_mobile(self) -> None:
        """is_mobile для mobile и tablet."""
        m: Device = Device("ivan", "mobile", "Android")
        t: Device = Device("ivan", "tablet", "iOS")
        d: Device = Device("ivan", "desktop", "Linux")
        assert m.is_mobile()
        assert t.is_mobile()
        assert not d.is_mobile()

    def test_equality(self) -> None:
        """Равные по (user, type)."""
        a: Device = Device("ivan", "mobile", "A")
        b: Device = Device("ivan", "mobile", "B")
        assert a == b
        assert a != "not device"

    def test_hash(self) -> None:
        """Хеш устройства."""
        a: Device = Device("ivan", "mobile", "A")
        b: Device = Device("ivan", "mobile", "B")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        d: Device = Device("ivan", "mobile", "Android")
        text: str = str(d)
        assert "ivan" in text
        assert "Android" in text

    def test_parse(self) -> None:
        """from_string разбирает устройство."""
        d: Device = Device.from_string("ivan; mobile; Android")
        assert d.user == "ivan"
        assert d.device_type == "mobile"
