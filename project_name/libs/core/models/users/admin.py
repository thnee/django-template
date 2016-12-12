
from django.contrib.postgres.fields import JSONField

from libs.auth.permissions import FakeAdminPermissionsMixin

from ...managers.users.admin import AdminUserManager
from .base import BaseUser


class AdminUser(FakeAdminPermissionsMixin, BaseUser):
    class Meta:
        db_table = 'core_AdminUser'

    objects = AdminUserManager()

    profile = JSONField(default={})

    def get_short_name(self):
        return self.profile['first_name']

    def get_full_name(self):
        return '{first_name} {last_name}'.format(**self.profile)
