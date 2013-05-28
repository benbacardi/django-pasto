"""Default Pasto-specific settings"""
from django.conf import settings

ALLOW_ANONYMOUS_POSTS = getattr(settings, 'PASTO_ALLOW_ANONYMOUS_POSTS', False)
