"""
Загрузка и сохранение доменных объектов.

Module: social.io.parser
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from pathlib import Path

from common.abstract.readable import Readable

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

ENCODING: str = "utf-8"
"""Кодировка файлов."""


# ---------------------------------------------------------------------------
# Public functions
# ---------------------------------------------------------------------------

def load_object[T: Readable](cls: type[T], path: Path) -> T:
    """Загрузить объект из файла.

    Args:
        cls: Класс объекта.
        path: Путь к файлу.

    Returns:
        Восстановленный объект.
    """
    with path.open(encoding=ENCODING) as stream:
        return cls.from_stream(stream)


def save_object(obj: Readable, path: Path) -> None:
    """Сохранить объект в файл.

    Args:
        obj: Объект.
        path: Путь к файлу.

    Returns:
        Ничего не возвращает.
    """
    with path.open("w", encoding=ENCODING) as stream:
        stream.write(str(obj))
