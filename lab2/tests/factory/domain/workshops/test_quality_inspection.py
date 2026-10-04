"""
Тесты класса QualityInspection.

Module: tests.factory.domain.workshops.test_quality_inspection
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.exceptions import QualityControlFailedError
from factory.domain.parts.part import Part
from factory.domain.workshops.quality_inspection import (
    QualityInspection,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_inspection(
    part: Part,
    batch: int = 100,
) -> QualityInspection:
    """Создать проверку качества.

    Args:
        part: Деталь.
        batch: Размер партии.

    Returns:
        Объект ``QualityInspection``.
    """
    return QualityInspection(
        part=part,
        inspector_name="Петров П.П.",
        batch_size=batch,
        date="2026-01-20",
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestQualityInspection:
    """Проверки класса QualityInspection."""

    def test_creates(self, piston_part: Part) -> None:
        """Проверка создаётся.

        Args:
            piston_part: Фикстура детали.
        """
        ins: QualityInspection = _make_inspection(piston_part)
        assert ins.batch_size == 100
        assert ins.passed_count == 0

    def test_zero_batch_raises(self, piston_part: Part) -> None:
        """Нулевая партия недопустима.

        Args:
            piston_part: Фикстура детали.
        """
        with pytest.raises(ValueError):
            _make_inspection(piston_part, batch=0)

    def test_record_pass(self, piston_part: Part) -> None:
        """record_pass фиксирует годные.

        Args:
            piston_part: Фикстура детали.
        """
        ins: QualityInspection = _make_inspection(piston_part)
        ins.record_pass(97)
        assert ins.passed_count == 97

    def test_record_pass_capped(self, piston_part: Part) -> None:
        """record_pass не превышает размер партии.

        Args:
            piston_part: Фикстура детали.
        """
        ins: QualityInspection = _make_inspection(piston_part, batch=10)
        ins.record_pass(20)
        assert ins.passed_count == 10

    def test_pass_rate(self, piston_part: Part) -> None:
        """pass_rate считает долю.

        Args:
            piston_part: Фикстура детали.
        """
        ins: QualityInspection = _make_inspection(piston_part, batch=100)
        ins.record_pass(90)
        assert ins.pass_rate() == 0.9

    def test_is_successful(self, piston_part: Part) -> None:
        """is_successful проверяет порог.

        Args:
            piston_part: Фикстура детали.
        """
        ins: QualityInspection = _make_inspection(piston_part, batch=100)
        ins.record_pass(96)
        assert ins.is_successful()

    def test_not_successful(self, piston_part: Part) -> None:
        """Мало годных — провал.

        Args:
            piston_part: Фикстура детали.
        """
        ins: QualityInspection = _make_inspection(piston_part, batch=100)
        ins.record_pass(50)
        assert not ins.is_successful()

    def test_raise_if_failed(self, piston_part: Part) -> None:
        """raise_if_failed падает при провале.

        Args:
            piston_part: Фикстура детали.
        """
        ins: QualityInspection = _make_inspection(piston_part, batch=100)
        ins.record_pass(50)
        with pytest.raises(QualityControlFailedError):
            ins.raise_if_failed()

    def test_raise_if_failed_ok(self, piston_part: Part) -> None:
        """raise_if_failed не падает при успехе.

        Args:
            piston_part: Фикстура детали.
        """
        ins: QualityInspection = _make_inspection(piston_part, batch=100)
        ins.record_pass(98)
        ins.raise_if_failed()  # не должно бросить

    def test_equality(self, piston_part: Part) -> None:
        """Равные проверки.

        Args:
            piston_part: Фикстура детали.
        """
        a: QualityInspection = _make_inspection(piston_part)
        b: QualityInspection = _make_inspection(piston_part)
        assert a == b
        assert a != "not inspection"

    def test_hash(self, piston_part: Part) -> None:
        """Хеш проверок.

        Args:
            piston_part: Фикстура детали.
        """
        a: QualityInspection = _make_inspection(piston_part)
        b: QualityInspection = _make_inspection(piston_part)
        assert hash(a) == hash(b)

    def test_str(self, piston_part: Part) -> None:
        """str возвращает поля.

        Args:
            piston_part: Фикстура детали.
        """
        ins: QualityInspection = _make_inspection(piston_part)
        text: str = str(ins)
        assert "Петров" in text
        assert "2026-01-20" in text
