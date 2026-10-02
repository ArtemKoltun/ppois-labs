"""
Загрузка и сохранение нормального алгорифма Маркова в файл.

Module: markov_algorithms.io.parser
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from pathlib import Path

from markov_algorithms.domain.algorithm import MarkovAlgorithm


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

ENCODING: str = "utf-8"
"""Кодировка файлов с описанием алгорифма."""


# ---------------------------------------------------------------------------
# Public functions
# ---------------------------------------------------------------------------

def load_algorithm(path: Path) -> MarkovAlgorithm:
    """Загрузить нормальный алгорифм Маркова из файла.

    Args:
        path: Путь к файлу с JSON-описанием алгорифма.

    Returns:
        Алгорифм, восстановленный из файла.

    Raises:
        FileNotFoundError: Если файл не существует.
        ValueError: Если содержимое файла не является корректным
            описанием алгорифма.
    """
    with path.open(encoding=ENCODING) as stream:
        return MarkovAlgorithm.from_stream(stream)


def save_algorithm(
    algorithm: MarkovAlgorithm,
    path: Path,
) -> None:
    """Сохранить нормальный алгорифм Маркова в файл.

    Args:
        algorithm: Алгорифм для сохранения.
        path: Путь к файлу.

    Returns:
        Ничего не возвращает.
    """
    with path.open("w", encoding=ENCODING) as stream:
        algorithm.to_stream(stream)
