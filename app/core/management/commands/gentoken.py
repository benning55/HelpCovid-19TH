import string
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.core.management import BaseCommand, CommandError
from pprint import pprint
from core.models import User, RegisterToken
from django.contrib.auth.models import Group


def token_generator(size=10, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class Command(BaseCommand):
    """Django command to add db"""

    def handle(self, *args, **options):
        many = int(input("Please enter how many token you need: "))
        for _ in range(many):
            token = token_generator()
            RegisterToken.objects.create(
                token=token
            )
        print("Finish adding Token!")
