# Лабораторная работа №2

## Тема

Крупный ООП-проект. Предметная область — **завод по изготовлению
автомобильных деталей**.

## Содержание

1. [Запуск](#запуск)
2. [Архитектура](#архитектура)
3. [Классы](#классы)
4. [Исключения](#исключения)
5. [Итоговая статистика](#итоговая-статистика)

## Запуск

Установка зависимостей: `pip install -e ".[dev]"`.

Прогон тестов: `pytest`.

Запуск приложения: `python main.py`.

## Архитектура

Проект разделён на слои:

- `common/` — общий код: ABC `Readable`/`Writable`, перечисления,
  value-объекты (`Address`, `Money`), исключения, виджеты меню.
- `factory/domain/` — доменные классы, разбитые по подпакетам:
  `parts`, `materials`, `equipment`, `workshops`, `personnel`,
  `orders`, `warehouse`, `documents`, `management`.
- `factory/io/` — парсеры и сериализаторы.
- `factory/ui/` — консольное меню.
- `main.py` — точка входа.

Домен не зависит от I/O и UI. Общий код (`common/`) используется
всеми модулями.

## Классы

### Детали (`factory.domain.parts`)

| Класс | Поля | Методы | Свойства | Ассоциации (связанные классы) |
|---|---|---|---|---|
| Part | 5 | 8 | 2 | Specification, Material |
| Piston | 3 | 3 | 0 | Part |
| Cylinder | 3 | 3 | 0 | Part |
| Shaft | 3 | 3 | 0 | Part |
| Gear | 3 | 3 | 0 | Part |
| Bearing | 3 | 3 | 0 | Part |
| Specification | 5 | 8 | 3 | — |

### Материалы (`factory.domain.materials`)

| Класс | Поля | Методы | Свойства | Ассоциации (связанные классы) |
|---|---|---|---|---|
| Material | 4 | 7 | 4 | Supplier |
| Steel | 2 | 3 | 0 | Material |
| Aluminum | 2 | 3 | 0 | Material |
| Plastic | 2 | 3 | 0 | Material |
| Supplier | 5 | 8 | 2 | Address |
| MaterialBatch | 4 | 8 | 3 | Material, Supplier |

### Оборудование (`factory.domain.equipment`)

| Класс | Поля | Методы | Свойства | Ассоциации (связанные классы) |
|---|---|---|---|---|
| Equipment | 5 | 10 | 3 | Workshop |
| Machine | 3 | 4 | 0 | Equipment |
| Lathe | 2 | 3 | 0 | Machine |
| MillingMachine | 2 | 3 | 0 | Machine |
| CNCMachine | 3 | 4 | 0 | Machine |
| MaintenanceRecord | 5 | 7 | 1 | Equipment, Employee |

### Цеха и производство (`factory.domain.workshops`)

| Класс | Поля | Методы | Свойства | Ассоциации (связанные классы) |
|---|---|---|---|---|
| Workshop | 5 | 10 | 2 | Employee |
| FoundryShop | 3 | 4 | 0 | Workshop |
| MachiningShop | 2 | 4 | 0 | Workshop |
| AssemblyShop | 2 | 4 | 0 | Workshop |
| ProductionProcess | 4 | 9 | 2 | Part, Workshop |
| ProductionOrder | 6 | 10 | 3 | Part, ProductionProcess |
| QualityInspection | 5 | 9 | 2 | Part |

### Персонал (`factory.domain.personnel`)

| Класс | Поля | Методы | Свойства | Ассоциации (связанные классы) |
|---|---|---|---|---|
| Employee | 7 | 10 | 4 | Department, Workshop, Money |
| Engineer | 3 | 4 | 0 | Employee |
| Technologist | 2 | 4 | 0 | Employee, ProductionProcess |
| Turner | 2 | 4 | 0 | Employee, Lathe |
| Foreman | 3 | 5 | 0 | Employee, Workshop |
| WorkShift | 4 | 10 | 1 | Employee |

### Заказы и клиенты (`factory.domain.orders`)

| Класс | Поля | Методы | Свойства | Ассоциации (связанные классы) |
|---|---|---|---|---|
| Customer | 5 | 7 | 2 | Address |
| Order | 9 | 11 | 4 | Customer, Part, Money |
| Contract | 6 | 8 | 2 | Customer, Money |
| Invoice | 6 | 8 | 3 | Order, Customer, Money |
| Payment | 4 | 7 | 2 | Invoice, Money |
| ProductionPlan | 4 | 10 | 2 | Order, Workshop |

### Склад (`factory.domain.warehouse`)

| Класс | Поля | Методы | Свойства | Ассоциации (связанные классы) |
|---|---|---|---|---|
| Warehouse | 6 | 11 | 3 | Address, Employee |
| RawMaterialWarehouse | 2 | 5 | 0 | Warehouse, Material |
| FinishedGoodsWarehouse | 2 | 5 | 0 | Warehouse, Part |
| StorageUnit | 4 | 9 | 2 | — |
| Batch | 5 | 8 | 2 | Part, MaterialBatch |

### Документы (`factory.domain.documents`)

| Класс | Поля | Методы | Свойства | Ассоциации (связанные классы) |
|---|---|---|---|---|
| Document | 4 | 7 | 3 | Employee |
| Drawing | 3 | 5 | 0 | Document, Part |
| QualityCertificate | 3 | 4 | 0 | Document, Part, QualityInspection |

### Управление (`factory.domain.management`)

| Класс | Поля | Методы | Свойства | Ассоциации (связанные классы) |
|---|---|---|---|---|
| Department | 3 | 8 | 1 | — |
| Factory | 6 | 14 | 2 | Workshop, Warehouse, Department, Order, Address |
| Statistics | 4 | 13 | 2 | Order, ProductionOrder |
| Report | 4 | 8 | 2 | Employee, Statistics |

### Общие доменные классы (`common.domain`)

| Класс | Поля | Методы | Свойства | Ассоциации (связанные классы) |
|---|---|---|---|---|
| Address | 5 | 6 | 5 | — |
| Money | 2 | 5 | 2 | — |

### Перечисления (`common.enums`)

| Перечисление | Значения | Используется в |
|---|---|---|
| OrderStatus | NEW, IN_PROGRESS, COMPLETED, SHIPPED, CANCELLED | Order, ProductionOrder |
| PartType | PISTON, CYLINDER, SHAFT, GEAR, BEARING | Part |
| MaterialType | STEEL, ALUMINUM, PLASTIC | Material |
| EquipmentStatus | WORKING, IDLE, BROKEN, MAINTENANCE | Equipment |

## Исключения

Пакет `common/exceptions/` содержит 12 классов исключений,
наследуемых от общего базового `FactoryException`:

| Класс | Описание |
|---|---|
| FactoryException | Базовое исключение всех модулей проекта |
| InvalidPartException | Некорректные данные детали |
| InvalidSpecificationException | Некорректная спецификация детали |
| QualityControlFailedException | Деталь не прошла контроль качества |
| InvalidMaterialException | Некорректные данные материала |
| InsufficientMaterialException | Недостаточно материала на складе |
| EquipmentBrokenException | Оборудование сломано |
| EquipmentNotAvailableException | Оборудование занято или недоступно |
| OrderNotFoundException | Заказ не найден |
| InvalidOrderException | Некорректные данные заказа |
| ProductionDeadlineMissedException | Срок производства заказа пропущен |
| EmployeeNotAvailableException | Сотрудник недоступен (отпуск, больничный) |

## Итоговая статистика

| Показатель | Требуется | Реализовано |
|---|---|---|
| Классы | ≥ 50 | 68 |
| Поля | ≥ 150 | 211 |
| Методы | ≥ 100 | 393 |
| Ассоциации | ≥ 30 | ~85 |
| Исключения | ≥ 12 | 12 |

Все количественные требования лабораторной работы выполнены
с запасом.

## Соответствие требованиям Lab 1

| Требование | Реализация |
|---|---|
| Инкапсуляция | Все поля приватные, доступ через свойства |
| Отделение UI от домена | Слои `domain/`, `io/`, `ui/` |
| Конструктор копирования | В Python копирование неявное, `__eq__`/`__hash__` переопределены |
| Освобождение ресурсов | Менеджер контекста в I/O |
| Сравнение на равенство | `__eq__` во всех доменных классах |
| Чтение/запись объекта | `Readable`/`Writable` (ABC) |
| Разделение интерфейса и реализации | ABC в `abstract/`, реализации в конкретных файлах |
| Документация Sphinx | `docs/conf.py`, `docs/api/*.rst` |
| Покрытие > 90% | `pytest --cov=src --cov-fail-under=90` |
| CLI/меню | `main.py` + `factory/ui/menu.py` |