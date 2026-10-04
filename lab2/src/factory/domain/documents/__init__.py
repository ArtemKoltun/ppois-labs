"""
Доменные классы документов.

Module: factory.domain.documents
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from factory.domain.documents.document import Document
from factory.domain.documents.drawing import Drawing
from factory.domain.documents.quality_certificate import (
    QualityCertificate,
)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

__all__ = ["Document", "Drawing", "QualityCertificate"]
