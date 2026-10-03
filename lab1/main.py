"""
Точка входа лабораторной работы №1.

Module: main
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from common.enums.menu_result import MenuResult
from markov_algorithms.domain.algorithm import MarkovAlgorithm
from markov_algorithms.ui.menu import build_menu as build_markov_menu
from turing_machine.domain.machine import TuringMachine
from turing_machine.ui.menu import build_menu as build_turing_menu

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

ENCODING: str = "utf-8"
"""Кодировка входных файлов."""


# ---------------------------------------------------------------------------
# Public functions
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    """Запустить консольное меню для файла с описанием машины.

    Args:
        argv: Аргументы командной строки без имени программы.
            Если ``None`` — берутся из ``sys.argv``.

    Returns:
        Код возврата процесса.
    """
    args: argparse.Namespace = _parse_args(argv)
    path: Path = args.path
    if not path.exists():
        print(f"Файл не найден: {path}", file=sys.stderr)
        return 1
    try:
        text: str = path.read_text(encoding=ENCODING)
        kind: str = _detect_kind(text)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Ошибка чтения: {exc}", file=sys.stderr)
        return 1
    return _run_menu(kind, text, log=args.log)


# ---------------------------------------------------------------------------
# Private functions
# ---------------------------------------------------------------------------

def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    """Разобрать аргументы командной строки.

    Args:
        argv: Аргументы без имени программы.

    Returns:
        Пространство имён с полями ``path`` и ``log``.
    """
    parser = argparse.ArgumentParser(
        description=(
            "Интерпретатор машины Тьюринга и нормальных "
            "алгорифмов Маркова."
        ),
    )
    parser.add_argument(
        "path",
        type=Path,
        help="файл с описанием машины в формате JSON",
    )
    parser.add_argument(
        "-log",
        action="store_true",
        help="печатать состояние после каждого шага",
    )
    return parser.parse_args(argv)


def _detect_kind(text: str) -> str:
    """Определить тип машины по содержимому JSON.

    Args:
        text: Содержимое файла.

    Returns:
        ``"turing"`` или ``"markov"``.

    Raises:
        ValueError: Если тип не удалось определить.
    """
    data = json.loads(text)
    if "transitions" in data:
        return "turing"
    if "rules" in data:
        return "markov"
    raise ValueError(
        "не удалось определить тип машины: ожидался ключ "
        "'transitions' или 'rules'"
    )


def _run_menu(kind: str, text: str, log: bool) -> int:
    """Запустить меню нужной машины.

    Args:
        kind: Тип машины — ``"turing"`` или ``"markov"``.
        text: Содержимое файла.
        log: Печатать состояние после каждого шага.

    Returns:
        Код возврата процесса.
    """
    if kind == "turing":
        machine: TuringMachine = TuringMachine.from_string(text)
        menu = build_turing_menu(machine, log=log)
    else:
        algorithm: MarkovAlgorithm = MarkovAlgorithm.from_string(text)
        menu = build_markov_menu(algorithm, log=log)
    while True:
        result: MenuResult = menu.run()
        if result is MenuResult.BACK:
            return 0


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    sys.exit(main())
