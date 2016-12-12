
from django.core.management.base import BaseCommand

from libs.core.factories.users.admin import AdminUserFactory
from libs.core.factories.users.dude import DudeUserFactory


class Command(BaseCommand):
    help = 'Populate database with some useful data for development or staging'

    def handle(self, *args, **options):
        AdminUserFactory(
            email='admin@example.com',
            password='password',
        )
        DudeUserFactory(
            email='dude@example.com',
            password='password',
        )
