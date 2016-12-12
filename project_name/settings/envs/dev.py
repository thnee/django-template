
from ..base import *  # noqa


DEBUG = True

SECRET_KEY = 'ywsup+3=+iyi^_zm49+ht!b^27)2b)mwr48igzjb$3w&c0%f(!'

INSTALLED_APPS += [
    'libs.dbtools',
]

DATABASES['default']['HOST'] = 'postgres'
DATABASES['default']['USER'] = '{{ project_name }}'
DATABASES['default']['PASSWORD'] = '{{ project_name }}'
DATABASES['default']['NAME'] = '{{ project_name }}'
