"""
Фотография.

Module: social.domain.content.photo
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.exceptions.content_exceptions import InvalidPostError

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Photo(Readable, Writable):
    """Фотография.

    Attributes:
        _url: Ссылка.
        _width: Ширина в пикселях.
        _height: Высота в пикселях.
        _caption: Подпись.
    """

    def __init__(
        self,
        url: str,
        width: int,
        height: int,
        caption: str = "",
    ) -> None:
        """Создать фотографию.

        Args:
            url: Ссылка.
            width: Ширина.
            height: Высота.
            caption: Подпись.

        Raises:
            InvalidPostError: Если данные некорректны.
        """
        if not url:
            raise InvalidPostError("URL не может быть пустым")
        if width <= 0 or height <= 0:
            raise InvalidPostError("размеры должны быть положительными")
        self._url: str = url
        self._width: int = width
        self._height: int = height
        self._caption: str = caption

    @classmethod
    def _parse(cls, text: str) -> Photo:
        """Разобрать фото из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            url=parts[0],
            width=int(parts[1]),
            height=int(parts[2]),
            caption=parts[3] if len(parts) > 3 else "",
        )

    @property
    def url(self) -> str:
        """Ссылка.

        Returns:
            Строка.
        """
        return self._url

    @property
    def caption(self) -> str:
        """Подпись.

        Returns:
            Строка.
        """
        return self._caption

    def aspect_ratio(self) -> float:
        """Рассчитать соотношение сторон.

        Returns:
            Число.
        """
        return self._width / self._height

    def is_landscape(self) -> bool:
        """Проверить горизонтальную ориентацию.

        Returns:
            ``True``, если ширина больше высоты.
        """
        return self._width > self._height

    def __eq__(self, other: object) -> bool:
        """Сравнить два фото.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении URL.
        """
        if not isinstance(other, Photo):
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
            f"{self._url}; {self._width}; "
            f"{self._height}; {self._caption}"
        )
