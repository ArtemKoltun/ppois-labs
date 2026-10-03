"""
Правило подстановки нормального алгорифма Маркова.

Module: markov_algorithms.domain.substitution
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from typing import Self

from markov_algorithms.domain.abstract.rule import AbstractRule

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_ARROW: str = "->"
"""Разделитель левой и правой частей правила."""

_FINAL_MARKER: str = "."
"""Маркер заключительного правила сразу после стрелки."""


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Substitution(AbstractRule):
    """Правило подстановки нормального алгорифма Маркова.

    Обычное правило заменяет первое вхождение ``left`` на ``right``,
    после чего алгоритм продолжает работу с начала списка правил.
    Заключительное правило заменяет и останавливает алгоритм.

    Attributes:
        _left: Левая часть правила.
        _right: Правая часть правила.
        _is_final: Признак заключительного правила.
    """

    # -----------------------------------------------------------------------
    # Constructors
    # -----------------------------------------------------------------------

    def __init__(
        self,
        left: str,
        right: str,
        is_final: bool = False,
    ) -> None:
        """Создать правило подстановки.

        Args:
            left: Левая часть правила.
            right: Правая часть правила.
            is_final: ``True`` для заключительного правила.

        Raises:
            ValueError: Если обе части пусты одновременно.
        """
        if not left and not right:
            raise ValueError(
                "обе части правила не могут быть пустыми"
            )
        self._left: str = left
        self._right: str = right
        self._is_final: bool = is_final

    @classmethod
    def _parse(cls, text: str) -> Self:
        """Разобрать строку вида ``"ab -> ba"`` или ``"ab ->. ba"``.

        Args:
            text: Текстовое представление правила.

        Returns:
            Новый экземпляр :class:`Substitution`.

        Raises:
            ValueError: Если строка не содержит стрелку.
        """
        stripped: str = text.strip()
        if _ARROW not in stripped:
            raise ValueError(
                f"в правиле нет разделителя {_ARROW!r}"
            )
        left_raw, right_raw = stripped.split(_ARROW, 1)
        is_final: bool = right_raw.startswith(_FINAL_MARKER)
        if is_final:
            right_raw = right_raw[len(_FINAL_MARKER):]
        return cls(
            left=left_raw.strip(),
            right=right_raw.strip(),
            is_final=is_final,
        )

    # -----------------------------------------------------------------------
    # Properties
    # -----------------------------------------------------------------------

    @property
    def left(self) -> str:
        """Левая часть правила — что ищем.

        Returns:
            Строка символов.
        """
        return self._left

    @property
    def right(self) -> str:
        """Правая часть правила — на что заменяем.

        Returns:
            Строка символов.
        """
        return self._right

    @property
    def is_final(self) -> bool:
        """Признак заключительного правила.

        Returns:
            ``True``, если правило заключительное.
        """
        return self._is_final

    # -----------------------------------------------------------------------
    # Public methods
    # -----------------------------------------------------------------------

    def matches(self, word: str) -> bool:
        """Проверить, входит ли левая часть в слово.

        Args:
            word: Слово, к которому применяется правило.

        Returns:
            ``True``, если левая часть входит в слово.
        """
        return self._left in word

    # -----------------------------------------------------------------------
    # Magic methods
    # -----------------------------------------------------------------------

    def __eq__(self, other: object) -> bool:
        """Сравнить два правила на равенство.

        Args:
            other: Другой объект для сравнения.

        Returns:
            ``True``, если все поля совпадают.
        """
        if not isinstance(other, Substitution):
            return NotImplemented
        return (
            self._left == other._left
            and self._right == other._right
            and self._is_final == other._is_final
        )

    def __hash__(self) -> int:
        """Вернуть хеш правила.

        Returns:
            Целое число — хеш тройки (left, right, is_final).
        """
        return hash((self._left, self._right, self._is_final))

    def __str__(self) -> str:
        """Вернуть текстовое представление правила.

        Returns:
            Строка вида ``"ab -> ba"`` или ``"ab ->. ba"``.
        """
        arrow: str = (
            f"{_ARROW}{_FINAL_MARKER}" if self._is_final else _ARROW
        )
        return f"{self._left} {arrow} {self._right}"
