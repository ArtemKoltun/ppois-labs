"""
Сборочный цех.

Module: factory.domain.workshops.assembly_shop
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from factory.domain.workshops.workshop import Workshop

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class AssemblyShop(Workshop):
    """Сборочный цех.

    Attributes:
        _conveyor_count: Число конвейеров.
        _assembly_lines: Число линий.
    """

    def __init__(
        self,
        workshop: Workshop,
        conveyor_count: int,
        assembly_lines: int,
    ) -> None:
        """Создать сборочный цех.

        Args:
            workshop: Базовый цех.
            conveyor_count: Число конвейеров.
            assembly_lines: Число линий.
        """
        super().__init__(
            name=workshop.name,
            number=workshop.number,
            area=workshop._area,
            workshop_head=workshop._workshop_head,
        )
        self._conveyor_count: int = conveyor_count
        self._assembly_lines: int = assembly_lines

    def total_lines(self) -> int:
        """Вернуть общее число линий.

        Returns:
            Целое число.
        """
        return self._conveyor_count + self._assembly_lines

    def is_conveyor_type(self) -> bool:
        """Проверить, конвейерный ли цех.

        Returns:
            ``True``, если конвейеров больше 5.
        """
        return self._conveyor_count > 5

    def can_produce_in_parallel(self) -> bool:
        """Проверить параллельное производство.

        Returns:
            ``True``, если линий больше одной.
        """
        return self._assembly_lines > 1
