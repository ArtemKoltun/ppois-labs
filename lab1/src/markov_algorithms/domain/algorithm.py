"""
Нормальный алгорифм Маркова.

Module: markov_algorithms.domain.algorithm
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from typing import Self
from collections.abc import Callable

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.constants import DEFAULT_MAX_STEPS
from common.domain.alphabet import Alphabet
from common.enums.machine_status import MachineStatus
from common.exceptions import StepLimitExceeded
from markov_algorithms.domain.program import Program
from markov_algorithms.domain.substitution import Substitution
from markov_algorithms.domain.word import Word


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class MarkovAlgorithm(Readable, Writable):
    """Нормальный алгорифм Маркова: слово и программа подстановок.

    Алгоритм координирует работу доменных объектов: ищет первое
    подходящее правило, применяет подстановку, решает, продолжать
    или остановиться.

    Attributes:
        _alphabet: Алфавит алгорифма.
        _program: Программа подстановок.
        _initial_word: Снимок начального слова.
        _word: Текущее слово.
        _steps: Число успешно выполненных шагов.
    """

    # -----------------------------------------------------------------------
    # Constructors
    # -----------------------------------------------------------------------

    def __init__(
        self,
        alphabet: Alphabet,
        program: Program,
        initial_word: Word,
    ) -> None:
        """Создать алгорифм из готовых доменных объектов.

        Args:
            alphabet: Алфавит алгорифма.
            program: Программа подстановок.
            initial_word: Начальное слово.
        """
        self._alphabet: Alphabet = alphabet
        self._program: Program = program
        self._initial_word: Word = initial_word
        self._word: Word = initial_word
        self._steps: int = 0

    @classmethod
    def _parse(cls, text: str) -> Self:
        """Разобрать алгорифм из JSON-описания.

        Args:
            text: JSON-строка с полями ``alphabet``, ``rules``
                и ``initial_word``.

        Returns:
            Новый экземпляр :class:`MarkovAlgorithm`.
        """
        import json

        data = json.loads(text)
        return cls(
            alphabet=Alphabet(data["alphabet"]),
            program=Program([
                Substitution.from_string(line)
                for line in data["rules"]
            ]),
            initial_word=Word(data["initial_word"]),
        )

    # -----------------------------------------------------------------------
    # Properties
    # -----------------------------------------------------------------------

    @property
    def word(self) -> Word:
        """Текущее слово.

        Returns:
            Объект слова.
        """
        return self._word

    @property
    def program(self) -> Program:
        """Программа подстановок.

        Returns:
            Объект программы.
        """
        return self._program

    @property
    def steps(self) -> int:
        """Число выполненных шагов.

        Returns:
            Неотрицательное целое число.
        """
        return self._steps

    @property
    def halted(self) -> bool:
        """Признак остановки алгорифма.

        Returns:
            ``True``, если ни одно правило не применимо.
        """
        return self._program.find(self._word.symbols) is None

    @property
    def alphabet(self) -> Alphabet:
        """Алфавит алгорифма.

        Returns:
            Объект алфавита.
        """
        return self._alphabet

    def set_word(self, word: Word) -> None:
        """Заменить текущее слово.

        Args:
            word: Новое слово.

        Returns:
            Ничего не возвращает.
        """
        self._word = word

    @property
    def status(self) -> MachineStatus:
        """Текущий статус алгорифма.

        Returns:
            :attr:`MachineStatus.HALTED`, :attr:`MachineStatus.RUNNING`
            или :attr:`MachineStatus.NOT_STARTED`.
        """
        if self.halted:
            return MachineStatus.HALTED
        if self._steps == 0:
            return MachineStatus.NOT_STARTED
        return MachineStatus.RUNNING

    # -----------------------------------------------------------------------
    # Public methods
    # -----------------------------------------------------------------------

    def step(self) -> bool:
        """Выполнить один шаг подстановки.

        Находит первое подходящее правило, заменяет первое вхождение
        левой части на правую. Возвращает ``False``, если правило
        заключительное или подходящего правила нет.

        Returns:
            ``True``, если нужно продолжить выполнение.
        """
        rule: Substitution | None = self._program.find(
            self._word.symbols
        )
        if rule is None:
            return False
        self._word = self._word.replace_first(rule.left, rule.right)
        self._steps += 1
        return not rule.is_final

    def run(
        self,
        max_steps: int = DEFAULT_MAX_STEPS,
        on_step: Callable[[MarkovAlgorithm], None] | None = None,
    ) -> None:
        """Выполнять шаги до остановки или до лимита.

        Args:
            max_steps: Максимальное число шагов.
            on_step: Необязательный callback, вызываемый после
                каждого успешного шага.

        Returns:
            Ничего не возвращает.

        Raises:
            StepLimitExceeded: Если алгорифм не остановился за
                ``max_steps`` шагов.
        """
        for _ in range(max_steps):
            before: int = self._steps
            moved: bool = self.step()
            if self._steps > before and on_step is not None:
                on_step(self)
            if not moved:
                return
        raise StepLimitExceeded(max_steps)

    def reset(self) -> None:
        """Вернуть алгорифм в начальное состояние.

        Returns:
            Ничего не возвращает.
        """
        self._word = self._initial_word
        self._steps = 0

    # -----------------------------------------------------------------------
    # Magic methods
    # -----------------------------------------------------------------------

    def __str__(self) -> str:
        """Вернуть JSON-представление алгорифма.

        Returns:
            Строка с описанием начальной конфигурации алгорифма.
        """
        import json

        data = {
            "alphabet": list(self._alphabet),
            "initial_word": str(self._initial_word),
            "rules": [str(r) for r in self._program.rules],
        }
        return json.dumps(data, ensure_ascii=False, indent=2)
