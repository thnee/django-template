
import os
import importlib


env = os.environ.get('DJANGO_SETTINGS_ENV')
app = os.environ.get('DJANGO_SETTINGS_APP')

module_paths = [
    'settings.base',
    'settings.envs.{env}'.format(env=env),
    'settings.apps.{app}'.format(app=app),
    'settings.allowed_hosts',
]

for module_path in module_paths:
    module = importlib.import_module(module_path)
    globals().update(module.__dict__)
