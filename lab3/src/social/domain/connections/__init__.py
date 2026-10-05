"""
Доменные классы связей.

Module: social.domain.connections
"""

from social.domain.connections.block_list import BlockList
from social.domain.connections.close_friends import CloseFriends
from social.domain.connections.follow import Follow
from social.domain.connections.friendship import Friendship
from social.domain.connections.subscription import Subscription

__all__ = [
    "BlockList",
    "CloseFriends",
    "Follow",
    "Friendship",
    "Subscription",
]
