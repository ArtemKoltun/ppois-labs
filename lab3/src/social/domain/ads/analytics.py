"""
Аналитика пользователя.

Module: social.domain.ads.analytics
"""

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable


class Analytics(Readable, Writable):
    """Аналитика действий пользователя.

    Attributes:
        _user: Пользователь.
        _views: Число просмотров.
        _likes: Число лайков.
        _shares: Число репостов.
        _session_minutes: Минуты в сети.
    """

    def __init__(
        self,
        user: str,
    ) -> None:
        """Создать аналитику.

        Args:
            user: Пользователь.
        """
        self._user: str = user
        self._views: int = 0
        self._likes: int = 0
        self._shares: int = 0
        self._session_minutes: int = 0

    @classmethod
    def _parse(cls, text: str) -> Analytics:
        """Разобрать аналитику из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(user=parts[0])

    @property
    def user(self) -> str:
        """Пользователь.

        Returns:
            Строка.
        """
        return self._user

    @property
    def views(self) -> int:
        """Просмотры.

        Returns:
            Целое число.
        """
        return self._views

    def add_view(self) -> None:
        """Добавить просмотр.

        Returns:
            Ничего не возвращает.
        """
        self._views += 1

    def add_like(self) -> None:
        """Добавить лайк.

        Returns:
            Ничего не возвращает.
        """
        self._likes += 1

    def add_share(self) -> None:
        """Добавить репост.

        Returns:
            Ничего не возвращает.
        """
        self._shares += 1

    def add_session(self, minutes: int) -> None:
        """Добавить время сессии.

        Args:
            minutes: Минуты.

        Returns:
            Ничего не возвращает.
        """
        self._session_minutes += minutes

    def engagement_rate(self) -> float:
        """Рассчитать вовлечённость.

        Returns:
            Число от 0 до 1.
        """
        if self._views == 0:
            return 0.0
        return (self._likes + self._shares) / self._views

    def is_engaged(self) -> bool:
        """Проверить вовлечённость.

        Returns:
            ``True``, если вовлечённость выше 5%.
        """
        return self.engagement_rate() > 0.05

    def __eq__(self, other: object) -> bool:
        """Сравнить две аналитики.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении пользователя.
        """
        if not isinstance(other, Analytics):
            return NotImplemented
        return self._user == other._user

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._user)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка.
        """
        return self._user
