
from ..base import *  # noqa


DEBUG = False

SECRET_KEY = 'changeme'

DATABASES['default']['HOST'] = 'changeme'
DATABASES['default']['USER'] = '{{ project_name }}'
DATABASES['default']['PASSWORD'] = 'changeme'
DATABASES['default']['NAME'] = '{{ project_name }}'
