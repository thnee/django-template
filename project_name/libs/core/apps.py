
from importlib import import_module

from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'libs.core'

    def import_models(self, *args, **kwargs):
        super().import_models(*args, **kwargs)
        self.models_module = import_module('libs.core.all_models')
