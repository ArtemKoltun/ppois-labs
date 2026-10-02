"""
Меню машины Тьюринга.

Module: turing_machine.ui.menu
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.enums.menu_result import MenuResult
from common.ui.menu import Menu
from common.ui.menu import MenuItem
from common.ui.prompts import ask_str
from turing_machine.domain.direction import Direction
from turing_machine.domain.machine import TuringMachine
from turing_machine.domain.transition import Transition


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_MAX_RULES_DISPLAYED: int = 20
"""Максимум правил, отображаемых в списке."""

_LOG_ENABLED: bool = True
"""Флаг включения пошагового лога при выполнении."""


# ---------------------------------------------------------------------------
# Public functions
# ---------------------------------------------------------------------------

def build_menu(
    machine: TuringMachine,
    log: bool = False,
) -> Menu:
    """Собрать меню для машины Тьюринга.

    Args:
        machine: Машина, с которой работает меню.
        log: Печатать состояние после каждого шага.

    Returns:
        Готовое меню.
    """
    def action_show() -> None:
        _print_state(machine)

    def action_step() -> None:
        moved: bool = machine.step()
        if not moved:
            print("Машина остановлена.")
        _print_state(machine)

    def action_run() -> None:
        _run_to_halt(machine, log)

    def action_add_rule() -> None:
        _add_rule(machine)

    def action_remove_rule() -> None:
        _remove_rule(machine)

    def action_show_rules() -> None:
        _print_rules(machine)

    def action_write_cell() -> None:
        _write_cell(machine)

    def action_reset() -> None:
        machine.reset()
        print("Машина сброшена.")
        _print_state(machine)

    items: list[MenuItem] = [
        MenuItem("Показать состояние", action_show),
        MenuItem("Выполнить один шаг", action_step),
        MenuItem("Выполнить до остановки", action_run),
        MenuItem("Показать правила", action_show_rules),
        MenuItem("Добавить правило", action_add_rule),
        MenuItem("Удалить правило", action_remove_rule),
        MenuItem("Записать символ на ленту", action_write_cell),
        MenuItem("Сбросить машину", action_reset),
    ]
    return Menu("Машина Тьюринга", items)


# ---------------------------------------------------------------------------
# Private functions
# ---------------------------------------------------------------------------

def _run_to_halt(machine: TuringMachine, log: bool) -> None:
    """Выполнить машину до остановки с опциональным логом.

    Args:
        machine: Машина.
        log: Печатать состояние после каждого шага.

    Returns:
        Ничего не возвращает.
    """
    hook = (
        (lambda m: _print_state(m, prefix="  "))
        if log else None
    )
    try:
        machine.run(on_step=hook)
        print("Машина остановлена.")
    except Exception as exc:  # noqa: BLE001
        print(f"Ошибка выполнения: {exc}")
    _print_state(machine)


def _print_state(
    machine: TuringMachine,
    prefix: str = "",
) -> None:
    """Напечатать текущее состояние машины.

    Args:
        machine: Машина.
        prefix: Префикс каждой строки.

    Returns:
        Ничего не возвращает.
    """
    print(f"{prefix}Статус:  {machine.status}")
    print(f"{prefix}Состояние: {machine.state}")
    print(f"{prefix}Шагов:   {machine.steps}")
    print(f"{prefix}Каретка: {machine.head.position}")
    print(f"{prefix}Лента:   {machine.tape}")


def _print_rules(machine: TuringMachine) -> None:
    """Напечатать правила программы машины.

    Args:
        machine: Машина.

    Returns:
        Ничего не возвращает.
    """
    rules = machine.program.rules
    if not rules:
        print("Правил нет.")
        return
    limit: int = min(len(rules), _MAX_RULES_DISPLAYED)
    for index in range(limit):
        print(f"  {index}: {rules[index]}")
    if len(rules) > limit:
        print(f"  ... ещё {len(rules) - limit}")


def _add_rule(machine: TuringMachine) -> None:
    """Запросить у пользователя правило и добавить его.

    Args:
        machine: Машина.

    Returns:
        Ничего не возвращает.
    """
    current: str = ask_str("Текущее состояние: ")
    read: str = ask_str("Читаемый символ: ")
    next_state: str = ask_str("Следующее состояние: ")
    write: str = ask_str("Записываемый символ: ")
    direction_raw: str = ask_str("Направление [L/R/S]: ")
    try:
        rule: Transition = Transition(
            current_state=current,
            read_symbol=read,
            next_state=next_state,
            write_symbol=write,
            direction=Direction.from_char(direction_raw),
        )
    except ValueError as exc:
        print(f"Некорректное правило: {exc}")
        return
    machine.program.add_rule(rule)
    print("Правило добавлено.")


def _remove_rule(machine: TuringMachine) -> None:
    """Запросить индекс и удалить правило.

    Args:
        machine: Машина.

    Returns:
        Ничего не возвращает.
    """
    rules = machine.program.rules
    if not rules:
        print("Правил нет.")
        return
    _print_rules(machine)
    raw: str = ask_str("Номер правила: ")
    try:
        index: int = int(raw)
        machine.program.remove_rule(index)
    except (ValueError, IndexError) as exc:
        print(f"Не удалось удалить: {exc}")
        return
    print("Правило удалено.")


def _write_cell(machine: TuringMachine) -> None:
    """Записать символ в указанную позицию ленты.

    Args:
        machine: Машина.

    Returns:
        Ничего не возвращает.
    """
    position_raw: str = ask_str("Позиция: ")
    symbol: str = ask_str("Символ: ")
    try:
        position: int = int(position_raw)
        machine.tape.write(position, symbol)
    except ValueError as exc:
        print(f"Не удалось записать: {exc}")
        return
    print("Записано.")
    _print_state(machine)
