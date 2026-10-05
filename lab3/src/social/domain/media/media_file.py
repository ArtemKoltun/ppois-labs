"""
Медиафайл.

Module: social.domain.media.media_file
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.constants import DEFAULT_MAX_FILE_SIZE_MB
from common.exceptions.content_exceptions import InvalidPostError

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class MediaFile(Readable, Writable):
    """Медиафайл — фото, видео, аудио.

    Attributes:
        _filename: Имя файла.
        _url: Ссылка.
        _size_mb: Размер.
        _media_type: Тип.
        _owner: Владелец.
    """

    def __init__(
        self,
        filename: str,
        url: str,
        size_mb: float,
        media_type: str = "photo",
        owner: str = "",
    ) -> None:
        """Создать медиафайл.

        Args:
            filename: Имя.
            url: Ссылка.
            size_mb: Размер.
            media_type: Тип.
            owner: Владелец.

        Raises:
            InvalidPostError: Если данные некорректны.
        """
        if not filename or not url:
            raise InvalidPostError(
                "имя и ссылка не могут быть пустыми"
            )
        if size_mb <= 0 or size_mb > DEFAULT_MAX_FILE_SIZE_MB:
            raise InvalidPostError(
                f"размер должен быть от 0 до "
                f"{DEFAULT_MAX_FILE_SIZE_MB} МБ"
            )
        self._filename: str = filename
        self._url: str = url
        self._size_mb: float = size_mb
        self._media_type: str = media_type
        self._owner: str = owner

    @classmethod
    def _parse(cls, text: str) -> MediaFile:
        """Разобрать медиафайл из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            filename=parts[0],
            url=parts[1],
            size_mb=float(parts[2]),
            media_type=parts[3] if len(parts) > 3 else "photo",
            owner=parts[4] if len(parts) > 4 else "",
        )

    @property
    def filename(self) -> str:
        """Имя файла.

        Returns:
            Строка.
        """
        return self._filename

    @property
    def url(self) -> str:
        """Ссылка.

        Returns:
            Строка.
        """
        return self._url

    @property
    def size_mb(self) -> float:
        """Размер.

        Returns:
            Мегабайты.
        """
        return self._size_mb

    @property
    def media_type(self) -> str:
        """Тип медиа.

        Returns:
            Строка.
        """
        return self._media_type

    @property
    def owner(self) -> str:
        """Владелец.

        Returns:
            Строка.
        """
        return self._owner

    def is_image(self) -> bool:
        """Проверить тип.

        Returns:
            ``True``, если фото.
        """
        return self._media_type == "photo"

    def is_video(self) -> bool:
        """Проверить тип.

        Returns:
            ``True``, если видео.
        """
        return self._media_type == "video"

    def is_large(self) -> bool:
        """Проверить размер.

        Returns:
            ``True``, если больше 10 МБ.
        """
        return self._size_mb > 10.0

    def transfer_to(self, new_owner: str) -> None:
        """Передать владение.

        Args:
            new_owner: Новый владелец.

        Returns:
            Ничего не возвращает.
        """
        self._owner = new_owner

    def __eq__(self, other: object) -> bool:
        """Сравнить два файла.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении URL.
        """
        if not isinstance(other, MediaFile):
            return NotImplemented
        return self._url == other._url

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._url)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._filename}; {self._url}; "
            f"{self._size_mb}; {self._media_type}; {self._owner}"
        )
