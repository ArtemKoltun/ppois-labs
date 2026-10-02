"""
Тесты парсера нормального алгорифма Маркова.

Module: tests.markov_algorithms.test_parser
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from pathlib import Path

import pytest

from markov_algorithms.domain.algorithm import MarkovAlgorithm
from markov_algorithms.io.parser import load_algorithm
from markov_algorithms.io.parser import save_algorithm


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_VALID_JSON: str = """
{
  "alphabet": ["1", "+"],
  "initial_word": "11+111",
  "rules": ["1+ -> +1", "+ ->. "]
}
"""


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def valid_path(tmp_path: Path) -> Path:
    """Создать временный файл с корректным описанием.

    Args:
        tmp_path: Стандартная фикстура pytest.

    Returns:
        Путь к созданному файлу.
    """
    path: Path = tmp_path / "algorithm.json"
    path.write_text(_VALID_JSON, encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestLoadAlgorithm:
    """Проверки функции load_algorithm."""

    def test_loads_valid_file(self, valid_path: Path) -> None:
        """Корректный файл читается без ошибок."""
        algo: MarkovAlgorithm = load_algorithm(valid_path)
        assert str(algo.word) == "11+111"

    def test_missing_file_raises(self, tmp_path: Path) -> None:
        """Отсутствующий файл — FileNotFoundError."""
        missing: Path = tmp_path / "no_such.json"
        with pytest.raises(FileNotFoundError):
            load_algorithm(missing)

    def test_invalid_json_raises(self, tmp_path: Path) -> None:
        """Некорректный JSON — исключение."""
        path: Path = tmp_path / "broken.json"
        path.write_text("not a json", encoding="utf-8")
        with pytest.raises(Exception):
            load_algorithm(path)

    def test_loads_example_from_examples_dir(
        self,
        markov_examples: Path,
    ) -> None:
        """Пример из examples/markov/ читается и выполняется."""
        path: Path = markov_examples / "unary_addition.json"
        algo: MarkovAlgorithm = load_algorithm(path)
        algo.run()
        assert str(algo.word) == "11111"


class TestSaveAlgorithm:
    """Проверки функции save_algorithm."""

    def test_round_trip(self, tmp_path: Path) -> None:
        """Сохранение и повторная загрузка дают тот же алгорифм."""
        original: MarkovAlgorithm = MarkovAlgorithm.from_string(
            _VALID_JSON
        )
        path: Path = tmp_path / "saved.json"
        save_algorithm(original, path)
        restored: MarkovAlgorithm = load_algorithm(path)
        assert str(restored.word) == str(original.word)

    def test_creates_file(self, tmp_path: Path) -> None:
        """save_algorithm создаёт файл."""
        path: Path = tmp_path / "out.json"
        algo: MarkovAlgorithm = MarkovAlgorithm.from_string(_VALID_JSON)
        save_algorithm(algo, path)
        assert path.exists()
