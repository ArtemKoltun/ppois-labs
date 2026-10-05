"""
Тесты класса Profile.

Module: tests.social.domain.users.test_profile
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.exceptions import InvalidUserError
from social.domain.users.profile import Profile

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestProfile:
    """Проверки класса Profile."""

    def test_creates_default(self) -> None:
        """Профиль создаётся с дефолтами."""
        p: Profile = Profile()
        assert p.bio == ""
        assert p.city == ""
        assert not p.is_private

    def test_long_bio_raises(self) -> None:
        """Длинное bio недопустимо."""
        with pytest.raises(InvalidUserError):
            Profile(bio="a" * 600)

    def test_update_bio(self) -> None:
        """update_bio меняет описание."""
        p: Profile = Profile()
        p.update_bio("Привет")
        assert p.bio == "Привет"

    def test_update_bio_too_long_raises(self) -> None:
        """Слишком длинное bio падает."""
        p: Profile = Profile()
        with pytest.raises(InvalidUserError):
            p.update_bio("a" * 600)

    def test_set_avatar(self) -> None:
        """set_avatar меняет url."""
        p: Profile = Profile()
        p.set_avatar("https://example.com/a.jpg")
        assert p.avatar_url == "https://example.com/a.jpg"
        assert p.has_avatar()

    def test_has_avatar_false(self) -> None:
        """has_avatar для пустого."""
        assert not Profile().has_avatar()

    def test_set_private(self) -> None:
        """set_private меняет приватность."""
        p: Profile = Profile()
        p.set_private(True)
        assert p.is_private

    def test_is_complete(self) -> None:
        """is_complete проверяет bio и city."""
        p: Profile = Profile(bio="x", city="Москва")
        assert p.is_complete()
        assert not Profile(bio="x").is_complete()

    def test_equality(self) -> None:
        """Равные по bio и city."""
        a: Profile = Profile(bio="x", city="Москва")
        b: Profile = Profile(bio="x", city="Москва")
        assert a == b
        assert a != "not profile"

    def test_hash(self) -> None:
        """Хеш профиля."""
        a: Profile = Profile(bio="x", city="Москва")
        b: Profile = Profile(bio="x", city="Москва")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        p: Profile = Profile(bio="x", city="Москва")
        text: str = str(p)
        assert "x" in text
        assert "Москва" in text

    def test_parse(self) -> None:
        """from_string разбирает профиль."""
        p: Profile = Profile.from_string("bio; url; Москва; site; true")
        assert p.bio == "bio"
        assert p.is_private
