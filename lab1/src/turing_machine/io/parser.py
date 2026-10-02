"""
Загрузка и сохранение машины Тьюринга в файл.

Module: turing_machine.io.parser
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from pathlib import Path

from turing_machine.domain.machine import TuringMachine


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

ENCODING: str = "utf-8"
"""Кодировка файлов с описанием машины."""


# ---------------------------------------------------------------------------
# Public functions
# ---------------------------------------------------------------------------

def load_machine(path: Path) -> TuringMachine:
    """Загрузить машину Тьюринга из файла.

    Args:
        path: Путь к файлу с JSON-описанием машины.

    Returns:
        Машина, восстановленная из файла.

    Raises:
        FileNotFoundError: Если файл не существует.
        ValueError: Если содержимое файла не является корректным
            описанием машины.
    """
    with path.open(encoding=ENCODING) as stream:
        return TuringMachine.from_stream(stream)


def save_machine(machine: TuringMachine, path: Path) -> None:
    """Сохранить машину Тьюринга в файл.

    Args:
        machine: Машина для сохранения.
        path: Путь к файлу.

    Returns:
        Ничего не возвращает.
    """
    with path.open("w", encoding=ENCODING) as stream:
        machine.to_stream(stream)
