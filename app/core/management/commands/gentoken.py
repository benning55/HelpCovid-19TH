import string
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.core.management import BaseCommand, CommandError
from pprint import pprint
from core.models import User, RegisterToken, Location, Hospital
from django.contrib.auth.models import Group
import requests


def token_generator(size=10, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def get_position(name):
    """Get location"""
    response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={name}&key=AIzaSyCjsiYmer25q6yYO6SRMJZNJiMwMCp-BQ4')

    result = response.json()

    if result['status'] == 'ZERO_RESULTS':
        data = None
    else:
        locate = result['results'][0]['geometry']['location']

        data = [locate['lat'], locate['lng']]
    return data


class Command(BaseCommand):
    """Django command to add db"""

    def handle(self, *args, **options):
        hospitals = Hospital.objects.all()
        for hospital in hospitals:
            locate = get_position(hospital.name)
            if locate is None:
                continue
            else:
                Location.objects.update_or_create(
                    hospital_id=hospital.id,
                    latitude=locate[0],
                    longitude=locate[1]
                )
        print("Finish adding Location")
