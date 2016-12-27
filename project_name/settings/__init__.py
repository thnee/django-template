
import os
import importlib


env = os.environ.get('DJANGO_SETTINGS_ENV')
app = os.environ.get('DJANGO_SETTINGS_APP')

module_paths = []

module_paths.append('settings.base')

if env:
    module_paths.append('settings.envs.{env}'.format(env=env))

if app:
    module_paths.append('settings.apps.{app}'.format(app=app))

module_paths.append('settings.allowed_hosts')


for module_path in module_paths:
    module = importlib.import_module(module_path)
    globals().update(module.__dict__)
