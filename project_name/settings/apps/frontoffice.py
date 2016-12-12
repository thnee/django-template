
from ..base import *  # noqa


INSTALLED_APPS += [
    'apps.frontoffice',
]

ROOT_URLCONF = 'apps.frontoffice.urls'

AUTH_USER_MODEL = 'core.DudeUser'
