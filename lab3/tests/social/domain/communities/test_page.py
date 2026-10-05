"""
Тесты класса Page.

Module: tests.social.domain.communities.test_page
"""

from __future__ import annotations

from social.domain.communities.community import Community
from social.domain.communities.page import Page


class TestPage:
    """Проверки класса Page."""

    def test_creates(self) -> None:
        """Страница создаётся."""
        base: Community = Community("Brand", "ivan")
        p: Page = Page(base)
        assert p.name == "Brand"
        assert p.category == "other"
        assert not p.is_official()

    def test_set_website(self) -> None:
        """set_website устанавливает сайт."""
        base: Community = Community("X", "ivan")
        p: Page = Page(base)
        p.set_website("https://x.com")
        assert p._website == "https://x.com"

    def test_mark_official(self) -> None:
        """mark_official помечает."""
        base: Community = Community("X", "ivan")
        p: Page = Page(base)
        p.mark_official()
        assert p.is_official()

    def test_change_category(self) -> None:
        """change_category меняет категорию."""
        base: Community = Community("X", "ivan")
        p: Page = Page(base)
        p.change_category("media")
        assert p.category == "media"
