"""
Публичная страница.

Module: social.domain.communities.page
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from social.domain.communities.community import Community

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class Page(Community):
    """Публичная страница бренда или медиа.

    Attributes:
        _category: Категория.
        _website: Сайт.
        _is_official: Официальная ли.
    """

    def __init__(
        self,
        community: Community,
        category: str = "other",
    ) -> None:
        """Создать страницу.

        Args:
            community: Базовое сообщество.
            category: Категория.
        """
        super().__init__(
            name=community.name,
            owner=community.owner,
            description=community._description,
        )
        self._category: str = category
        self._website: str = ""
        self._is_official: bool = False

    @property
    def category(self) -> str:
        """Категория.

        Returns:
            Строка.
        """
        return self._category

    def set_website(self, url: str) -> None:
        """Установить сайт.

        Args:
            url: Адрес.

        Returns:
            Ничего не возвращает.
        """
        self._website = url

    def mark_official(self) -> None:
        """Отметить как официальную.

        Returns:
            Ничего не возвращает.
        """
        self._is_official = True

    def is_official(self) -> bool:
        """Проверить официальность.

        Returns:
            ``True``, если официальная.
        """
        return self._is_official

    def change_category(self, category: str) -> None:
        """Сменить категорию.

        Args:
            category: Новая категория.

        Returns:
            Ничего не возвращает.
        """
        self._category = category
