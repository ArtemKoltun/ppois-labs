"""
Тесты класса Reaction.

Module: tests.social.domain.content.test_reaction
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from social.domain.content.reaction import Reaction

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestReaction:
    """Проверки класса Reaction."""

    def test_creates_default(self) -> None:
        """Реакция создаётся с типом like."""
        r: Reaction = Reaction("ivan", "post1")
        assert r.user == "ivan"
        assert r.reaction_type == "like"

    def test_creates_custom(self) -> None:
        """Реакция с пользовательским типом."""
        r: Reaction = Reaction("ivan", "post1", "love")
        assert r.reaction_type == "love"

    def test_change_type(self) -> None:
        """change_type меняет тип."""
        r: Reaction = Reaction("ivan", "post1")
        r.change_type("haha")
        assert r.reaction_type == "haha"

    def test_is_positive(self) -> None:
        """is_positive для like и love."""
        like: Reaction = Reaction("ivan", "p", "like")
        love: Reaction = Reaction("ivan", "p", "love")
        angry: Reaction = Reaction("ivan", "p", "angry")
        assert like.is_positive()
        assert love.is_positive()
        assert not angry.is_positive()

    def test_equality(self) -> None:
        """Равные по паре (пользователь, контент)."""
        a: Reaction = Reaction("ivan", "p1")
        b: Reaction = Reaction("ivan", "p1", "love")
        assert a == b
        assert a != "not reaction"

    def test_hash(self) -> None:
        """Хеш реакции."""
        a: Reaction = Reaction("ivan", "p1")
        b: Reaction = Reaction("ivan", "p1", "love")
        assert hash(a) == hash(b)

    def test_str(self) -> None:
        """str возвращает поля."""
        r: Reaction = Reaction("ivan", "p1", "like")
        text: str = str(r)
        assert "ivan" in text
        assert "like" in text

    def test_parse(self) -> None:
        """from_string разбирает реакцию."""
        r: Reaction = Reaction.from_string("ivan; p1; love")
        assert r.user == "ivan"
        assert r.reaction_type == "love"
