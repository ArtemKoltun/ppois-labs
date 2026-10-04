"""
Тесты исключений.

Module: tests.common.exceptions.test_exceptions
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.exceptions import (
    EmployeeNotAvailableException,
    EquipmentBrokenException,
    EquipmentNotAvailableException,
    FactoryException,
    InsufficientMaterialException,
    InvalidMaterialException,
    InvalidOrderException,
    InvalidPartException,
    InvalidSpecificationException,
    OrderNotFoundException,
    ProductionDeadlineMissedException,
    QualityControlFailedException,
)


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_ALL_EXCEPTIONS: list[type[FactoryException]] = [
    EmployeeNotAvailableException,
    EquipmentBrokenException,
    EquipmentNotAvailableException,
    InsufficientMaterialException,
    InvalidMaterialException,
    InvalidOrderException,
    InvalidPartException,
    InvalidSpecificationException,
    OrderNotFoundException,
    ProductionDeadlineMissedException,
    QualityControlFailedException,
]
"""Все конкретные исключения проекта."""


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestFactoryException:
    """Проверки базового исключения."""

    def test_inherits_exception(self) -> None:
        """FactoryException наследуется от Exception."""
        assert issubclass(FactoryException, Exception)

    def test_message(self) -> None:
        """Сообщение сохраняется в поле message."""
        exc: FactoryException = FactoryException("что-то пошло не так")
        assert exc.message == "что-то пошло не так"
        assert str(exc) == "что-то пошло не так"


class TestConcreteExceptions:
    """Проверки всех конкретных исключений."""

    @pytest.mark.parametrize("exc_class", _ALL_EXCEPTIONS)
    def test_inherits_factory(
        self,
        exc_class: type[FactoryException],
    ) -> None:
        """Каждое исключение наследуется от FactoryException.

        Args:
            exc_class: Класс исключения.
        """
        assert issubclass(exc_class, FactoryException)

    @pytest.mark.parametrize("exc_class", _ALL_EXCEPTIONS)
    def test_raises_with_message(
        self,
        exc_class: type[FactoryException],
    ) -> None:
        """Каждое исключение можно поднять с сообщением.

        Args:
            exc_class: Класс исключения.
        """
        with pytest.raises(exc_class) as exc_info:
            raise exc_class("тестовое сообщение")
        assert "тестовое сообщение" in str(exc_info.value)
