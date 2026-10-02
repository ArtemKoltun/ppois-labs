"""
Машина Тьюринга.

Module: turing_machine.domain.machine
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

import json
from collections.abc import Callable
from typing import Any
from typing import Self

from common.abstract.readable import Readable
from common.abstract.writable import Writable
from common.constants import DEFAULT_BLANK
from common.constants import DEFAULT_HEAD_POSITION
from common.constants import DEFAULT_MAX_STEPS
from common.domain.alphabet import Alphabet
from common.enums.machine_status import MachineStatus
from common.exceptions import StepLimitExceeded
from turing_machine.domain.head import Head
from turing_machine.domain.program import Program
from turing_machine.domain.transition import Transition
from turing_machine.domain.unbounded_tape import UnboundedTape


# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class TuringMachine(Readable, Writable):
    """Машина Тьюринга: лента, каретка, программа и состояния.

    Машина координирует работу доменных объектов: читает символ под
    кареткой, ищет правило в программе, записывает новый символ,
    двигает каретку и меняет текущее состояние.

    Attributes:
        _alphabet: Алфавит машины.
        _tape: Лента машины.
        _head: Каретка.
        _program: Программа машины.
        _initial_state: Начальное состояние.
        _final_states: Множество конечных состояний.
        _initial_tape: Снимок начального содержимого ленты.
        _initial_head: Снимок начальной позиции каретки.
        _state: Текущее состояние.
        _steps: Число успешно выполненных шагов.
    """

    # -----------------------------------------------------------------------
    # Constructors
    # -----------------------------------------------------------------------

    def __init__(
        self,
        alphabet: Alphabet,
        tape: UnboundedTape,
        head: Head,
        program: Program,
        initial_state: str,
        final_states: set[str],
    ) -> None:
        """Создать машину Тьюринга из готовых доменных объектов.

        Args:
            alphabet: Алфавит машины.
            tape: Лента машины.
            head: Каретка.
            program: Программа машины.
            initial_state: Начальное состояние.
            final_states: Множество конечных состояний.
        """
        self._alphabet: Alphabet = alphabet
        self._tape: UnboundedTape = tape
        self._head: Head = head
        self._program: Program = program
        self._initial_state: str = initial_state
        self._final_states: set[str] = set(final_states)
        self._initial_tape: str = str(tape)
        self._initial_head: int = head.position
        self._state: str = initial_state
        self._steps: int = 0

    @classmethod
    def _parse(cls, text: str) -> Self:
        """Разобрать машину из JSON-описания.

        Args:
            text: JSON-строка с полями ``alphabet``, ``transitions``,
                ``initial_state``, ``final_states`` и опциональными
                ``blank``, ``initial_tape``, ``initial_head``.

        Returns:
            Новый экземпляр :class:`TuringMachine`.
        """
        data: dict[str, Any] = json.loads(text)
        return cls(
            alphabet=Alphabet(data["alphabet"]),
            tape=cls._tape_from_data(data),
            head=Head(data.get("initial_head", DEFAULT_HEAD_POSITION)),
            program=cls._program_from_data(data),
            initial_state=data["initial_state"],
            final_states=set(data["final_states"]),
        )

    @staticmethod
    def _tape_from_data(data: dict[str, Any]) -> UnboundedTape:
        """Создать ленту из словаря с описанием машины.

        Args:
            data: Словарь с полями ``blank`` и ``initial_tape``.

        Returns:
            Новая лента.
        """
        return UnboundedTape(
            blank=data.get("blank", DEFAULT_BLANK),
            initial=data.get("initial_tape", ""),
        )

    @staticmethod
    def _program_from_data(data: dict[str, Any]) -> Program:
        """Создать программу из словаря с описанием машины.

        Args:
            data: Словарь с полем ``transitions`` — списком строк.

        Returns:
            Новая программа.
        """
        rules: list[Transition] = [
            Transition.from_string(line) for line in data["transitions"]
        ]
        return Program(rules)

    # -----------------------------------------------------------------------
    # Properties
    # -----------------------------------------------------------------------

    @property
    def state(self) -> str:
        """Текущее состояние машины.

        Returns:
            Имя состояния.
        """
        return self._state

    @property
    def steps(self) -> int:
        """Число успешно выполненных шагов.

        Returns:
            Неотрицательное целое число.
        """
        return self._steps

    @property
    def status(self) -> MachineStatus:
        """Текущий статус машины.

        Returns:
            :attr:`MachineStatus.HALTED`, если машина остановлена;
            :attr:`MachineStatus.NOT_STARTED`, если не сделано ни
            одного шага; иначе :attr:`MachineStatus.RUNNING`.
        """
        if self.halted:
            return MachineStatus.HALTED
        if self._steps == 0:
            return MachineStatus.NOT_STARTED
        return MachineStatus.RUNNING

    @property
    def halted(self) -> bool:
        """Признак остановки машины.

        Returns:
            ``True``, если машина в конечном состоянии или нет
            применимого правила.
        """
        if self._state in self._final_states:
            return True
        symbol: str = self._tape.read(self._head.position)
        return self._program.find(self._state, symbol) is None

    @property
    def alphabet(self) -> Alphabet:
        """Алфавит машины.

        Returns:
            Объект алфавита.
        """
        return self._alphabet

    @property
    def tape(self) -> UnboundedTape:
        """Лента машины.

        Returns:
            Объект ленты.
        """
        return self._tape

    @property
    def head(self) -> Head:
        """Каретка машины.

        Returns:
            Объект каретки.
        """
        return self._head

    @property
    def program(self) -> Program:
        """Программа машины.

        Returns:
            Объект программы.
        """
        return self._program

    # -----------------------------------------------------------------------
    # Public methods
    # -----------------------------------------------------------------------

    def step(self) -> bool:
        """Выполнить один шаг интерпретации.

        Returns:
            ``True``, если шаг был выполнен; ``False``, если машина
            остановилась.
        """
        if self._state in self._final_states:
            return False
        symbol: str = self._tape.read(self._head.position)
        rule: Transition | None = self._program.find(self._state, symbol)
        if rule is None:
            return False
        self._tape.write(self._head.position, rule.write_symbol)
        self._head.move(rule.direction)
        self._state = rule.next_state
        self._steps += 1
        return True

    def run(
        self,
        max_steps: int = DEFAULT_MAX_STEPS,
        on_step: Callable[[TuringMachine], None] | None = None,
    ) -> None:
        """Выполнять шаги до остановки или до лимита.

        Args:
            max_steps: Максимальное число шагов.
            on_step: Необязательный callback, вызываемый после
                каждого успешного шага.

        Returns:
            Ничего не возвращает.

        Raises:
            StepLimitExceeded: Если машина не остановилась за
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
        """Вернуть машину в начальное состояние.

        Returns:
            Ничего не возвращает.
        """
        self._tape = UnboundedTape(
            blank=self._tape.blank,
            initial=self._initial_tape,
        )
        self._head.reset(self._initial_head)
        self._state = self._initial_state
        self._steps = 0

    # -----------------------------------------------------------------------
    # Magic methods
    # -----------------------------------------------------------------------

    def __str__(self) -> str:
        """Вернуть JSON-представление машины.

        Returns:
            Строка с описанием начальной конфигурации машины.
        """
        data: dict[str, Any] = {
            "alphabet": list(self._alphabet),
            "blank": self._tape.blank,
            "initial_tape": self._initial_tape,
            "initial_head": self._initial_head,
            "initial_state": self._initial_state,
            "final_states": sorted(self._final_states),
            "transitions": [str(r) for r in self._program.rules],
        }
        return json.dumps(data, ensure_ascii=False, indent=2)