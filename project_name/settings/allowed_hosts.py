
import os


env = os.environ.get('DJANGO_SETTINGS_ENV')
app = os.environ.get('DJANGO_SETTINGS_APP')

hosts = {
    'stage': {
        'admin_site': [
            'some.domain',
        ],
        'backoffice': [
            'some.domain',
        ],
        'frontoffice': [
            'some.domain',
        ]
    },
    'prod': {
        'admin_site': [
            'some.domain',
        ],
        'backoffice': [
            'some.domain',
        ],
        'frontoffice': [
            'some.domain',
        ]
    }
}

if env == 'dev':
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = hosts[env][app]
