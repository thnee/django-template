
from django.db import models

from .base import BaseUserManager


class AdminUserMixin(object):
    pass


class AdminUserQuerySet(AdminUserMixin, models.QuerySet):
    pass


class AdminUserManager(AdminUserMixin, BaseUserManager):
    def get_queryset(self):
        return AdminUserQuerySet(self.model, using=self._db)
