"""
Тесты класса Album.

Module: tests.social.domain.media.test_album
"""

from __future__ import annotations

from social.domain.media.album import Album
from social.domain.media.media_file import MediaFile


class TestAlbum:
    """Проверки класса Album."""

    def test_creates(self) -> None:
        """Альбом создаётся."""
        a: Album = Album("Лето", "ivan")
        assert a.title == "Лето"
        assert a.owner == "ivan"
        assert a.is_public
        assert a.files_count() == 0

    def test_add_remove_file(self) -> None:
        """Добавление и удаление файлов."""
        a: Album = Album("X", "ivan")
        m: MediaFile = MediaFile("a.jpg", "https://x", 5.0)
        a.add_file(m)
        assert a.files_count() == 1
        a.remove_file(m)
        assert a.files_count() == 0

    def test_remove_missing_file(self) -> None:
        """Удаление отсутствующего не падает."""
        a: Album = Album("X", "ivan")
        m: MediaFile = MediaFile("a.jpg", "https://x", 5.0)
        a.remove_file(m)

    def test_total_size_mb(self) -> None:
        """total_size_mb считает сумму."""
        a: Album = Album("X", "ivan")
        a.add_file(MediaFile("a", "https://x", 5.0))
        a.add_file(MediaFile("b", "https://y", 3.5))
        assert a.total_size_mb() == 8.5

    def test_make_private(self) -> None:
        """make_private меняет публичность."""
        a: Album = Album("X", "ivan")
        a.make_private()
        assert not a.is_public

    def test_equality(self) -> None:
        """Равные по title и owner."""
        a: Album = Album("X", "ivan")
        b: Album = Album("X", "ivan")
        assert a == b
        assert a != "not album"

    def test_hash(self) -> None:
        """Хеш альбома."""
        a: Album = Album("X", "ivan")
        b: Album = Album("X", "ivan")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        a: Album = Album("X", "ivan")
        text: str = str(a)
        assert "X" in text
        assert "ivan" in text

    def test_parse(self) -> None:
        """from_string разбирает альбом."""
        a: Album = Album.from_string("X; ivan; false")
        assert a.title == "X"
        assert not a.is_public
