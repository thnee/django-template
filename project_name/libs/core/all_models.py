
"""
Used by apps.CoreConfig to define which models are available in this app.
Just add all new models here. Don't import from here.
"""

from .models.users.admin import AdminUser  # noqa
from .models.users.dude import DudeUser  # noqa
