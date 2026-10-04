"""
Тесты класса Document.

Module: tests.factory.domain.documents.test_document
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from factory.domain.documents.document import Document
from factory.domain.personnel.employee import Employee

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestDocument:
    """Проверки класса Document."""

    def test_creates(self, document: Document) -> None:
        """Документ создаётся.

        Args:
            document: Фикстура документа.
        """
        assert document.number == "DOC-001"
        assert document.title == "Технический документ"

    def test_empty_number_raises(self, employee: Employee) -> None:
        """Пустой номер недопустим.

        Args:
            employee: Фикстура сотрудника.
        """
        with pytest.raises(ValueError):
            Document(
                number="",
                date="2026-01-01",
                author=employee,
                title="X",
            )

    def test_empty_title_raises(self, employee: Employee) -> None:
        """Пустой заголовок недопустим.

        Args:
            employee: Фикстура сотрудника.
        """
        with pytest.raises(ValueError):
            Document(
                number="X",
                date="2026-01-01",
                author=employee,
                title="",
            )

    def test_get_summary(self, document: Document) -> None:
        """get_summary возвращает краткое описание.

        Args:
            document: Фикстура документа.
        """
        text: str = document.get_summary()
        assert "DOC-001" in text
        assert "Технический документ" in text

    def test_is_signed(self, document: Document) -> None:
        """Базовый документ всегда подписан.

        Args:
            document: Фикстура документа.
        """
        assert document.is_signed()

    def test_equality(self, document: Document) -> None:
        """Равные по номеру.

        Args:
            document: Фикстура документа.
        """
        other: Document = Document(
            number="DOC-001",
            date="X",
            author=document.author,
            title="Y",
        )
        assert document == other

    def test_inequality(self, document: Document) -> None:
        """Разные документы.

        Args:
            document: Фикстура документа.
        """
        assert document != "not a document"

    def test_hash(self, document: Document) -> None:
        """Хеш по номеру.

        Args:
            document: Фикстура документа.
        """
        other: Document = Document(
            number="DOC-001",
            date="X",
            author=document.author,
            title="Y",
        )
        assert hash(document) == hash(other)

    def test_str(self, document: Document) -> None:
        """str возвращает поля.

        Args:
            document: Фикстура документа.
        """
        text: str = str(document)
        assert "DOC-001" in text
