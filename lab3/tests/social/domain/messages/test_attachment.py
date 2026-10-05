"""
Тесты класса Attachment.

Module: tests.social.domain.messages.test_attachment
"""

from __future__ import annotations

import pytest

from common.exceptions import MessageDeliveryError
from social.domain.messages.attachment import Attachment


class TestAttachment:
    """Проверки класса Attachment."""

    def test_creates(self) -> None:
        """Вложение создаётся."""
        a: Attachment = Attachment("file.pdf", "https://x", 5.0)
        assert a.filename == "file.pdf"
        assert a.size_mb == 5.0
        assert a.file_type == "file"

    def test_empty_filename_raises(self) -> None:
        """Пустое имя недопустимо."""
        with pytest.raises(MessageDeliveryError):
            Attachment("", "https://x", 5.0)

    def test_zero_size_raises(self) -> None:
        """Нулевой размер недопустим."""
        with pytest.raises(MessageDeliveryError):
            Attachment("f", "https://x", 0.0)

    def test_too_large_raises(self) -> None:
        """Превышение лимита недопустимо."""
        with pytest.raises(MessageDeliveryError):
            Attachment("f", "https://x", 100.0)

    def test_is_image(self) -> None:
        """is_image для типа image."""
        a: Attachment = Attachment("p.jpg", "https://x", 5.0, "image")
        b: Attachment = Attachment("f.pdf", "https://x", 5.0)
        assert a.is_image()
        assert not b.is_image()

    def test_is_large(self) -> None:
        """is_large при >10 МБ."""
        a: Attachment = Attachment("f", "https://x", 15.0)
        b: Attachment = Attachment("f", "https://x", 5.0)
        assert a.is_large()
        assert not b.is_large()

    def test_extension(self) -> None:
        """extension извлекает расширение."""
        a: Attachment = Attachment("file.pdf", "https://x", 5.0)
        b: Attachment = Attachment("noext", "https://x", 5.0)
        assert a.extension() == "pdf"
        assert b.extension() == ""

    def test_equality(self) -> None:
        """Равные по URL."""
        a: Attachment = Attachment("a", "https://x", 5.0)
        b: Attachment = Attachment("b", "https://x", 3.0)
        assert a == b
        assert a != "not attachment"

    def test_hash(self) -> None:
        """Хеш по URL."""
        a: Attachment = Attachment("a", "https://x", 5.0)
        b: Attachment = Attachment("b", "https://x", 3.0)
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        a: Attachment = Attachment("f.pdf", "https://x", 5.0)
        assert "f.pdf" in str(a)

    def test_parse(self) -> None:
        """from_string разбирает вложение."""
        a: Attachment = Attachment.from_string("f.pdf; https://x; 5.0; file")
        assert a.filename == "f.pdf"
        assert a.size_mb == 5.0
