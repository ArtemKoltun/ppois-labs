"""
Альбом с медиафайлами.

Module: social.domain.media.album
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from social.domain.media.media_file import MediaFile

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Album(Readable, Writable):
    """Альбом пользователя.

    Attributes:
        _title: Название.
        _owner: Владелец.
        _files: Список файлов.
        _is_public: Публичный ли.
    """

    def __init__(
        self,
        title: str,
        owner: str,
        is_public: bool = True,
    ) -> None:
        """Создать альбом.

        Args:
            title: Название.
            owner: Владелец.
            is_public: Публичность.
        """
        self._title: str = title
        self._owner: str = owner
        self._files: list[MediaFile] = []
        self._is_public: bool = is_public

    @classmethod
    def _parse(cls, text: str) -> Album:
        """Разобрать альбом из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            title=parts[0],
            owner=parts[1],
            is_public=parts[2].lower() == "true",
        )

    @property
    def title(self) -> str:
        """Название.

        Returns:
            Строка.
        """
        return self._title

    @property
    def owner(self) -> str:
        """Владелец.

        Returns:
            Строка.
        """
        return self._owner

    @property
    def is_public(self) -> bool:
        """Публичность.

        Returns:
            ``True``, если публичный.
        """
        return self._is_public

    def add_file(self, media: MediaFile) -> None:
        """Добавить файл.

        Args:
            media: Медиафайл.

        Returns:
            Ничего не возвращает.
        """
        self._files.append(media)

    def remove_file(self, media: MediaFile) -> None:
        """Убрать файл.

        Args:
            media: Медиафайл.

        Returns:
            Ничего не возвращает.
        """
        if media in self._files:
            self._files.remove(media)

    def files_count(self) -> int:
        """Число файлов.

        Returns:
            Целое число.
        """
        return len(self._files)

    def total_size_mb(self) -> float:
        """Суммарный размер.

        Returns:
            Мегабайты.
        """
        return sum(f.size_mb for f in self._files)

    def make_private(self) -> None:
        """Сделать приватным.

        Returns:
            Ничего не возвращает.
        """
        self._is_public = False

    def __eq__(self, other: object) -> bool:
        """Сравнить два альбома.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении названия и владельца.
        """
        if not isinstance(other, Album):
            return NotImplemented
        return (
            self._title == other._title
            and self._owner == other._owner
        )

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash((self._title, self._owner))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return f"{self._title}; {self._owner}; {self._is_public}"
