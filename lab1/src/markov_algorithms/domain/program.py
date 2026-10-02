"""
Программа нормального алгорифма Маркова.

Module: markov_algorithms.domain.program
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from collections.abc import Iterable
from collections.abc import Iterator
from typing import Self

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from markov_algorithms.domain.substitution import Substitution


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_COMMENT_PREFIX: str = "#"
"""Префикс строки-комментария в текстовом представлении."""


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Program(Readable, Writable):
    """Упорядоченный набор правил подстановки.

    Порядок правил критичен: алгорифм всегда просматривает список
    сверху вниз и применяет первое подходящее правило.

    Attributes:
        _rules: Список правил программы.
    """

    # -----------------------------------------------------------------------
    # Constructors
    # -----------------------------------------------------------------------

    def __init__(self, rules: Iterable[Substitution] = ()) -> None:
        """Создать программу из набора правил.

        Args:
            rules: Итерируемый объект с правилами.
        """
        self._rules: list[Substitution] = list(rules)

    @classmethod
    def _parse(cls, text: str) -> Self:
        """Разобрать программу из многострочного текста.

        Пустые строки и строки, начинающиеся с ``#``, игнорируются.

        Args:
            text: Текст, по одному правилу на строку.

        Returns:
            Новый экземпляр :class:`Program`.

        Raises:
            ValueError: Если строка не является правилом.
        """
        rules: list[Substitution] = []
        for line in text.splitlines():
            stripped: str = line.strip()
            if not stripped or stripped.startswith(_COMMENT_PREFIX):
                continue
            rules.append(Substitution.from_string(stripped))
        return cls(rules)

    # -----------------------------------------------------------------------
    # Properties
    # -----------------------------------------------------------------------

    @property
    def rules(self) -> tuple[Substitution, ...]:
        """Правила программы в порядке добавления.

        Returns:
            Кортеж правил.
        """
        return tuple(self._rules)

    # -----------------------------------------------------------------------
    # Public methods
    # -----------------------------------------------------------------------

    def add_rule(self, rule: Substitution) -> None:
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

    def find(self, word: str) -> Substitution | None:
        """Найти первое правило, применимое к слову.

        Args:
            word: Слово, к которому применяются правила.

        Returns:
            Первое подходящее правило или ``None``.
        """
        for rule in self._rules:
            if rule.matches(word):
                return rule
        return None

    # -----------------------------------------------------------------------
    # Magic methods
    # -----------------------------------------------------------------------

    def __iter__(self) -> Iterator[Substitution]:
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
