"""
Тесты перечислений.

Module: tests.common.enums.test_enums
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from common.enums.notification_type import NotificationType
from common.enums.post_visibility import PostVisibility
from common.enums.report_status import ReportStatus
from common.enums.user_role import UserRole

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestUserRole:
    """Проверки UserRole."""

    def test_values(self) -> None:
        """Все значения корректны."""
        assert UserRole.USER.value == "user"
        assert UserRole.MODERATOR.value == "moderator"
        assert UserRole.ADMIN.value == "admin"
        assert UserRole.ADVERTISER.value == "advertiser"

    def test_str(self) -> None:
        """str возвращает русские названия."""
        assert str(UserRole.USER) == "пользователь"
        assert str(UserRole.MODERATOR) == "модератор"
        assert str(UserRole.ADMIN) == "администратор"
        assert str(UserRole.ADVERTISER) == "рекламодатель"

    def test_distinct(self) -> None:
        """Значения попарно различны."""
        assert len(set(UserRole)) == 4


class TestPostVisibility:
    """Проверки PostVisibility."""

    def test_values(self) -> None:
        """Все значения корректны."""
        assert PostVisibility.PUBLIC.value == "public"
        assert PostVisibility.FRIENDS.value == "friends"
        assert PostVisibility.CLOSE_FRIENDS.value == "close_friends"
        assert PostVisibility.PRIVATE.value == "private"

    def test_str(self) -> None:
        """str возвращает русские названия."""
        assert str(PostVisibility.PUBLIC) == "публичный"
        assert str(PostVisibility.FRIENDS) == "для друзей"
        assert str(PostVisibility.CLOSE_FRIENDS) == "для близких друзей"
        assert str(PostVisibility.PRIVATE) == "приватный"

    def test_distinct(self) -> None:
        """Значения попарно различны."""
        assert len(set(PostVisibility)) == 4


class TestNotificationType:
    """Проверки NotificationType."""

    def test_values(self) -> None:
        """Все значения корректны."""
        assert NotificationType.LIKE.value == "like"
        assert NotificationType.COMMENT.value == "comment"
        assert NotificationType.FRIEND_REQUEST.value == "friend_request"
        assert NotificationType.MESSAGE.value == "message"
        assert NotificationType.MENTION.value == "mention"
        assert NotificationType.SYSTEM.value == "system"

    def test_str(self) -> None:
        """str возвращает русские названия."""
        assert str(NotificationType.LIKE) == "лайк"
        assert str(NotificationType.COMMENT) == "комментарий"
        assert str(NotificationType.FRIEND_REQUEST) == "заявка в друзья"
        assert str(NotificationType.MESSAGE) == "сообщение"
        assert str(NotificationType.MENTION) == "упоминание"
        assert str(NotificationType.SYSTEM) == "системное"

    def test_distinct(self) -> None:
        """Значения попарно различны."""
        assert len(set(NotificationType)) == 6


class TestReportStatus:
    """Проверки ReportStatus."""

    def test_values(self) -> None:
        """Все значения корректны."""
        assert ReportStatus.PENDING.value == "pending"
        assert ReportStatus.IN_REVIEW.value == "in_review"
        assert ReportStatus.RESOLVED.value == "resolved"
        assert ReportStatus.REJECTED.value == "rejected"

    def test_str(self) -> None:
        """str возвращает русские названия."""
        assert str(ReportStatus.PENDING) == "ожидает"
        assert str(ReportStatus.IN_REVIEW) == "на рассмотрении"
        assert str(ReportStatus.RESOLVED) == "рассмотрена"
        assert str(ReportStatus.REJECTED) == "отклонена"

    def test_distinct(self) -> None:
        """Значения попарно различны."""
        assert len(set(ReportStatus)) == 4
