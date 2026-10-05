"""
Доменные классы сообщений и чатов.

Module: social.domain.messages
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from social.domain.messages.attachment import Attachment
from social.domain.messages.chat import Chat
from social.domain.messages.group_chat import GroupChat
from social.domain.messages.message import Message
from social.domain.messages.message_reaction import MessageReaction

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

__all__ = [
    "Attachment",
    "Chat",
    "GroupChat",
    "Message",
    "MessageReaction",
]
