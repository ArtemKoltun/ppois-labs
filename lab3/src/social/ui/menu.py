"""
Меню демонстрации социальной сети.

Module: social.ui.menu
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from __future__ import annotations

from common.enums.notification_type import NotificationType
from common.enums.post_visibility import PostVisibility
from common.ui.menu import Menu, MenuItem
from common.ui.prompts import ask_str
from social.domain.content.post import Post
from social.domain.messages.chat import Chat
from social.domain.messages.message import Message
from social.domain.notifications.notification import Notification
from social.domain.users.user import User

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class SocialSession:
    """Сессия демонстрации социальной сети.

    Attributes:
        _user: Текущий пользователь.
        _posts: Список постов.
        _chats: Список чатов.
        _notifications: Список уведомлений.
    """

    def __init__(self, user: User) -> None:
        """Создать сессию.

        Args:
            user: Текущий пользователь.
        """
        self._user: User = user
        self._posts: list[Post] = []
        self._chats: list[Chat] = []
        self._notifications: list[Notification] = []

    @property
    def user(self) -> User:
        """Текущий пользователь.

        Returns:
            Объект ``User``.
        """
        return self._user

    @property
    def posts(self) -> list[Post]:
        """Все посты.

        Returns:
            Список постов.
        """
        return self._posts

    @property
    def chats(self) -> list[Chat]:
        """Все чаты.

        Returns:
            Список чатов.
        """
        return self._chats

    @property
    def notifications(self) -> list[Notification]:
        """Все уведомления.

        Returns:
            Список уведомлений.
        """
        return self._notifications

    def add_post(self, post: Post) -> None:
        """Добавить пост.

        Args:
            post: Пост.

        Returns:
            Ничего не возвращает.
        """
        self._posts.append(post)

    def add_chat(self, chat: Chat) -> None:
        """Добавить чат.

        Args:
            chat: Чат.

        Returns:
            Ничего не возвращает.
        """
        self._chats.append(chat)

    def add_notification(self, notification: Notification) -> None:
        """Добавить уведомление.

        Args:
            notification: Уведомление.

        Returns:
            Ничего не возвращает.
        """
        self._notifications.append(notification)


# ---------------------------------------------------------------------------
# Public functions
# ---------------------------------------------------------------------------

def build_menu(session: SocialSession) -> Menu:
    """Собрать меню социальной сети.

    Args:
        session: Сессия демонстрации.

    Returns:
        Готовое меню.
    """
    def show_profile() -> None:
        _show_profile(session)

    def create_post() -> None:
        _create_post(session)

    def like_last_post() -> None:
        _like_last_post(session)

    def send_message() -> None:
        _send_message(session)

    def show_notifications() -> None:
        _show_notifications(session)

    items: list[MenuItem] = [
        MenuItem("Показать профиль", show_profile),
        MenuItem("Создать пост", create_post),
        MenuItem("Лайкнуть последний пост", like_last_post),
        MenuItem("Написать сообщение", send_message),
        MenuItem("Показать уведомления", show_notifications),
    ]
    return Menu("Социальная сеть", items)


# ---------------------------------------------------------------------------
# Private functions
# ---------------------------------------------------------------------------

def _show_profile(session: SocialSession) -> None:
    """Показать профиль пользователя.

    Args:
        session: Сессия.

    Returns:
        Ничего не возвращает.
    """
    user: User = session.user
    print()
    print(f"Пользователь: {user.display_name} (@{user.username})")
    print(f"Email: {user.email}")
    print(f"Роль: {user.role}")
    print(f"Активен: {user.is_active}")
    print(f"Заблокирован: {user.is_blocked}")
    print(f"Постов: {len(session.posts)}")
    print(f"Чатов: {len(session.chats)}")


def _create_post(session: SocialSession) -> None:
    """Создать новый пост.

    Args:
        session: Сессия.

    Returns:
        Ничего не возвращает.
    """
    text: str = ask_str("Текст поста: ")
    if not text:
        print("Текст не может быть пустым.")
        return
    visibility_raw: str = ask_str(
        "Видимость (public/friends/private): "
    )
    try:
        visibility: PostVisibility = PostVisibility(visibility_raw)
    except ValueError:
        print(f"Неизвестная видимость: {visibility_raw}")
        return
    try:
        post: Post = Post(
            author=session.user.username,
            text=text,
            visibility=visibility,
        )
    except Exception as exc:
        print(f"Ошибка: {exc}")
        return
    session.add_post(post)
    print(f"Пост создан. Всего постов: {len(session.posts)}")


def _like_last_post(session: SocialSession) -> None:
    """Поставить лайк последнему посту.

    Args:
        session: Сессия.

    Returns:
        Ничего не возвращает.
    """
    if not session.posts:
        print("Постов пока нет.")
        return
    post: Post = session.posts[-1]
    post.like()
    print(f"Лайк поставлен. У поста {post.likes_count} лайков.")


def _send_message(session: SocialSession) -> None:
    """Отправить сообщение пользователю.

    Args:
        session: Сессия.

    Returns:
        Ничего не возвращает.
    """
    recipient: str = ask_str("Кому (username): ")
    if not recipient:
        print("Имя получателя не может быть пустым.")
        return
    if recipient == session.user.username:
        print("Нельзя написать самому себе.")
        return
    text: str = ask_str("Текст: ")
    if not text:
        print("Текст не может быть пустым.")
        return
    chat: Chat = Chat(session.user.username, recipient)
    session.add_chat(chat)
    try:
        message: Message = Message(
            sender=session.user.username,
            chat_id=f"{session.user.username}:{recipient}",
            text=text,
        )
    except Exception as exc:
        print(f"Ошибка: {exc}")
        return
    chat.send()
    notification: Notification = Notification(
        recipient=recipient,
        notification_type=NotificationType.MESSAGE,
        text=f"Новое сообщение от {session.user.username}",
    )
    session.add_notification(notification)
    print(f"Сообщение отправлено: {message.text}")


def _show_notifications(session: SocialSession) -> None:
    """Показать уведомления.

    Args:
        session: Сессия.

    Returns:
        Ничего не возвращает.
    """
    if not session.notifications:
        print("Уведомлений нет.")
        return
    print(f"Всего уведомлений: {len(session.notifications)}")
    for index, notification in enumerate(
        session.notifications, start=1
    ):
        print(
            f"  {index}. [{notification.notification_type}] "
            f"{notification.text}"
        )
