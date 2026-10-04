"""
Меню демонстрации работы завода.

Module: factory.ui.menu
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.domain.money import Money
from common.enums.material_type import MaterialType
from common.enums.part_type import PartType
from common.ui.menu import Menu, MenuItem
from common.ui.prompts import ask_float, ask_int, ask_str
from factory.domain.management.department import Department
from factory.domain.management.factory import Factory
from factory.domain.materials.material import Material
from factory.domain.parts.part import Part
from factory.domain.parts.specification import Specification
from factory.domain.personnel.employee import Employee
from factory.domain.workshops.workshop import Workshop

# ---------------------------------------------------------------------------
# Public functions
# ---------------------------------------------------------------------------

def build_menu(factory: Factory) -> Menu:
    """Собрать меню для завода.

    Args:
        factory: Объект завода.

    Returns:
        Готовое меню.
    """
    def show_info() -> None:
        _print_factory_info(factory)

    def add_workshop() -> None:
        _add_workshop(factory)

    def add_employee() -> None:
        _add_employee(factory)

    def add_material() -> None:
        _add_material(factory)

    def add_part() -> None:
        _add_part(factory)

    items: list[MenuItem] = [
        MenuItem("Показать информацию о заводе", show_info),
        MenuItem("Добавить цех", add_workshop),
        MenuItem("Нанять сотрудника", add_employee),
        MenuItem("Принять материал", add_material),
        MenuItem("Выпустить деталь", add_part),
    ]
    return Menu("Завод автомобильных деталей", items)


# ---------------------------------------------------------------------------
# Private functions
# ---------------------------------------------------------------------------

def _print_factory_info(factory: Factory) -> None:
    """Напечатать информацию о заводе.

    Args:
        factory: Завод.

    Returns:
        Ничего не возвращает.
    """
    print()
    print(f"Завод: {factory.name}")
    print(f"Адрес: {factory.address.full()}")
    print(f"Цехов: {factory.workshops_count()}")
    print(f"Складов: {factory.warehouses_count()}")
    print(f"Отделов: {factory.departments_count()}")
    print(f"Заказов: {factory.orders_count()}")


def _add_workshop(factory: Factory) -> None:
    """Запросить данные цеха и добавить его.

    Args:
        factory: Завод.

    Returns:
        Ничего не возвращает.
    """
    name: str = ask_str("Название цеха: ")
    if not name:
        print("Название не может быть пустым.")
        return
    number: int = ask_int("Номер цеха [1-999]: ", 1, 999)
    area: float = ask_float("Площадь (м²): ")
    workshop: Workshop = Workshop(
        name=name, number=number, area=area,
    )
    factory.add_workshop(workshop)
    print(f"Цех «{name}» добавлен.")


def _add_employee(factory: Factory) -> None:
    """Запросить данные сотрудника и добавить его.

    Args:
        factory: Завод.

    Returns:
        Ничего не возвращает.
    """
    department: Department = Department(name="Общий отдел")
    if factory.departments_count() == 0:
        factory.add_department(department)
    name: str = ask_str("ФИО: ")
    position: str = ask_str("Должность: ")
    salary: float = ask_float("Оклад: ")
    employee: Employee = Employee(
        name=name,
        position=position,
        salary=Money(amount=salary),
        hire_date="2026-01-01",
        department=department,
    )
    department.add_employee()
    print(f"Сотрудник «{employee.name}» принят.")


def _add_material(factory: Factory) -> None:
    """Запросить данные материала и создать партию.

    Args:
        factory: Завод.

    Returns:
        Ничего не возвращает.
    """
    name: str = ask_str("Название материала: ")
    material_type: str = ask_str(
        "Тип (steel/aluminum/plastic): "
    )
    density: float = ask_float("Плотность (кг/м³): ")
    cost: float = ask_float("Цена за кг: ")
    try:
        material: Material = Material(
            name=name,
            material_type=material_type,
            density=density,
            cost_per_kg=cost,
        )
    except Exception as exc:
        print(f"Ошибка: {exc}")
        return
    print(f"Материал «{material.name}» зарегистрирован.")


def _add_part(factory: Factory) -> None:
    """Запросить данные детали и создать её.

    Args:
        factory: Завод.

    Returns:
        Ничего не возвращает.
    """
    name: str = ask_str("Название детали: ")
    part_type_raw: str = ask_str(
        "Тип (piston/cylinder/shaft/gear/bearing): "
    )
    weight: float = ask_float("Вес (кг): ")
    try:
        part_type: PartType = PartType(part_type_raw)
    except ValueError:
        print(f"Неизвестный тип детали: {part_type_raw}")
        return
    material: Material = Material(
        name="steel_default",
        material_type=MaterialType.STEEL.value,
        density=7800.0,
        cost_per_kg=80.0,
    )
    spec: Specification = Specification(part_name=name)
    try:
        part: Part = Part(
            name=name,
            part_type=part_type,
            weight=weight,
            specification=spec,
            material=material,
        )
    except Exception as exc:
        print(f"Ошибка: {exc}")
        return
    cost: float = part.calculate_cost()
    print(
        f"Деталь «{part.name}» ({part_type}) создана. "
        f"Стоимость: {cost:.2f} руб."
    )
