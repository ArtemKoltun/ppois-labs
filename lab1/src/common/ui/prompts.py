"""
Функции ввода с валидацией для консольного интерфейса.

Module: common.ui.prompts
"""

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_YES_ANSWERS: frozenset[str] = frozenset(
    {"y", "yes", "д", "да"}
)
"""Ответы, означающие согласие."""

_NO_ANSWERS: frozenset[str] = frozenset(
    {"n", "no", "н", "нет"}
)
"""Ответы, означающие отказ."""


# ---------------------------------------------------------------------------
# Public functions
# ---------------------------------------------------------------------------

def ask_str(prompt: str) -> str:
    """Запросить у пользователя строку.

    Args:
        prompt: Текст приглашения.

    Returns:
        Введённая строка без крайних пробелов.
    """
    return input(prompt).strip()


def ask_int(prompt: str, minimum: int, maximum: int) -> int:
    """Запросить у пользователя целое число в диапазоне.

    Повторяет запрос, пока не будет введено корректное значение.

    Args:
        prompt: Текст приглашения.
        minimum: Минимально допустимое значение.
        maximum: Максимально допустимое значение.

    Returns:
        Введённое число.
    """
    while True:
        raw: str = input(prompt).strip()
        value: int | None = _try_parse_int(raw)
        if value is None:
            print(
                f"Введите целое число от {minimum} до {maximum}."
            )
            continue
        if not minimum <= value <= maximum:
            print(
                f"Число должно быть от {minimum} до {maximum}."
            )
            continue
        return value


def confirm(prompt: str) -> bool:
    """Запросить подтверждение у пользователя.

    Повторяет запрос, пока не будет введён один из вариантов
    «да» или «нет».

    Args:
        prompt: Текст вопроса.

    Returns:
        ``True`` для согласия, ``False`` для отказа.
    """
    while True:
        raw: str = input(f"{prompt} [y/n]: ").strip().lower()
        if raw in _YES_ANSWERS:
            return True
        if raw in _NO_ANSWERS:
            return False
        print("Ответьте 'y' или 'n'.")


# ---------------------------------------------------------------------------
# Private functions
# ---------------------------------------------------------------------------

def _try_parse_int(text: str) -> int | None:
    """Попробовать разобрать строку как целое число.

    Args:
        text: Проверяемая строка.

    Returns:
        Число или ``None``, если строка не является числом.
    """
    try:
        return int(text)
    except ValueError:
        return None
