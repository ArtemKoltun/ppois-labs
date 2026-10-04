"""
Сталь.

Module: factory.domain.materials.steel
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from factory.domain.materials.material import Material

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Steel(Material):
    """Сталь.

    Attributes:
        _grade: Марка стали.
        _hardness: Твёрдость по HB.
    """

    def __init__(
        self,
        material: Material,
        grade: str,
        hardness: float,
    ) -> None:
        """Создать сталь.

        Args:
            material: Базовый материал.
            grade: Марка стали.
            hardness: Твёрдость.
        """
        super().__init__(
            name=material.name,
            material_type=material.material_type,
            density=material.density,
            cost_per_kg=material.cost_per_kg,
        )
        self._grade: str = grade
        self._hardness: float = hardness

    def is_hardened(self) -> bool:
        """Проверить, закалена ли сталь.

        Returns:
            ``True``, если твёрдость больше 50 HB.
        """
        return self._hardness > 50

    def is_stainless(self) -> bool:
        """Проверить, нержавеющая ли сталь.

        Returns:
            ``True``, если марка начинается с "12Х18".
        """
        return self._grade.startswith("12Х18")
