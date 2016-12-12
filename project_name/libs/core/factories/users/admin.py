
import factory

from .base import BaseUserFactory

from libs.core.models.users.admin import AdminUser


class AdminProfileFactory(factory.Factory):
    class Meta:
        model = dict

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class AdminUserFactory(BaseUserFactory):
    class Meta:
        model = AdminUser

    profile = factory.SubFactory(AdminProfileFactory)
