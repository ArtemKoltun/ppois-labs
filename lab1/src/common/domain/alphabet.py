"""
Алфавит абстрактной машины — множество допустимых символов.

Module: common.domain.alphabet
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
from common.constants import SYMBOL_LENGTH


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Alphabet(Readable, Writable):
    """Множество допустимых символов абстрактной машины.

    Символом считается строка длиной ровно один. Порядок символов
    сохраняется в порядке добавления — это делает текстовое
    представление детерминированным.

    Attributes:
        _symbols: Словарь-множество, где ключи — символы алфавита.
    """

    # -----------------------------------------------------------------------
    # Constructors
    # -----------------------------------------------------------------------

    def __init__(self, symbols: Iterable[str] = ()) -> None:
        """Создать алфавит из набора символов.

        Args:
            symbols: Итерируемый объект со строками длиной 1.

        Raises:
            TypeError: Если очередной символ не является строкой.
            ValueError: Если длина очередного символа не равна 1.
        """
        self._symbols: dict[str, None] = {}
        for symbol in symbols:
            self._validate(symbol)
            self._symbols[symbol] = None

    @classmethod
    def _parse(cls, text: str) -> Self:
        """Разобрать строку вида ``"{a, b, c}"`` или ``"abc"``.

        Args:
            text: Текстовое представление алфавита.

        Returns:
            Новый экземпляр :class:`Alphabet`.
        """
        stripped: str = text.strip()
        if stripped.startswith("{") and stripped.endswith("}"):
            stripped = stripped[1:-1]
        if "," in stripped:
            symbols: list[str] = [
                s.strip() for s in stripped.split(",") if s.strip()
            ]
        else:
            symbols = list(stripped.replace(" ", ""))
        return cls(symbols)

    # -----------------------------------------------------------------------
    # Private methods
    # -----------------------------------------------------------------------

    @staticmethod
    def _validate(symbol: str) -> None:
        """Проверить, что ``symbol`` — корректный символ алфавита.

        Args:
            symbol: Проверяемое значение.

        Raises:
            TypeError: Если ``symbol`` не строка.
            ValueError: Если длина ``symbol`` не равна 1.
        """
        if not isinstance(symbol, str):
            raise TypeError("символ алфавита должен быть строкой")
        if len(symbol) != SYMBOL_LENGTH:
            raise ValueError(
                f"символ алфавита должен быть длиной {SYMBOL_LENGTH}, "
                f"получено {symbol!r}"
            )

    # -----------------------------------------------------------------------
    # Public methods
    # -----------------------------------------------------------------------

    def add(self, symbol: str) -> None:
        """Добавить символ в алфавит.

        Операция идемпотентна: повторное добавление не меняет алфавит.

        Args:
            symbol: Строка длиной 1.

        Returns:
            Ничего не возвращает.

        Raises:
            TypeError: Если ``symbol`` не строка.
            ValueError: Если длина ``symbol`` не равна 1.
        """
        self._validate(symbol)
        self._symbols[symbol] = None

    def remove(self, symbol: str) -> None:
        """Удалить символ из алфавита.

        Args:
            symbol: Символ, который нужно удалить.

        Returns:
            Ничего не возвращает.

        Raises:
            KeyError: Если символа нет в алфавите.
        """
        del self._symbols[symbol]

    # -----------------------------------------------------------------------
    # Magic methods
    # -----------------------------------------------------------------------

    def __contains__(self, symbol: object) -> bool:
        """Проверить принадлежность символа алфавиту.

        Args:
            symbol: Проверяемое значение.

        Returns:
            ``True``, если символ есть в алфавите, иначе ``False``.
        """
        return symbol in self._symbols

    def __iter__(self) -> Iterator[str]:
        """Итерироваться по символам в порядке добавления.

        Returns:
            Итератор по символам алфавита.
        """
        return iter(self._symbols)

    def __len__(self) -> int:
        """Вернуть мощность алфавита.

        Returns:
            Количество символов в алфавите.
        """
        return len(self._symbols)

    def __eq__(self, other: object) -> bool:
        """Сравнить два алфавита на равенство.

        Порядок символов не учитывается.

        Args:
            other: Другой объект для сравнения.

        Returns:
            ``True``, если множества символов совпадают.
        """
        if not isinstance(other, Alphabet):
            return NotImplemented
        return set(self._symbols) == set(other._symbols)

    def __hash__(self) -> int:
        """Вернуть хеш алфавита, не зависящий от порядка символов.

        Returns:
            Целое число — хеш множества символов.
        """
        return hash(frozenset(self._symbols))

    def __str__(self) -> str:
        """Вернуть текстовое представление вида ``"{a, b, c}"``.

        Returns:
            Строка с перечислением символов через запятую.
        """
        return "{" + ", ".join(self._symbols) + "}"
