
from django.db import models

from .base import BaseUserManager


class DudeUserMixin(object):
    pass


class DudeUserQuerySet(DudeUserMixin, models.QuerySet):
    pass


class DudeUserManager(DudeUserMixin, BaseUserManager):
    def get_queryset(self):
        return DudeUserQuerySet(self.model, using=self._db)
