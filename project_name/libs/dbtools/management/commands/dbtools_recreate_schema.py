
from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Drop and recreate the public schema'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute('drop schema public cascade')
            cursor.execute('create schema public authorization {{ project_name }}')
