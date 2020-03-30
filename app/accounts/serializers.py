import django.contrib.auth.password_validation as validators
from django.core import exceptions
from rest_framework import serializers
from core.models import User, Hospital
import requests


class HospitalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hospital
        fields = ('id', 'name', 'picture', 'address', 'donated_money', 'tel', 'back_account_name', 'bank_name')


class UserSerializer(serializers.ModelSerializer):
    hospital = HospitalSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'hospital', 'email', 'first_name', 'last_name', 'tel')
        extra_kwargs = {
            'id': {'read_only': True}
        }


class HospitalRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hospital
        fields = ('name', 'picture', 'address', 'tel', 'bank_account_number', 'back_account_name', 'bank_name')

    def validate(self, data):
        hospital = Hospital(**data)

        tel = data.get('tel')
        errors = dict()

        if len(tel) < 9 or len(tel) > 10:
            errors['tel'] = 'The tel number must be 10 number'

        if errors:
            raise serializers.ValidationError(errors)

        return data


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'tel')

    def validate(self, data):
        # here data has all the fields which have validated values
        # so we can create a User instance out of it
        user = User(**data)

        # get the password from the data
        password = data.get('password')

        errors = dict()
        try:
            # validate the password and catch the exception
            validators.validate_password(password=password, user=User)

        # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super(UserRegisterSerializer, self).validate(data)



class RegisterSerializer(serializers.Serializer):
    hospital = HospitalRegisterSerializer()
    user = UserRegisterSerializer()


class getLocationSerializer(serializers.ModelSerializer):
    geolocation = serializers.SerializerMethodField(read_only=True, required=False)

    class Meta:
        model = Hospital
        fields = ('id', 'name', 'geolocation')

    def get_geolocation(self, obj):
        """Get location"""
        response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={obj.name}&key=AIzaSyCjsiYmer25q6yYO6SRMJZNJiMwMCp-BQ4')

        result = response.json()

        if result['status'] == 'ZERO_RESULTS':
            data = 'No position'
        else:
            locate = result['results'][0]['geometry']['location']

            data = {
                'lat': locate['lat'],
                'lng': locate['lng']
            }
        return data
