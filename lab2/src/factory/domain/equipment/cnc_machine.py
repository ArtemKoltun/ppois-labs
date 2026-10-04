"""
Станок с ЧПУ.

Module: factory.domain.equipment.cnc_machine
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from factory.domain.equipment.machine import Machine


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class CNCMachine(Machine):
    """Станок с числовым программным управлением.

    Attributes:
        _controller_model: Модель контроллера.
        _programs_count: Число загруженных программ.
        _has_network: Есть ли сетевое подключение.
    """

    def __init__(
        self,
        machine: Machine,
        controller_model: str,
        has_network: bool = False,
    ) -> None:
        """Создать станок с ЧПУ.

        Args:
            machine: Базовый станок.
            controller_model: Модель контроллера.
            has_network: Есть ли сеть.
        """
        super().__init__(
            equipment=machine,
            power_kw=machine._power_kw,
            max_rpm=machine._max_rpm,
            accuracy_class=machine._accuracy_class,
        )
        self._controller_model: str = controller_model
        self._programs_count: int = 0
        self._has_network: bool = has_network

    def load_program(self) -> None:
        """Загрузить программу обработки.

        Returns:
            Ничего не возвращает.
        """
        self._programs_count += 1

    def is_connected(self) -> bool:
        """Проверить наличие сетевого подключения.

        Returns:
            ``True``, если станок в сети.
        """
        return self._has_network

    def can_remote_control(self) -> bool:
        """Проверить возможность удалённого управления.

        Returns:
            ``True``, если есть сеть и программы.
        """
        return self._has_network and self._programs_count > 0
