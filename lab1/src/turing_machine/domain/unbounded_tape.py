"""
Неограниченная в обе стороны лента машины Тьюринга.

Module: turing_machine.domain.unbounded_tape
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from typing import Self

from common.constants import DEFAULT_BLANK, SYMBOL_LENGTH
from turing_machine.domain.abstract.tape import AbstractTape

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class UnboundedTape(AbstractTape):
    """Лента, хранящая только непустые ячейки.

    Пустые позиции не занимают память: при чтении из неинициализированной
    ячейки возвращается ``blank``. Это даёт ленту, неограниченную в обе
    стороны, без предварительного выделения массива.

    Attributes:
        _blank: Символ пустой ячейки.
        _cells: Словарь «позиция → символ» для непустых ячеек.
    """

    # -----------------------------------------------------------------------
    # Constructors
    # -----------------------------------------------------------------------

    def __init__(
        self,
        blank: str = DEFAULT_BLANK,
        initial: str = "",
        start: int = 0,
    ) -> None:
        """Создать ленту с заданным пустым символом и содержимым.

        Args:
            blank: Символ пустой ячейки, строка длиной 1.
            initial: Начальное содержимое ленты, записываемое начиная
                с позиции ``start``.
            start: Позиция, с которой записывается ``initial``.

        Raises:
            ValueError: Если длина ``blank`` не равна 1.
        """
        self._validate_symbol(blank, "blank-символ")
        self._blank: str = blank
        self._cells: dict[int, str] = {}
        for offset, symbol in enumerate(initial):
            self._cells[start + offset] = symbol

    @classmethod
    def _parse(cls, text: str) -> Self:
        """Разобрать строку вида ``"abc"`` или ``"blank=. abc"``.

        Args:
            text: Текстовое представление ленты.

        Returns:
            Новый экземпляр :class:`UnboundedTape`.
        """
        blank: str = DEFAULT_BLANK
        body: str = text.strip()
        if body.startswith("blank="):
            parts: list[str] = body.split(maxsplit=1)
            blank = parts[0][len("blank="):]
            body = parts[1] if len(parts) > 1 else ""
        return cls(blank=blank, initial=body)

    # -----------------------------------------------------------------------
    # Private methods
    # -----------------------------------------------------------------------

    @staticmethod
    def _validate_symbol(symbol: str, name: str) -> None:
        """Проверить, что ``symbol`` — один допустимый символ.

        Args:
            symbol: Проверяемое значение.
            name: Имя символа для сообщения об ошибке.

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
    def blank(self) -> str:
        """Символ пустой ячейки.

        Returns:
            Строка длиной 1.
        """
        return self._blank

    # -----------------------------------------------------------------------
    # Public methods
    # -----------------------------------------------------------------------

    def read(self, position: int) -> str:
        """Вернуть символ в заданной позиции.

        Args:
            position: Целочисленная координата ячейки.

        Returns:
            Символ в позиции ``position`` или ``blank``, если
            ячейка не инициализирована.
        """
        return self._cells.get(position, self._blank)

    def write(self, position: int, symbol: str) -> None:
        """Записать символ в заданную позицию.

        Запись ``blank`` удаляет ячейку из хранилища.

        Args:
            position: Целочисленная координата ячейки.
            symbol: Строка длиной 1.

        Returns:
            Ничего не возвращает.

        Raises:
            ValueError: Если длина ``symbol`` не равна 1.
        """
        self._validate_symbol(symbol, "записываемый символ")
        if symbol == self._blank:
            self._cells.pop(position, None)
        else:
            self._cells[position] = symbol

    # -----------------------------------------------------------------------
    # Magic methods
    # -----------------------------------------------------------------------

    def __eq__(self, other: object) -> bool:
        """Сравнить две ленты на равенство.

        Args:
            other: Другой объект для сравнения.

        Returns:
            ``True``, если совпадают ``blank`` и содержимое ячеек.
        """
        if not isinstance(other, UnboundedTape):
            return NotImplemented
        return self._blank == other._blank and self._cells == other._cells

    def __hash__(self) -> int:
        """Вернуть хеш состояния ленты.

        Returns:
            Целое число — хеш пары (blank, cells).
        """
        return hash((self._blank, frozenset(self._cells.items())))

    def __str__(self) -> str:
        """Вернуть текстовое представление ленты.

        Пустые ячейки внутри диапазона заполняются ``blank``.

        Returns:
            Строка с содержимым ленты от минимальной до максимальной
            непустой позиции.
        """
        if not self._cells:
            return self._blank
        lo: int = min(self._cells)
        hi: int = max(self._cells)
        return "".join(
            self._cells.get(i, self._blank) for i in range(lo, hi + 1)
        )
