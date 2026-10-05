"""
Тесты класса Photo.

Module: tests.social.domain.content.test_photo
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.exceptions import InvalidPostError
from social.domain.content.photo import Photo

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestPhoto:
    """Проверки класса Photo."""

    def test_creates(self) -> None:
        """Фото создаётся."""
        p: Photo = Photo("https://x.jpg", 1920, 1080)
        assert p.url == "https://x.jpg"
        assert p.caption == ""

    def test_empty_url_raises(self) -> None:
        """Пустой URL недопустим."""
        with pytest.raises(InvalidPostError):
            Photo("", 100, 100)

    def test_zero_size_raises(self) -> None:
        """Нулевые размеры недопустимы."""
        with pytest.raises(InvalidPostError):
            Photo("https://x.jpg", 0, 100)

    def test_aspect_ratio(self) -> None:
        """aspect_ratio считает."""
        p: Photo = Photo("https://x.jpg", 1920, 1080)
        assert round(p.aspect_ratio(), 2) == 1.78

    def test_is_landscape(self) -> None:
        """is_landscape для горизонтали."""
        landscape: Photo = Photo("https://l.jpg", 1920, 1080)
        portrait: Photo = Photo("https://p.jpg", 1080, 1920)
        assert landscape.is_landscape()
        assert not portrait.is_landscape()

    def test_equality(self) -> None:
        """Равные по URL."""
        a: Photo = Photo("https://x.jpg", 100, 100)
        b: Photo = Photo("https://x.jpg", 200, 200)
        assert a == b
        assert a != "not photo"

    def test_hash(self) -> None:
        """Хеш по URL."""
        a: Photo = Photo("https://x.jpg", 100, 100)
        b: Photo = Photo("https://x.jpg", 200, 200)
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        p: Photo = Photo("https://x.jpg", 100, 100, "Подпись")
        text: str = str(p)
        assert "https://x.jpg" in text
        assert "Подпись" in text

    def test_parse(self) -> None:
        """from_string разбирает фото."""
        p: Photo = Photo.from_string("https://x.jpg; 800; 600; Подпись")
        assert p.url == "https://x.jpg"
        assert p.caption == "Подпись"
