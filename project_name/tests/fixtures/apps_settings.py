
import importlib

import pytest


def load_settings(app_name, settings):
    APP_SETTINGS = [
        'INSTALLED_APPS',
        'ROOT_URLCONF',
        'AUTH_USER_MODEL',
    ]

    module_name = 'settings.apps.{app_name}'.format(app_name=app_name)
    app_settings = importlib.import_module(module_name)

    for setting in APP_SETTINGS:
        setattr(settings, setting, getattr(app_settings, setting))


@pytest.fixture
def frontoffice_app(settings):
    load_settings('frontoffice', settings)


@pytest.fixture
def backoffice_app(settings):
    load_settings('backoffice', settings)
