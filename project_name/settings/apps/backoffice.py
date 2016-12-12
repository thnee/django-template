
from ..base import *  # noqa


INSTALLED_APPS += [
    'apps.backoffice',
]

ROOT_URLCONF = 'apps.backoffice.urls'

AUTH_USER_MODEL = 'core.AdminUser'
