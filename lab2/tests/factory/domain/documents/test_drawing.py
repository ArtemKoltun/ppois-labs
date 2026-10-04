"""
Тесты класса Drawing.

Module: tests.factory.domain.documents.test_drawing
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.documents.document import Document
from factory.domain.documents.drawing import Drawing
from factory.domain.parts.part import Part


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_drawing(
    base: Document,
    part: Part,
    scale: str = "1:1",
    format_: str = "A3",
) -> Drawing:
    """Создать чертёж.

    Args:
        base: Базовый документ.
        part: Деталь.
        scale: Масштаб.
        format_: Формат.

    Returns:
        Объект ``Drawing``.
    """
    return Drawing(
        document=base,
        part=part,
        scale=scale,
        format_=format_,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestDrawing:
    """Проверки класса Drawing."""

    def test_creates(
        self,
        document: Document,
        piston_part: Part,
    ) -> None:
        """Чертёж создаётся.

        Args:
            document: Фикстура документа.
            piston_part: Фикстура детали.
        """
        drawing: Drawing = _make_drawing(document, piston_part)
        assert drawing.number == "DOC-001"

    def test_is_large_format(
        self,
        document: Document,
        piston_part: Part,
    ) -> None:
        """is_large_format проверяет формат.

        Args:
            document: Фикстура документа.
            piston_part: Фикстура детали.
        """
        a1: Drawing = _make_drawing(
            document, piston_part, format_="A1"
        )
        a3: Drawing = _make_drawing(
            document, piston_part, format_="A3"
        )
        assert a1.is_large_format()
        assert not a3.is_large_format()

    def test_is_zoomed(
        self,
        document: Document,
        piston_part: Part,
    ) -> None:
        """is_zoomed проверяет масштаб.

        Args:
            document: Фикстура документа.
            piston_part: Фикстура детали.
        """
        zoomed: Drawing = _make_drawing(
            document, piston_part, scale="2:1"
        )
        normal: Drawing = _make_drawing(
            document, piston_part, scale="1:1"
        )
        assert zoomed.is_zoomed()
        assert not normal.is_zoomed()

    def test_matches_part(
        self,
        document: Document,
        piston_part: Part,
    ) -> None:
        """matches_part проверяет деталь.

        Args:
            document: Фикстура документа.
            piston_part: Фикстура детали.
        """
        drawing: Drawing = _make_drawing(document, piston_part)
        assert drawing.matches_part(piston_part)

    def test_str(
        self,
        document: Document,
        piston_part: Part,
    ) -> None:
        """str содержит информацию о чертеже.

        Args:
            document: Фикстура документа.
            piston_part: Фикстура детали.
        """
        drawing: Drawing = _make_drawing(document, piston_part)
        text: str = str(drawing)
        assert "Чертёж" in text
