"""
Правило перехода машины Тьюринга.

Module: turing_machine.domain.transition
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from typing import Self

from common.constants import SYMBOL_LENGTH
from turing_machine.domain.abstract.rule import AbstractRule
from turing_machine.domain.direction import Direction


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_TRANSITION_PARTS: int = 5
"""Число полей в текстовом представлении правила."""


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Transition(AbstractRule):
    """Правило перехода машины Тьюринга.

    Правило задаёт: в состоянии ``current_state`` при чтении
    ``read_symbol`` перейти в ``next_state``, записать ``write_symbol``
    и сдвинуть каретку в направлении ``direction``.

    Attributes:
        _current_state: Состояние, в котором применимо правило.
        _read_symbol: Символ, который должно прочитать правило.
        _next_state: Состояние, в которое переходит машина.
        _write_symbol: Символ, который записывается на ленту.
        _direction: Направление сдвига каретки.
    """

    # -----------------------------------------------------------------------
    # Constructors
    # -----------------------------------------------------------------------

    def __init__(
        self,
        current_state: str,
        read_symbol: str,
        next_state: str,
        write_symbol: str,
        direction: Direction,
    ) -> None:
        """Создать правило перехода.

        Args:
            current_state: Состояние, в котором применимо правило.
            read_symbol: Символ, который должно прочитать правило.
            next_state: Состояние, в которое переходит машина.
            write_symbol: Символ, который записывается на ленту.
            direction: Направление сдвига каретки.

        Raises:
            ValueError: Если символы не длиной 1 или состояния пусты.
        """
        self._validate_state(current_state, "текущее состояние")
        self._validate_state(next_state, "следующее состояние")
        self._validate_symbol(read_symbol, "читаемый символ")
        self._validate_symbol(write_symbol, "записываемый символ")
        self._current_state: str = current_state
        self._read_symbol: str = read_symbol
        self._next_state: str = next_state
        self._write_symbol: str = write_symbol
        self._direction: Direction = direction

    @classmethod
    def _parse(cls, text: str) -> Self:
        """Разобрать строку вида ``"q0 1 q1 0 R"``.

        Args:
            text: Текстовое представление правила.

        Returns:
            Новый экземпляр :class:`Transition`.

        Raises:
            ValueError: Если число полей не равно пяти.
        """
        parts: list[str] = text.split()
        if len(parts) != _TRANSITION_PARTS:
            raise ValueError(
                f"правило должно содержать {_TRANSITION_PARTS} полей, "
                f"получено {len(parts)}"
            )
        return cls(
            current_state=parts[0],
            read_symbol=parts[1],
            next_state=parts[2],
            write_symbol=parts[3],
            direction=Direction.from_char(parts[4]),
        )

    # -----------------------------------------------------------------------
    # Private methods
    # -----------------------------------------------------------------------

    @staticmethod
    def _validate_state(state: str, name: str) -> None:
        """Проверить, что имя состояния непусто.

        Args:
            state: Проверяемое значение.
            name: Имя поля для сообщения об ошибке.

        Raises:
            ValueError: Если строка пуста.
        """
        if not state:
            raise ValueError(f"{name} не может быть пустым")

    @staticmethod
    def _validate_symbol(symbol: str, name: str) -> None:
        """Проверить, что символ имеет длину 1.

        Args:
            symbol: Проверяемое значение.
            name: Имя поля для сообщения об ошибке.

        Raises:
            ValueError: Если длина ``symbol`` не равна 1.
        """
        if len(symbol) != SYMBOL_LENGTH:
            raise ValueError(
                f"{name} должен быть длиной {SYMBOL_LENGTH}"
            )

    # -----------------------------------------------------------------------
    # Properties
    # -----------------------------------------------------------------------

    @property
    def current_state(self) -> str:
        """Состояние, в котором применимо правило.

        Returns:
            Имя состояния.
        """
        return self._current_state

    @property
    def read_symbol(self) -> str:
        """Символ, который должно прочитать правило.

        Returns:
            Строка длиной 1.
        """
        return self._read_symbol

    @property
    def next_state(self) -> str:
        """Состояние, в которое переходит машина.

        Returns:
            Имя состояния.
        """
        return self._next_state

    @property
    def write_symbol(self) -> str:
        """Символ, который записывается на ленту.

        Returns:
            Строка длиной 1.
        """
        return self._write_symbol

    @property
    def direction(self) -> Direction:
        """Направление сдвига каретки.

        Returns:
            Элемент перечисления :class:`Direction`.
        """
        return self._direction

    # -----------------------------------------------------------------------
    # Public methods
    # -----------------------------------------------------------------------

    def matches(self, state: str, symbol: str) -> bool:
        """Проверить применимость правила к паре (состояние, символ).

        Args:
            state: Текущее состояние машины.
            symbol: Символ, прочитанный с ленты.

        Returns:
            ``True``, если правило применимо.
        """
        return (
            self._current_state == state
            and self._read_symbol == symbol
        )

    # -----------------------------------------------------------------------
    # Magic methods
    # -----------------------------------------------------------------------

    def __eq__(self, other: object) -> bool:
        """Сравнить два правила на равенство.

        Args:
            other: Другой объект для сравнения.

        Returns:
            ``True``, если все пять полей совпадают.
        """
        if not isinstance(other, Transition):
            return NotImplemented
        return (
            self._current_state == other._current_state
            and self._read_symbol == other._read_symbol
            and self._next_state == other._next_state
            and self._write_symbol == other._write_symbol
            and self._direction is other._direction
        )

    def __hash__(self) -> int:
        """Вернуть хеш правила.

        Returns:
            Целое число — хеш всех полей правила.
        """
        return hash((
            self._current_state,
            self._read_symbol,
            self._next_state,
            self._write_symbol,
            self._direction,
        ))

    def __str__(self) -> str:
        """Вернуть текстовое представление правила.

        Returns:
            Строка вида ``"q0 1 q1 0 R"``.
        """
        return (
            f"{self._current_state} {self._read_symbol} "
            f"{self._next_state} {self._write_symbol} "
            f"{self._direction.value}"
        )
