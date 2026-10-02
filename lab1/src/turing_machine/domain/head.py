"""
Каретка машины Тьюринга.

Module: turing_machine.domain.head
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.constants import DEFAULT_HEAD_POSITION
from turing_machine.domain.direction import Direction


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Head:
    """Каретка машины Тьюринга — позиция на ленте.

    Каретка не хранит содержимое ленты; её задача — знать текущую
    позицию и уметь перемещаться. Для сдвига на одну ячейку есть
    методы :meth:`increment` и :meth:`decrement`.

    Attributes:
        _position: Текущая позиция каретки на ленте.
    """

    # -----------------------------------------------------------------------
    # Constructors
    # -----------------------------------------------------------------------

    def __init__(self, position: int = DEFAULT_HEAD_POSITION) -> None:
        """Создать каретку в заданной позиции.

        Args:
            position: Начальная позиция каретки.
        """
        self._position: int = position

    # -----------------------------------------------------------------------
    # Properties
    # -----------------------------------------------------------------------

    @property
    def position(self) -> int:
        """Текущая позиция каретки.

        Returns:
            Целочисленная координата каретки на ленте.
        """
        return self._position

    # -----------------------------------------------------------------------
    # Public methods
    # -----------------------------------------------------------------------

    def move(self, direction: Direction) -> None:
        """Сдвинуть каретку в заданном направлении.

        Args:
            direction: Направление сдвига.

        Returns:
            Ничего не возвращает.
        """
        if direction is Direction.LEFT:
            self.decrement()
        elif direction is Direction.RIGHT:
            self.increment()
        # STAY: позиция не меняется

    def increment(self) -> None:
        """Сдвинуть каретку на одну позицию вправо.

        Returns:
            Ничего не возвращает.
        """
        self._position += 1

    def decrement(self) -> None:
        """Сдвинуть каретку на одну позицию влево.

        Returns:
            Ничего не возвращает.
        """
        self._position -= 1

    def reset(self, position: int = DEFAULT_HEAD_POSITION) -> None:
        """Вернуть каретку в заданную позицию.

        Args:
            position: Позиция, в которую возвращается каретка.

        Returns:
            Ничего не возвращает.
        """
        self._position = position

    # -----------------------------------------------------------------------
    # Magic methods
    # -----------------------------------------------------------------------

    def __eq__(self, other: object) -> bool:
        """Сравнить две каретки на равенство.

        Args:
            other: Другой объект для сравнения.

        Returns:
            ``True``, если позиции совпадают.
        """
        if not isinstance(other, Head):
            return NotImplemented
        return self._position == other._position

    def __hash__(self) -> int:
        """Вернуть хеш позиции каретки.

        Returns:
            Целое число — хеш позиции.
        """
        return hash(self._position)

    def __str__(self) -> str:
        """Вернуть текстовое представление позиции.

        Returns:
            Строка вида ``"Head(position=0)"``.
        """
        return f"Head(position={self._position})"
