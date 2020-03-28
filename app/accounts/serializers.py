import django.contrib.auth.password_validation as validators
from django.core import exceptions
from rest_framework import serializers
from core.models import User, Hospital


class HospitalRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hospital
        fields = ('name', 'picture', 'address', 'tel')

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
        user = User(**data)

        password = data.get('password')
        errors = dict()

        try:
            validators.validate_password(password=password, user=User)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.message)

        if errors:
            raise serializers.ValidationError(errors)

        return data



class RegisterSerializer(serializers.Serializer):
    hospital = HospitalRegisterSerializer()
    user = UserRegisterSerializer()
