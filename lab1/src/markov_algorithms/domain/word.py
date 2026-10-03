"""
Слово, над которым работает нормальный алгорифм Маркова.

Module: markov_algorithms.domain.word
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from typing import Self

from common.abstract.readable import Readable
from common.abstract.writable import Writable

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Word(Readable, Writable):
    """Слово — строка символов, над которой работает алгорифм.

    Слово неизменяемо: каждая операция возвращает новый экземпляр.
    Это упрощает трассировку и откат.

    Attributes:
        _symbols: Строка символов слова.
    """

    # -----------------------------------------------------------------------
    # Constructors
    # -----------------------------------------------------------------------

    def __init__(self, symbols: str = "") -> None:
        """Создать слово из строки символов.

        Args:
            symbols: Строка, содержимое слова.
        """
        self._symbols: str = symbols

    @classmethod
    def _parse(cls, text: str) -> Self:
        """Разобрать слово из строки.

        Args:
            text: Текстовое представление слова.

        Returns:
            Новый экземпляр :class:`Word`.
        """
        return cls(text.strip())

    # -----------------------------------------------------------------------
    # Properties
    # -----------------------------------------------------------------------

    @property
    def symbols(self) -> str:
        """Содержимое слова как строка.

        Returns:
            Строка символов.
        """
        return self._symbols

    # -----------------------------------------------------------------------
    # Public methods
    # -----------------------------------------------------------------------

    def replace_first(self, left: str, right: str) -> Word:
        """Заменить первое вхождение ``left`` на ``right``.

        Args:
            left: Что искать.
            right: На что заменить.

        Returns:
            Новое слово с выполненной заменой.

        Raises:
            ValueError: Если ``left`` не входит в слово.
        """
        if left not in self._symbols:
            raise ValueError(
                f"подстрока {left!r} не найдена в слове"
            )
        replaced: str = self._symbols.replace(left, right, 1)
        return Word(replaced)

    def is_empty(self) -> bool:
        """Проверить, пусто ли слово.

        Returns:
            ``True``, если слово пустое.
        """
        return not self._symbols

    # -----------------------------------------------------------------------
    # Magic methods
    # -----------------------------------------------------------------------

    def __len__(self) -> int:
        """Вернуть длину слова.

        Returns:
            Число символов в слове.
        """
        return len(self._symbols)

    def __eq__(self, other: object) -> bool:
        """Сравнить два слова на равенство.

        Args:
            other: Другой объект для сравнения.

        Returns:
            ``True``, если строки символов совпадают.
        """
        if not isinstance(other, Word):
            return NotImplemented
        return self._symbols == other._symbols

    def __hash__(self) -> int:
        """Вернуть хеш слова.

        Returns:
            Целое число — хеш строки символов.
        """
        return hash(self._symbols)

    def __str__(self) -> str:
        """Вернуть текстовое представление слова.

        Returns:
            Строка символов.
        """
        return self._symbols
