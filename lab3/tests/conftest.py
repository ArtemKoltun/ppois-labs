"""
Общие фикстуры тестов.

Module: tests.conftest
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

import pytest

from common.enums.user_role import UserRole
from social.domain.users.user import User

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def user() -> User:
    """Обычный пользователь.

    Returns:
        Объект ``User``.
    """
    return User(
        username="ivan",
        email="ivan@mail.ru",
        display_name="Иван",
    )


@pytest.fixture
def second_user() -> User:
    """Второй пользователь.

    Returns:
        Объект ``User``.
    """
    return User(
        username="petr",
        email="petr@mail.ru",
        display_name="Пётр",
    )


@pytest.fixture
def admin() -> User:
    """Администратор.

    Returns:
        Объект ``User``.
    """
    return User(
        username="admin",
        email="admin@social.net",
        display_name="Админ",
        role=UserRole.ADMIN,
    )
