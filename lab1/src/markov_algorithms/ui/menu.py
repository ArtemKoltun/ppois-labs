"""
Меню нормального алгорифма Маркова.

Module: markov_algorithms.ui.menu
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.ui.menu import Menu
from common.ui.menu import MenuItem
from common.ui.prompts import ask_str
from markov_algorithms.domain.algorithm import MarkovAlgorithm
from markov_algorithms.domain.substitution import Substitution
from markov_algorithms.domain.word import Word


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_MAX_RULES_DISPLAYED: int = 20
"""Максимум правил, отображаемых в списке."""


# ---------------------------------------------------------------------------
# Public functions
# ---------------------------------------------------------------------------

def build_menu(
    algorithm: MarkovAlgorithm,
    log: bool = False,
) -> Menu:
    """Собрать меню для нормального алгорифма Маркова.

    Args:
        algorithm: Алгорифм, с которым работает меню.
        log: Печатать состояние после каждого шага.

    Returns:
        Готовое меню.
    """
    def action_show() -> None:
        _print_state(algorithm)

    def action_step() -> None:
        _step(algorithm)

    def action_run() -> None:
        _run_to_halt(algorithm, log)

    def action_add_rule() -> None:
        _add_rule(algorithm)

    def action_remove_rule() -> None:
        _remove_rule(algorithm)

    def action_show_rules() -> None:
        _print_rules(algorithm)

    def action_set_word() -> None:
        _set_word(algorithm)

    def action_reset() -> None:
        algorithm.reset()
        print("Алгорифм сброшен.")
        _print_state(algorithm)

    items: list[MenuItem] = [
        MenuItem("Показать состояние", action_show),
        MenuItem("Выполнить один шаг", action_step),
        MenuItem("Выполнить до остановки", action_run),
        MenuItem("Показать правила", action_show_rules),
        MenuItem("Добавить правило", action_add_rule),
        MenuItem("Удалить правило", action_remove_rule),
        MenuItem("Заменить слово", action_set_word),
        MenuItem("Сбросить алгорифм", action_reset),
    ]
    return Menu("Нормальные алгорифмы Маркова", items)


# ---------------------------------------------------------------------------
# Private functions
# ---------------------------------------------------------------------------

def _step(algorithm: MarkovAlgorithm) -> None:
    """Выполнить один шаг и напечатать состояние.

    Args:
        algorithm: Алгорифм.

    Returns:
        Ничего не возвращает.
    """
    moved: bool = algorithm.step()
    if not moved:
        print("Алгорифм остановлен.")
    _print_state(algorithm)


def _run_to_halt(
    algorithm: MarkovAlgorithm,
    log: bool,
) -> None:
    """Выполнить алгорифм до остановки с опциональным логом.

    Args:
        algorithm: Алгорифм.
        log: Печатать состояние после каждого шага.

    Returns:
        Ничего не возвращает.
    """
    hook = (
        (lambda a: _print_state(a, prefix="  "))
        if log else None
    )
    try:
        algorithm.run(on_step=hook)
        print("Алгорифм остановлен.")
    except Exception as exc:  # noqa: BLE001
        print(f"Ошибка выполнения: {exc}")
    _print_state(algorithm)


def _print_state(
    algorithm: MarkovAlgorithm,
    prefix: str = "",
) -> None:
    """Напечатать текущее состояние алгорифма.

    Args:
        algorithm: Алгорифм.
        prefix: Префикс каждой строки.

    Returns:
        Ничего не возвращает.
    """
    print(f"{prefix}Статус: {algorithm.status}")
    print(f"{prefix}Шагов:  {algorithm.steps}")
    print(f"{prefix}Слово:  {algorithm.word}")


def _print_rules(algorithm: MarkovAlgorithm) -> None:
    """Напечатать правила программы.

    Args:
        algorithm: Алгорифм.

    Returns:
        Ничего не возвращает.
    """
    rules = algorithm.program.rules
    if not rules:
        print("Правил нет.")
        return
    limit: int = min(len(rules), _MAX_RULES_DISPLAYED)
    for index in range(limit):
        print(f"  {index}: {rules[index]}")
    if len(rules) > limit:
        print(f"  ... ещё {len(rules) - limit}")


def _add_rule(algorithm: MarkovAlgorithm) -> None:
    """Запросить у пользователя правило и добавить его.

    Args:
        algorithm: Алгорифм.

    Returns:
        Ничего не возвращает.
    """
    line: str = ask_str("Правило (например 'ab -> ba'): ")
    try:
        rule: Substitution = Substitution.from_string(line)
    except ValueError as exc:
        print(f"Некорректное правило: {exc}")
        return
    algorithm.program.add_rule(rule)
    print("Правило добавлено.")


def _remove_rule(algorithm: MarkovAlgorithm) -> None:
    """Запросить индекс и удалить правило.

    Args:
        algorithm: Алгорифм.

    Returns:
        Ничего не возвращает.
    """
    rules = algorithm.program.rules
    if not rules:
        print("Правил нет.")
        return
    _print_rules(algorithm)
    raw: str = ask_str("Номер правила: ")
    try:
        index: int = int(raw)
        algorithm.program.remove_rule(index)
    except (ValueError, IndexError) as exc:
        print(f"Не удалось удалить: {exc}")
        return
    print("Правило удалено.")


def _set_word(algorithm: MarkovAlgorithm) -> None:
    """Заменить текущее слово алгорифма.

    Args:
        algorithm: Алгорифм.

    Returns:
        Ничего не возвращает.
    """
    raw: str = ask_str("Новое слово: ")
    algorithm.set_word(Word(raw))
    print("Слово заменено.")
    _print_state(algorithm)
