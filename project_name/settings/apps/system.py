
from ..base import *  # noqa


INSTALLED_APPS += [
    'django.contrib.admin',
    'apps.admin_site',
    'apps.backoffice',
    'apps.frontoffice',
]

ROOT_URLCONF = 'apps.system.urls'
