# Лабораторная работа №3

## Тема

Крупный ООП-проект на новой предметной области. Домен —
**социальная сеть**.

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

- `common/` — общий код: ABC `Readable`/`Writable`, перечисления
  (`UserRole`, `PostVisibility`, `NotificationType`, `ReportStatus`),
  исключения, виджеты консольного меню.
- `social/domain/` — доменные классы, разбитые по подпакетам:
  `users`, `content`, `messages`, `communities`, `media`,
  `notifications`, `moderation`, `connections`, `ads`, `technical`.
- `social/io/` — парсеры и сериализаторы.
- `social/ui/` — консольное меню.
- `main.py` — точка входа.

Домен не зависит от I/O и UI. Общий код (`common/`) используется
всеми модулями.

## Классы

### Пользователи (`social.domain.users`)

| Класс | Поля | Методы | Свойства | Ассоциации (связанные классы) |
|---|---|---|---|---|
| User | 6 | 16 | 6 | Profile, Account, UserRole |
| Profile | 5 | 10 | 5 | — |
| Account | 4 | 11 | 3 | — |
| UserSettings | 4 | 10 | 4 | PostVisibility |
| Verification | 4 | 9 | 3 | — |
| FriendRequest | 5 | 9 | 5 | FriendshipError |

### Контент (`social.domain.content`)

| Класс | Поля | Методы | Свойства | Ассоциации (связанные классы) |
|---|---|---|---|---|
| Post | 6 | 12 | 5 | PostVisibility |
| Photo | 4 | 7 | 2 | — |
| Video | 5 | 8 | 3 | — |
| Story | 4 | 7 | 3 | — |
| Comment | 4 | 8 | 3 | — |
| Reaction | 3 | 7 | 2 | — |
| Hashtag | 3 | 9 | 2 | — |

### Сообщения (`social.domain.messages`)

| Класс | Поля | Методы | Свойства | Ассоциации (связанные классы) |
|---|---|---|---|---|
| Chat | 5 | 13 | 4 | — |
| Message | 5 | 11 | 4 | — |
| GroupChat | 3 | 7 | 2 | Chat |
| Attachment | 4 | 8 | 4 | — |
| MessageReaction | 3 | 7 | 2 | — |

### Сообщества (`social.domain.communities`)

| Класс | Поля | Методы | Свойства | Ассоциации (связанные классы) |
|---|---|---|---|---|
| Community | 5 | 11 | 4 | — |
| Group | 3 | 6 | 2 | Community |
| Page | 3 | 5 | 1 | Community |
| GroupMember | 4 | 9 | 2 | GroupRole |
| GroupRole | 3 | 9 | 1 | — |
| Event | 6 | 10 | 3 | — |

### Медиа (`social.domain.media`)

| Класс | Поля | Методы | Свойства | Ассоциации (связанные классы) |
|---|---|---|---|---|
| MediaFile | 5 | 9 | 5 | — |
| Album | 4 | 10 | 3 | MediaFile |
| Mention | 3 | 6 | 3 | — |

### Уведомления (`social.domain.notifications`)

| Класс | Поля | Методы | Свойства | Ассоциации (связанные классы) |
|---|---|---|---|---|
| Notification | 5 | 8 | 5 | NotificationType |
| PushNotification | 2 | 4 | 1 | Notification |
| EmailNotification | 2 | 3 | 2 | Notification |
| NotificationSettings | 4 | 10 | 1 | — |

### Модерация (`social.domain.moderation`)

| Класс | Поля | Методы | Свойства | Ассоциации (связанные классы) |
|---|---|---|---|---|
| Moderator | 4 | 10 | 3 | — |
| Report | 5 | 10 | 3 | ReportStatus |
| Ban | 4 | 8 | 4 | — |
| Warning | 4 | 7 | 4 | — |
| Appeal | 4 | 8 | 3 | — |

### Связи (`social.domain.connections`)

| Класс | Поля | Методы | Свойства | Ассоциации (связанные классы) |
|---|---|---|---|---|
| Friendship | 4 | 9 | 3 | — |
| Follow | 3 | 8 | 3 | — |
| Subscription | 4 | 8 | 3 | — |
| BlockList | 3 | 10 | 1 | — |
| CloseFriends | 3 | 10 | 1 | — |

### Реклама (`social.domain.ads`)

| Класс | Поля | Методы | Свойства | Ассоциации (связанные классы) |
|---|---|---|---|---|
| Advertisement | 6 | 12 | 4 | — |
| AdCampaign | 5 | 11 | 2 | Advertisement |
| Analytics | 5 | 11 | 2 | — |
| AudienceSegment | 4 | 8 | 2 | — |
| Statistics | 4 | 10 | 1 | Advertisement |

### Технические (`social.domain.technical`)

| Класс | Поля | Методы | Свойства | Ассоциации (связанные классы) |
|---|---|---|---|---|
| Session | 4 | 9 | 2 | Device |
| Device | 4 | 9 | 2 | — |
| Location | 4 | 8 | 2 | — |
| ActivityLog | 3 | 10 | 1 | — |

### Перечисления (`common.enums`)

| Перечисление | Значения | Используется в |
|---|---|---|
| UserRole | USER, MODERATOR, ADMIN, ADVERTISER | User |
| PostVisibility | PUBLIC, FRIENDS, CLOSE_FRIENDS, PRIVATE | Post, UserSettings |
| NotificationType | LIKE, COMMENT, FRIEND_REQUEST, MESSAGE, MENTION, SYSTEM | Notification |
| ReportStatus | PENDING, IN_REVIEW, RESOLVED, REJECTED | Report |

## Исключения

Пакет `common/exceptions/` содержит 12 классов исключений,
наследуемых от общего базового `SocialNetworkError`:

| Класс | Описание |
|---|---|
| SocialNetworkError | Базовое исключение всех модулей проекта |
| InvalidUserError | Некорректные данные пользователя |
| UserNotFoundError | Пользователь не найден |
| InvalidCredentialsError | Неверные логин или пароль |
| AccountBlockedError | Аккаунт заблокирован |
| InvalidPostError | Некорректный пост |
| ContentModerationError | Ошибка модерации контента |
| PrivacyViolationError | Нарушение приватности |
| FriendshipError | Ошибка при работе с дружбой |
| MessageDeliveryError | Ошибка доставки сообщения |
| NotificationError | Ошибка при работе с уведомлениями |
| AdCampaignError | Ошибка рекламной кампании |

## Итоговая статистика

| Показатель | Требуется | Реализовано |
|---|---|---|
| Классы | ≥ 50 | 50 + 12 = 62 |
| Поля | ≥ 150 | 203 |
| Методы | ≥ 100 | 445 |
| Свойства | — | 141 |
| Ассоциации | ≥ 30 | ~50 |
| Исключения | ≥ 12 | 12 |

Все количественные требования лабораторной работы выполнены
с запасом.

## Соответствие требованиям

| Требование | Реализация |
|---|---|
| Инкапсуляция | Все поля приватные, доступ через свойства |
| Отделение UI от домена | Слои `domain/`, `io/`, `ui/` |
| Конструктор копирования | В Python копирование неявное, `__eq__`/`__hash__` переопределены |
| Освобождение ресурсов | Менеджер контекста в I/O |
| Сравнение на равенство | `__eq__` во всех доменных классах |
| Чтение/запись объекта | `Readable`/`Writable` (ABC) |
| Разделение интерфейса и реализации | ABC в `common/abstract/`, реализации в конкретных файлах |
| Документация Sphinx | `docs/conf.py`, `docs/api/*.rst` |
| Покрытие > 90% | `pytest --cov=src --cov-fail-under=90` |
| CLI/меню | `main.py` + `social/ui/menu.py` |