"""
Тесты класса FriendRequest.

Module: tests.social.domain.users.test_friend_request
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.exceptions import FriendshipError
from social.domain.users.friend_request import FriendRequest

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestFriendRequest:
    """Проверки класса FriendRequest."""

    def test_creates(self) -> None:
        """Заявка создаётся."""
        fr: FriendRequest = FriendRequest("ivan", "petr")
        assert fr.from_username == "ivan"
        assert fr.to_username == "petr"
        assert fr.is_pending()

    def test_same_users_raises(self) -> None:
        """Заявка самому себе недопустима."""
        with pytest.raises(FriendshipError):
            FriendRequest("ivan", "ivan")

    def test_accept(self) -> None:
        """accept принимает заявку."""
        fr: FriendRequest = FriendRequest("ivan", "petr")
        fr.accept()
        assert fr.is_accepted
        assert not fr.is_pending()

    def test_reject(self) -> None:
        """reject отклоняет."""
        fr: FriendRequest = FriendRequest("ivan", "petr")
        fr.reject()
        assert fr.is_rejected

    def test_accept_after_reject_raises(self) -> None:
        """Принять отклонённую нельзя."""
        fr: FriendRequest = FriendRequest("ivan", "petr")
        fr.reject()
        with pytest.raises(FriendshipError):
            fr.accept()

    def test_reject_after_accept_raises(self) -> None:
        """Отклонить принятую нельзя."""
        fr: FriendRequest = FriendRequest("ivan", "petr")
        fr.accept()
        with pytest.raises(FriendshipError):
            fr.reject()

    def test_has_message(self) -> None:
        """has_message проверяет сообщение."""
        a: FriendRequest = FriendRequest("ivan", "petr", "Привет")
        b: FriendRequest = FriendRequest("ivan", "petr")
        assert a.has_message()
        assert not b.has_message()

    def test_equality(self) -> None:
        """Равные по паре (от, кому)."""
        a: FriendRequest = FriendRequest("ivan", "petr")
        b: FriendRequest = FriendRequest("ivan", "petr")
        assert a == b
        assert a != "not request"

    def test_hash(self) -> None:
        """Хеш по паре."""
        a: FriendRequest = FriendRequest("ivan", "petr")
        b: FriendRequest = FriendRequest("ivan", "petr")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        fr: FriendRequest = FriendRequest("ivan", "petr", "Привет")
        text: str = str(fr)
        assert "ivan" in text
        assert "petr" in text

    def test_parse(self) -> None:
        """from_string разбирает заявку."""
        fr: FriendRequest = FriendRequest.from_string(
            "ivan; petr; Привет"
        )
        assert fr.from_username == "ivan"
        assert fr.message == "Привет"
