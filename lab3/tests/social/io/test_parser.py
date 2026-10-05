"""
Тесты парсера.

Module: tests.social.io.test_parser
"""

from __future__ import annotations

from pathlib import Path

from social.domain.users.user import User
from social.io.parser import load_object, save_object


class TestParser:
    """Проверки load_object и save_object."""

    def test_save_and_load(self, tmp_path: Path) -> None:
        """Сохранение и загрузка возвращают тот же объект.

        Args:
            tmp_path: Временная директория pytest.
        """
        user: User = User(username="ivan", email="ivan@mail.ru")
        path: Path = tmp_path / "user.txt"
        save_object(user, path)
        loaded: User = load_object(User, path)
        assert loaded.username == "ivan"
        assert loaded.email == "ivan@mail.ru"

    def test_load_missing_raises(self, tmp_path: Path) -> None:
        """Отсутствующий файл падает.

        Args:
            tmp_path: Временная директория pytest.
        """
        import pytest
        missing: Path = tmp_path / "no.txt"
        with pytest.raises(FileNotFoundError):
            load_object(User, missing)
