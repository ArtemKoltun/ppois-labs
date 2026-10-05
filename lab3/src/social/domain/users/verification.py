"""
Верификация пользователя.

Module: social.domain.users.verification
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Verification(Readable, Writable):
    """Верификация аккаунта (синяя галочка).

    Attributes:
        _document_number: Номер документа.
        _is_verified: Подтверждена ли.
        _reason: Причина отказа.
        _verifier_name: Имя проверяющего.
    """

    # -----------------------------------------------------------------------
    # Constructors
    # -----------------------------------------------------------------------

    def __init__(
        self,
        document_number: str,
        verifier_name: str = "",
    ) -> None:
        """Создать заявку на верификацию.

        Args:
            document_number: Номер документа.
            verifier_name: Имя проверяющего.
        """
        self._document_number: str = document_number
        self._is_verified: bool = False
        self._reason: str = ""
        self._verifier_name: str = verifier_name

    @classmethod
    def _parse(cls, text: str) -> Verification:
        """Разобрать верификацию из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            document_number=parts[0],
            verifier_name=parts[1],
        )

    # -----------------------------------------------------------------------
    # Properties
    # -----------------------------------------------------------------------

    @property
    def document_number(self) -> str:
        """Номер документа.

        Returns:
            Строка.
        """
        return self._document_number

    @property
    def is_verified(self) -> bool:
        """Подтверждена ли верификация.

        Returns:
            ``True``, если подтверждена.
        """
        return self._is_verified

    @property
    def reason(self) -> str:
        """Причина отказа.

        Returns:
            Строка.
        """
        return self._reason

    # -----------------------------------------------------------------------
    # Public methods
    # -----------------------------------------------------------------------

    def approve(self) -> None:
        """Одобрить верификацию.

        Returns:
            Ничего не возвращает.
        """
        self._is_verified = True
        self._reason = ""

    def reject(self, reason: str) -> None:
        """Отклонить верификацию.

        Args:
            reason: Причина отказа.

        Returns:
            Ничего не возвращает.
        """
        self._is_verified = False
        self._reason = reason

    def assign_verifier(self, name: str) -> None:
        """Назначить проверяющего.

        Args:
            name: Имя проверяющего.

        Returns:
            Ничего не возвращает.
        """
        self._verifier_name = name

    def has_verifier(self) -> bool:
        """Проверить наличие проверяющего.

        Returns:
            ``True``, если проверяющий назначен.
        """
        return bool(self._verifier_name)

    # -----------------------------------------------------------------------
    # Magic methods
    # -----------------------------------------------------------------------

    def __eq__(self, other: object) -> bool:
        """Сравнить две верификации.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении номера документа.
        """
        if not isinstance(other, Verification):
            return NotImplemented
        return self._document_number == other._document_number

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._document_number)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return f"{self._document_number}; {self._verifier_name}"
