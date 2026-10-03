"""
Программа машины Тьюринга.

Module: turing_machine.domain.program
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Self

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from turing_machine.domain.transition import Transition

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Program(Readable, Writable):
    """Упорядоченный набор правил машины Тьюринга.

    Порядок правил сохраняется в порядке добавления. Поиск правила
    выполняется линейно по списку.

    Attributes:
        _rules: Список правил программы.
    """

    # -----------------------------------------------------------------------
    # Constructors
    # -----------------------------------------------------------------------

    def __init__(self, rules: Iterable[Transition] = ()) -> None:
        """Создать программу из набора правил.

        Args:
            rules: Итерируемый объект с правилами.
        """
        self._rules: list[Transition] = list(rules)

    @classmethod
    def _parse(cls, text: str) -> Self:
        """Разобрать программу из многострочного текста.

        Args:
            text: Текст, по одному правилу на строку.

        Returns:
            Новый экземпляр :class:`Program`.

        Raises:
            ValueError: Если хотя бы одна строка не является правилом.
        """
        lines: list[str] = [
            line.strip() for line in text.splitlines() if line.strip()
        ]
        rules: list[Transition] = [
            Transition.from_string(line) for line in lines
        ]
        return cls(rules)

    # -----------------------------------------------------------------------
    # Properties
    # -----------------------------------------------------------------------

    @property
    def rules(self) -> tuple[Transition, ...]:
        """Правила программы в порядке добавления.

        Returns:
            Кортеж правил.
        """
        return tuple(self._rules)

    # -----------------------------------------------------------------------
    # Public methods
    # -----------------------------------------------------------------------

    def add_rule(self, rule: Transition) -> None:
        """Добавить правило в конец программы.

        Args:
            rule: Добавляемое правило.

        Returns:
            Ничего не возвращает.
        """
        self._rules.append(rule)

    def remove_rule(self, index: int) -> None:
        """Удалить правило по индексу.

        Args:
            index: Индекс правила в программе.

        Returns:
            Ничего не возвращает.

        Raises:
            IndexError: Если индекс вне диапазона.
        """
        del self._rules[index]

    def find(self, state: str, symbol: str) -> Transition | None:
        """Найти первое правило, применимое к паре (состояние, символ).

        Args:
            state: Текущее состояние машины.
            symbol: Символ, прочитанный с ленты.

        Returns:
            Найденное правило или ``None``, если ничего не подошло.
        """
        for rule in self._rules:
            if rule.matches(state, symbol):
                return rule
        return None

    # -----------------------------------------------------------------------
    # Magic methods
    # -----------------------------------------------------------------------

    def __iter__(self) -> Iterator[Transition]:
        """Итерироваться по правилам программы.

        Returns:
            Итератор по правилам.
        """
        return iter(self._rules)

    def __len__(self) -> int:
        """Вернуть число правил в программе.

        Returns:
            Количество правил.
        """
        return len(self._rules)

    def __eq__(self, other: object) -> bool:
        """Сравнить две программы на равенство.

        Args:
            other: Другой объект для сравнения.

        Returns:
            ``True``, если списки правил совпадают.
        """
        if not isinstance(other, Program):
            return NotImplemented
        return self._rules == other._rules

    def __hash__(self) -> int:
        """Вернуть хеш программы.

        Returns:
            Целое число — хеш кортежа правил.
        """
        return hash(tuple(self._rules))

    def __str__(self) -> str:
        """Вернуть текстовое представление программы.

        Returns:
            Строка с правилами, по одному на строку.
        """
        return "\n".join(str(rule) for rule in self._rules)
