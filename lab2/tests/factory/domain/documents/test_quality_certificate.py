"""
Тесты класса QualityCertificate.

Module: tests.factory.domain.documents.test_quality_certificate
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.documents.document import Document
from factory.domain.documents.quality_certificate import (
    QualityCertificate,
)
from factory.domain.parts.part import Part
from factory.domain.workshops.quality_inspection import (
    QualityInspection,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_certificate(
    base: Document,
    part: Part,
    valid_until: str = "2026-12-31",
) -> QualityCertificate:
    """Создать сертификат.

    Args:
        base: Базовый документ.
        part: Деталь.
        valid_until: Срок действия.

    Returns:
        Объект ``QualityCertificate``.
    """
    inspection: QualityInspection = QualityInspection(
        part=part,
        inspector_name="Петров П.П.",
        batch_size=100,
        date="2026-02-01",
    )
    inspection.record_pass(98)
    return QualityCertificate(
        document=base,
        part=part,
        inspection=inspection,
        valid_until=valid_until,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestQualityCertificate:
    """Проверки класса QualityCertificate."""

    def test_creates(
        self,
        document: Document,
        piston_part: Part,
    ) -> None:
        """Сертификат создаётся.

        Args:
            document: Фикстура документа.
            piston_part: Фикстура детали.
        """
        cert: QualityCertificate = _make_certificate(
            document, piston_part
        )
        assert cert.number == "DOC-001"

    def test_is_valid_for(
        self,
        document: Document,
        piston_part: Part,
    ) -> None:
        """is_valid_for проверяет дату.

        Args:
            document: Фикстура документа.
            piston_part: Фикстура детали.
        """
        cert: QualityCertificate = _make_certificate(
            document, piston_part, valid_until="2026-12-31"
        )
        assert cert.is_valid_for("2026-06-01")
        assert not cert.is_valid_for("2027-01-01")

    def test_passed_all_checks(
        self,
        document: Document,
        piston_part: Part,
    ) -> None:
        """passed_all_checks проверяет ОТК.

        Args:
            document: Фикстура документа.
            piston_part: Фикстура детали.
        """
        cert: QualityCertificate = _make_certificate(
            document, piston_part
        )
        assert cert.passed_all_checks()

    def test_str(
        self,
        document: Document,
        piston_part: Part,
    ) -> None:
        """str содержит информацию.

        Args:
            document: Фикстура документа.
            piston_part: Фикстура детали.
        """
        cert: QualityCertificate = _make_certificate(
            document, piston_part
        )
        text: str = str(cert)
        assert "Сертификат" in text
