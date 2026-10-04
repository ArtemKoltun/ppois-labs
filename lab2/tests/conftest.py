"""
Общие фикстуры тестов.

Module: tests.conftest
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from pathlib import Path

import pytest

from common.domain.address import Address
from common.domain.money import Money
from common.enums.material_type import MaterialType
from common.enums.part_type import PartType
from factory.domain.materials.material import Material
from factory.domain.materials.supplier import Supplier
from factory.domain.parts.part import Part
from factory.domain.parts.specification import Specification
from common.enums.equipment_status import EquipmentStatus
from common.enums.order_status import OrderStatus
from factory.domain.equipment.equipment import Equipment
from factory.domain.equipment.machine import Machine
from factory.domain.management.department import Department
from factory.domain.personnel.employee import Employee
from factory.domain.workshops.workshop import Workshop
from factory.domain.orders.customer import Customer
from factory.domain.orders.order import Order
from factory.domain.orders.invoice import Invoice
from factory.domain.parts.part import Part
from factory.domain.documents.document import Document
from factory.domain.management.statistics import Statistics


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_EXAMPLES_ROOT: Path = (
    Path(__file__).resolve().parent.parent / "examples"
)
"""Корень папки с примерами."""


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def examples_root() -> Path:
    """Корень папки с примерами.

    Returns:
        Путь ``lab2/examples``.
    """
    return _EXAMPLES_ROOT


@pytest.fixture
def address() -> Address:
    """Адрес в Москве.

    Returns:
        Объект ``Address``.
    """
    return Address(
        country="Россия",
        city="Москва",
        street="Тверская",
        building="1",
        postal_code="101000",
    )


@pytest.fixture
def money() -> Money:
    """Денежная сумма 1000 RUB.

    Returns:
        Объект ``Money``.
    """
    return Money(amount=1000.0)


@pytest.fixture
def supplier(address: Address) -> Supplier:
    """Поставщик с рейтингом 4.5.

    Args:
        address: Фикстура адреса.

    Returns:
        Объект ``Supplier``.
    """
    return Supplier(
        name="МеталлПром",
        address=address,
        contact_person="Петров П.П.",
        phone="+7-900-000-00-00",
        rating=4.5,
    )


@pytest.fixture
def steel(supplier: Supplier) -> Material:
    """Материал «сталь».

    Args:
        supplier: Фикстура поставщика.

    Returns:
        Объект ``Material``.
    """
    return Material(
        name="Сталь 45",
        material_type=MaterialType.STEEL.value,
        density=7800.0,
        cost_per_kg=80.0,
    )


@pytest.fixture
def specification() -> Specification:
    """Спецификация детали.

    Returns:
        Объект ``Specification``.
    """
    return Specification(
        part_name="Поршень",
        tolerance=0.05,
        surface_finish="Ra 1.6",
        material_type="steel",
    )


@pytest.fixture
def piston_part(
    specification: Specification,
    steel: Material,
) -> Part:
    """Деталь «Поршень».

    Args:
        specification: Фикстура спецификации.
        steel: Фикстура материала.

    Returns:
        Объект ``Part``.
    """
    return Part(
        name="Поршень",
        part_type=PartType.PISTON,
        weight=1.5,
        specification=specification,
        material=steel,
    )


@pytest.fixture
def department() -> Department:
    """Общий отдел завода.

    Returns:
        Объект ``Department``.
    """
    return Department(name="Инженерный отдел")


@pytest.fixture
def workshop() -> Workshop:
    """Механический цех №1.

    Returns:
        Объект ``Workshop``.
    """
    return Workshop(
        name="Механический",
        number=1,
        area=500.0,
        workshop_head="Сидоров С.С.",
    )


@pytest.fixture
def employee(
    department: Department,
    workshop: Workshop,
) -> Employee:
    """Сотрудник «Иванов И.И.».

    Args:
        department: Фикстура отдела.
        workshop: Фикстура цеха.

    Returns:
        Объект ``Employee``.
    """
    return Employee(
        name="Иванов И.И.",
        position="Инженер",
        salary=Money(amount=80000.0),
        hire_date="2026-01-15",
        department=department,
        workshop=workshop,
    )


@pytest.fixture
def equipment(workshop: Workshop) -> Equipment:
    """Станок с инвентарным номером.

    Args:
        workshop: Фикстура цеха.

    Returns:
        Объект ``Equipment``.
    """
    return Equipment(
        name="Токарный 16К20",
        inventory_number="INV-001",
        purchase_year=2020,
        status=EquipmentStatus.IDLE,
    )


@pytest.fixture
def machine(equipment: Equipment) -> Machine:
    """Станок на основе оборудования.

    Args:
        equipment: Фикстура оборудования.

    Returns:
        Объект ``Machine``.
    """
    return Machine(
        equipment=equipment,
        power_kw=10.0,
        max_rpm=2000,
        accuracy_class="H",
    )


@pytest.fixture
def customer(address: Address) -> Customer:
    """Клиент ООО «АвтоПром».

    Args:
        address: Фикстура адреса.

    Returns:
        Объект ``Customer``.
    """
    return Customer(
        name="ООО АвтоПром",
        address=address,
        inn="7701234567",
        contact_person="Смирнов С.С.",
        phone="+7-495-000-00-00",
    )


@pytest.fixture
def order(
    customer: Customer,
    piston_part: Part,
) -> Order:
    """Заказ на 100 поршней.

    Args:
        customer: Фикстура клиента.
        piston_part: Фикстура детали.

    Returns:
        Объект ``Order``.
    """
    return Order(
        number="ORD-001",
        customer=customer,
        part=piston_part,
        quantity=100,
        price=Money(amount=500.0),
        deadline="2026-06-01",
        created_date="2026-01-15",
    )


@pytest.fixture
def invoice(order: Order, customer: Customer) -> Invoice:
    """Счёт на заказ.

    Args:
        order: Фикстура заказа.
        customer: Фикстура клиента.

    Returns:
        Объект ``Invoice``.
    """
    return Invoice(
        number="INV-001",
        order=order,
        customer=customer,
        amount=Money(amount=50000.0),
        issue_date="2026-01-20",
    )


@pytest.fixture
def document(employee: Employee) -> Document:
    """Базовый документ.

    Args:
        employee: Фикстура сотрудника.

    Returns:
        Объект ``Document``.
    """
    return Document(
        number="DOC-001",
        date="2026-02-01",
        author=employee,
        title="Технический документ",
    )


@pytest.fixture
def statistics() -> Statistics:
    """Статистика за январь 2026.

    Returns:
        Объект ``Statistics``.
    """
    return Statistics(period="2026-01", defects_count=0)
