"""
Базовое исключение социальной сети.

Module: common.exceptions.base
"""

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class SocialNetworkError(Exception):
    """Базовое исключение всех модулей проекта.

    Attributes:
        message: Текст сообщения об ошибке.
    """

    def __init__(self, message: str) -> None:
        """Создать исключение с сообщением.

        Args:
            message: Описание ошибки.
        """
        self.message: str = message
        super().__init__(message)
