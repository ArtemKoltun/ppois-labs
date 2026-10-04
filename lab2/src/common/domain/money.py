"""
Денежная сумма.

Module: common.domain.money
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.constants import DEFAULT_CURRENCY


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Money:
    """Денежная сумма с валютой.

    Attributes:
        _amount: Величина суммы.
        _currency: Код валюты.
    """

    # -----------------------------------------------------------------------
    # Constructors
    # -----------------------------------------------------------------------

    def __init__(
        self,
        amount: float,
        currency: str = DEFAULT_CURRENCY,
    ) -> None:
        """Создать денежную сумму.

        Args:
            amount: Величина суммы.
            currency: Код валюты.

        Raises:
            ValueError: Если сумма отрицательная или валюта пуста.
        """
        if amount < 0:
            raise ValueError("сумма не может быть отрицательной")
        if not currency:
            raise ValueError("валюта не может быть пустой")
        self._amount: float = amount
        self._currency: str = currency

    # -----------------------------------------------------------------------
    # Properties
    # -----------------------------------------------------------------------

    @property
    def amount(self) -> float:
        """Величина суммы.

        Returns:
            Число с плавающей точкой.
        """
        return self._amount

    @property
    def currency(self) -> str:
        """Код валюты.

        Returns:
            Строка валюты.
        """
        return self._currency

    # -----------------------------------------------------------------------
    # Public methods
    # -----------------------------------------------------------------------

    def add(self, other: Money) -> Money:
        """Сложить две суммы.

        Args:
            other: Другая денежная сумма.

        Returns:
            Новая сумма.

        Raises:
            ValueError: Если валюты различаются.
        """
        if self._currency != other._currency:
            raise ValueError("нельзя складывать разные валюты")
        return Money(self._amount + other._amount, self._currency)

    def multiply(self, factor: float) -> Money:
        """Умножить сумму на коэффициент.

        Args:
            factor: Множитель.

        Returns:
            Новая сумма.
        """
        return Money(self._amount * factor, self._currency)

    # -----------------------------------------------------------------------
    # Magic methods
    # -----------------------------------------------------------------------

    def __eq__(self, other: object) -> bool:
        """Сравнить две суммы.

        Args:
            other: Другой объект.

        Returns:
            ``True``, если суммы и валюты совпадают.
        """
        if not isinstance(other, Money):
            return NotImplemented
        return (
            self._amount == other._amount
            and self._currency == other._currency
        )

    def __hash__(self) -> int:
        """Вернуть хеш суммы.

        Returns:
            Целое число.
        """
        return hash((self._amount, self._currency))

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка вида ``"1000.00 RUB"``.
        """
        return f"{self._amount:.2f} {self._currency}"
