
import factory

from .base import BaseUserFactory

from libs.core.models.users.dude import DudeUser


class DudeProfileFactory(factory.Factory):
    class Meta:
        model = dict

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class DudeUserFactory(BaseUserFactory):
    class Meta:
        model = DudeUser

    profile = factory.SubFactory(DudeProfileFactory)
