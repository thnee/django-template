
from ..base import *  # noqa


INSTALLED_APPS += [
    'django.contrib.admin',
    'apps.admin_site',
]

ROOT_URLCONF = 'apps.admin_site.urls'

AUTH_USER_MODEL = 'core.AdminUser'
