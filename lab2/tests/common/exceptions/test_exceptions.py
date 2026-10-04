"""
Тесты исключений.

Module: tests.common.exceptions.test_exceptions
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.exceptions import (
    EmployeeNotAvailableError,
    EquipmentBrokenError,
    EquipmentNotAvailableError,
    FactoryError,
    InsufficientMaterialError,
    InvalidMaterialError,
    InvalidOrderError,
    InvalidPartError,
    InvalidSpecificationError,
    OrderNotFoundError,
    ProductionDeadlineMissedError,
    QualityControlFailedError,
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_ALL_EXCEPTIONS: list[type[FactoryError]] = [
    EmployeeNotAvailableError,
    EquipmentBrokenError,
    EquipmentNotAvailableError,
    InsufficientMaterialError,
    InvalidMaterialError,
    InvalidOrderError,
    InvalidPartError,
    InvalidSpecificationError,
    OrderNotFoundError,
    ProductionDeadlineMissedError,
    QualityControlFailedError,
]
"""Все конкретные исключения проекта."""


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestFactoryError:
    """Проверки базового исключения."""

    def test_inherits_exception(self) -> None:
        """FactoryError наследуется от Exception."""
        assert issubclass(FactoryError, Exception)

    def test_message(self) -> None:
        """Сообщение сохраняется в поле message."""
        exc: FactoryError = FactoryError("что-то пошло не так")
        assert exc.message == "что-то пошло не так"
        assert str(exc) == "что-то пошло не так"


class TestConcreteExceptions:
    """Проверки всех конкретных исключений."""

    @pytest.mark.parametrize("exc_class", _ALL_EXCEPTIONS)
    def test_inherits_factory(
        self,
        exc_class: type[FactoryError],
    ) -> None:
        """Каждое исключение наследуется от FactoryError.

        Args:
            exc_class: Класс исключения.
        """
        assert issubclass(exc_class, FactoryError)

    @pytest.mark.parametrize("exc_class", _ALL_EXCEPTIONS)
    def test_raises_with_message(
        self,
        exc_class: type[FactoryError],
    ) -> None:
        """Каждое исключение можно поднять с сообщением.

        Args:
            exc_class: Класс исключения.
        """
        with pytest.raises(exc_class) as exc_info:
            raise exc_class("тестовое сообщение")
        assert "тестовое сообщение" in str(exc_info.value)
