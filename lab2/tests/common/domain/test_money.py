"""
Тесты класса Money.

Module: tests.common.domain.test_money
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.domain.money import Money


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestMoney:
    """Проверки класса Money."""

    def test_creates(self, money: Money) -> None:
        """Money создаётся с суммой и валютой.

        Args:
            money: Фикстура денежной суммы.
        """
        assert money.amount == 1000.0
        assert money.currency == "RUB"

    def test_custom_currency(self) -> None:
        """Можно задать валюту."""
        m: Money = Money(amount=100.0, currency="USD")
        assert m.currency == "USD"

    def test_negative_raises(self) -> None:
        """Отрицательная сумма недопустима."""
        with pytest.raises(ValueError):
            Money(amount=-1.0)

    def test_empty_currency_raises(self) -> None:
        """Пустая валюта недопустима."""
        with pytest.raises(ValueError):
            Money(amount=100.0, currency="")

    def test_add(self, money: Money) -> None:
        """Сложение двух сумм.

        Args:
            money: Фикстура денежной суммы.
        """
        result: Money = money.add(Money(amount=500.0))
        assert result.amount == 1500.0

    def test_add_different_currency_raises(self, money: Money) -> None:
        """Разные валюты не складываются.

        Args:
            money: Фикстура денежной суммы.
        """
        with pytest.raises(ValueError):
            money.add(Money(amount=100.0, currency="USD"))

    def test_multiply(self, money: Money) -> None:
        """Умножение на коэффициент.

        Args:
            money: Фикстура денежной суммы.
        """
        result: Money = money.multiply(2.5)
        assert result.amount == 2500.0

    def test_equality(self, money: Money) -> None:
        """Одинаковые суммы равны.

        Args:
            money: Фикстура денежной суммы.
        """
        assert money == Money(amount=1000.0)

    def test_inequality(self, money: Money) -> None:
        """Разные суммы не равны.

        Args:
            money: Фикстура денежной суммы.
        """
        assert money != Money(amount=1001.0)
        assert money != "not money"

    def test_hash(self, money: Money) -> None:
        """Одинаковые суммы имеют одинаковый хеш.

        Args:
            money: Фикстура денежной суммы.
        """
        assert hash(money) == hash(Money(amount=1000.0))

    def test_str(self, money: Money) -> None:
        """str возвращает сумму с валютой.

        Args:
            money: Фикстура денежной суммы.
        """
        assert str(money) == "1000.00 RUB"
