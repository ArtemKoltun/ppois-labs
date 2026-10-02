"""
Тесты парсера машины Тьюринга.

Module: tests.turing_machine.test_parser
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from pathlib import Path

import pytest

from turing_machine.domain.machine import TuringMachine
from turing_machine.io.parser import load_machine
from turing_machine.io.parser import save_machine


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_VALID_JSON: str = """
{
  "alphabet": ["_", "1"],
  "blank": "_",
  "initial_tape": "111",
  "initial_head": 0,
  "initial_state": "q0",
  "final_states": ["q_accept"],
  "transitions": [
    "q0 1 q0 1 R",
    "q0 _ q_accept 1 S"
  ]
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
    path: Path = tmp_path / "machine.json"
    path.write_text(_VALID_JSON, encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestLoadMachine:
    """Проверки функции load_machine."""

    def test_loads_valid_file(self, valid_path: Path) -> None:
        """Корректный файл читается без ошибок."""
        machine: TuringMachine = load_machine(valid_path)
        assert machine.state == "q0"
        assert str(machine.tape) == "111"

    def test_missing_file_raises(self, tmp_path: Path) -> None:
        """Отсутствующий файл — FileNotFoundError."""
        missing: Path = tmp_path / "no_such.json"
        with pytest.raises(FileNotFoundError):
            load_machine(missing)

    def test_invalid_json_raises(self, tmp_path: Path) -> None:
        """Некорректный JSON — исключение."""
        path: Path = tmp_path / "broken.json"
        path.write_text("not a json", encoding="utf-8")
        with pytest.raises(Exception):
            load_machine(path)

    def test_loads_example_from_examples_dir(
        self,
        turing_examples: Path,
    ) -> None:
        """Пример из examples/turing/ читается и выполняется."""
        path: Path = turing_examples / "unary_increment.json"
        machine: TuringMachine = load_machine(path)
        machine.run()
        assert str(machine.tape) == "1111"


class TestSaveMachine:
    """Проверки функции save_machine."""

    def test_round_trip(self, tmp_path: Path) -> None:
        """Сохранение и повторная загрузка дают ту же машину."""
        original: TuringMachine = TuringMachine.from_string(_VALID_JSON)
        path: Path = tmp_path / "saved.json"
        save_machine(original, path)
        restored: TuringMachine = load_machine(path)
        assert restored.state == original.state
        assert str(restored.tape) == str(original.tape)

    def test_creates_file(self, tmp_path: Path) -> None:
        """save_machine создаёт файл."""
        path: Path = tmp_path / "out.json"
        machine: TuringMachine = TuringMachine.from_string(_VALID_JSON)
        save_machine(machine, path)
        assert path.exists()
