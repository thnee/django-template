
from django.contrib.postgres.fields import JSONField

from ...managers.users.dude import DudeUserManager
from .base import BaseUser


class DudeUser(BaseUser):
    class Meta:
        db_table = 'core_DudeUser'

    objects = DudeUserManager()

    profile = JSONField(default={})

    def get_short_name(self):
        return self.profile['first_name']

    def get_full_name(self):
        return '{first_name} {last_name}'.format(**self.profile)
