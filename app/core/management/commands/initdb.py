from abc import ABC

from django.core.management import BaseCommand, CommandError
from core.models import User
from django.contrib.auth.models import Group


class Command(BaseCommand):
    """Django command to add db"""

    def handle(self, *args, **options):
        users = User.objects.all()
        if users.count() < 1:
            self.stdout.write("Create Super User")
            User.objects.create_superuser(
                username='admin',
                email='test@gmail.com',
                password='admin@kmitl'
            ).save()
        else:
            self.stdout.write("Already have super user")
