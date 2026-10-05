"""
Тесты класса Verification.

Module: tests.social.domain.users.test_verification
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from social.domain.users.verification import Verification

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestVerification:
    """Проверки класса Verification."""

    def test_creates(self) -> None:
        """Верификация создаётся."""
        v: Verification = Verification(document_number="P-123")
        assert v.document_number == "P-123"
        assert not v.is_verified
        assert not v.has_verifier()

    def test_approve(self) -> None:
        """approve подтверждает."""
        v: Verification = Verification(document_number="P-123")
        v.approve()
        assert v.is_verified
        assert v.reason == ""

    def test_reject(self) -> None:
        """reject отклоняет с причиной."""
        v: Verification = Verification(document_number="P-123")
        v.reject("нечитаемый документ")
        assert not v.is_verified
        assert v.reason == "нечитаемый документ"

    def test_assign_verifier(self) -> None:
        """assign_verifier назначает."""
        v: Verification = Verification(document_number="P-123")
        v.assign_verifier("admin")
        assert v.has_verifier()

    def test_equality(self) -> None:
        """Равные по номеру документа."""
        a: Verification = Verification(document_number="P-123")
        b: Verification = Verification(document_number="P-123")
        assert a == b
        assert a != "not verification"

    def test_hash(self) -> None:
        """Хеш по номеру документа."""
        a: Verification = Verification(document_number="P-123")
        b: Verification = Verification(document_number="P-123")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        v: Verification = Verification(
            document_number="P-123", verifier_name="admin"
        )
        text: str = str(v)
        assert "P-123" in text
        assert "admin" in text

    def test_parse(self) -> None:
        """from_string разбирает верификацию."""
        v: Verification = Verification.from_string("P-123; admin")
        assert v.document_number == "P-123"
        assert v._verifier_name == "admin"
