"""
Сегмент аудитории.

Module: social.domain.ads.audience_segment
"""

from __future__ import annotations

from common.abstract.readable import Readable
from common.abstract.writable import Writable


class AudienceSegment(Readable, Writable):
    """Сегмент целевой аудитории.

    Attributes:
        _name: Название.
        _age_min: Минимальный возраст.
        _age_max: Максимальный возраст.
        _users_count: Размер сегмента.
    """

    def __init__(
        self,
        name: str,
        age_min: int,
        age_max: int,
    ) -> None:
        """Создать сегмент.

        Args:
            name: Название.
            age_min: Мин. возраст.
            age_max: Макс. возраст.

        Raises:
            ValueError: Если возрасты некорректны.
        """
        if age_min > age_max:
            raise ValueError(
                "минимальный возраст больше максимального"
            )
        self._name: str = name
        self._age_min: int = age_min
        self._age_max: int = age_max
        self._users_count: int = 0

    @classmethod
    def _parse(cls, text: str) -> AudienceSegment:
        """Разобрать сегмент из строки.

        Args:
            text: Строка с полями через точку с запятой.

        Returns:
            Новый экземпляр.
        """
        parts: list[str] = [p.strip() for p in text.split(";")]
        return cls(
            name=parts[0],
            age_min=int(parts[1]),
            age_max=int(parts[2]),
        )

    @property
    def name(self) -> str:
        """Название.

        Returns:
            Строка.
        """
        return self._name

    @property
    def users_count(self) -> int:
        """Размер.

        Returns:
            Целое число.
        """
        return self._users_count

    def add_users(self, count: int) -> None:
        """Добавить пользователей.

        Args:
            count: Количество.

        Returns:
            Ничего не возвращает.
        """
        self._users_count += count

    def matches_age(self, age: int) -> bool:
        """Проверить возраст.

        Args:
            age: Возраст.

        Returns:
            ``True``, если попадает в сегмент.
        """
        return self._age_min <= age <= self._age_max

    def is_large(self) -> bool:
        """Проверить размер.

        Returns:
            ``True``, если больше 100 000.
        """
        return self._users_count > 100_000

    def __eq__(self, other: object) -> bool:
        """Сравнить два сегмента.

        Args:
            other: Другой объект.

        Returns:
            ``True`` при совпадении названия.
        """
        if not isinstance(other, AudienceSegment):
            return NotImplemented
        return self._name == other._name

    def __hash__(self) -> int:
        """Вернуть хеш.

        Returns:
            Целое число.
        """
        return hash(self._name)

    def __str__(self) -> str:
        """Вернуть текстовое представление.

        Returns:
            Строка с полями через точку с запятой.
        """
        return (
            f"{self._name}; {self._age_min}; {self._age_max}"
        )
