"""
Видеозапись.

Module: social.domain.content.video
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

class Video(Readable, Writable):
    """Видеозапись.

    Attributes:
        _url: Ссылка.
        _duration_seconds: Длительность.
        _title: Заголовок.
        _views_count: Число просмотров.
        _is_short: Короткое ли видео.
    """

    def __init__(
        self,
        url: str,
        duration_seconds: int,
        title: str = "",
    ) -> None:
        """Создать видео.

        Args:
            url: Ссылка.
            duration_seconds: Длительность.
            title: Заголовок.

        Raises:
            InvalidPostError: Если данные некорректны.
        """
        if not url:
            raise InvalidPostError("URL не может быть пустым")
        if duration_seconds <= 0:
            raise InvalidPostError(
                "длительность должна быть положительной"
            )
        self._url: str = url
        self._duration_seconds: int = duration_seconds
        self._title: str = title
        self._views_count: int = 0
        self._is_short: bool = duration_seconds <= 60

    @classmethod
    def _parse(cls, text: str) -> Video:
        """Разобрать видео из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            url=parts[0],
            duration_seconds=int(parts[1]),
            title=parts[2] if len(parts) > 2 else "",
        )

    @property
    def url(self) -> str:
        """Ссылка.

        Returns:
            Строка.
        """
        return self._url

    @property
    def duration_seconds(self) -> int:
        """Длительность.

        Returns:
            Секунды.
        """
        return self._duration_seconds

    @property
    def views_count(self) -> int:
        """Число просмотров.

        Returns:
            Целое число.
        """
        return self._views_count

    def watch(self) -> None:
        """Увеличить счётчик просмотров.

        Returns:
            Ничего не возвращает.
        """
        self._views_count += 1

    def duration_minutes(self) -> float:
        """Длительность в минутах.

        Returns:
            Число.
        """
        return self._duration_seconds / 60

    def is_short(self) -> bool:
        """Проверить, короткое ли видео.

        Returns:
            ``True``, если длительность до 60 секунд.
        """
        return self._is_short

    def __eq__(self, other: object) -> bool:
        """Сравнить два видео.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении URL.
        """
        if not isinstance(other, Video):
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
        return f"{self._url}; {self._duration_seconds}; {self._title}"
