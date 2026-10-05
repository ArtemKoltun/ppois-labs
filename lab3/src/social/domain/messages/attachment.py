"""
Вложение в сообщении.

Module: social.domain.messages.attachment
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.constants import DEFAULT_MAX_FILE_SIZE_MB
from common.exceptions.connection_exceptions import MessageDeliveryError

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Attachment(Readable, Writable):
    """Вложение в сообщении.

    Attributes:
        _filename: Имя файла.
        _url: Ссылка.
        _size_mb: Размер в МБ.
        _file_type: Тип файла.
    """

    def __init__(
        self,
        filename: str,
        url: str,
        size_mb: float,
        file_type: str = "file",
    ) -> None:
        """Создать вложение.

        Args:
            filename: Имя файла.
            url: Ссылка.
            size_mb: Размер.
            file_type: Тип.

        Raises:
            MessageDeliveryError: Если данные некорректны.
        """
        if not filename or not url:
            raise MessageDeliveryError(
                "имя и ссылка не могут быть пустыми"
            )
        if size_mb <= 0:
            raise MessageDeliveryError(
                "размер должен быть положительным"
            )
        if size_mb > DEFAULT_MAX_FILE_SIZE_MB:
            raise MessageDeliveryError(
                f"файл слишком большой: {size_mb} МБ "
                f"(максимум {DEFAULT_MAX_FILE_SIZE_MB})"
            )
        self._filename: str = filename
        self._url: str = url
        self._size_mb: float = size_mb
        self._file_type: str = file_type

    @classmethod
    def _parse(cls, text: str) -> Attachment:
        """Разобрать вложение из строки.

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
            file_type=parts[3] if len(parts) > 3 else "file",
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
    def file_type(self) -> str:
        """Тип файла.

        Returns:
            Строка.
        """
        return self._file_type

    def is_image(self) -> bool:
        """Проверить, что это изображение.

        Returns:
            ``True``, если тип image.
        """
        return self._file_type == "image"

    def is_large(self) -> bool:
        """Проверить размер.

        Returns:
            ``True``, если больше 10 МБ.
        """
        return self._size_mb > 10.0

    def extension(self) -> str:
        """Извлечь расширение.

        Returns:
            Строка или пустая строка.
        """
        if "." in self._filename:
            return self._filename.rsplit(".", 1)[1]
        return ""

    def __eq__(self, other: object) -> bool:
        """Сравнить два вложения.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении URL.
        """
        if not isinstance(other, Attachment):
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
            f"{self._size_mb}; {self._file_type}"
        )
