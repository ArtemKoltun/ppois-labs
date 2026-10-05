"""
Доменные классы рекламы.

Module: social.domain.ads
"""

from social.domain.ads.ad_campaign import AdCampaign
from social.domain.ads.advertisement import Advertisement
from social.domain.ads.analytics import Analytics
from social.domain.ads.audience_segment import AudienceSegment
from social.domain.ads.statistics import Statistics

__all__ = [
    "AdCampaign",
    "Advertisement",
    "Analytics",
    "AudienceSegment",
    "Statistics",
]
