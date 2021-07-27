import django.contrib.auth.password_validation as validators
from django.core import exceptions
from rest_framework import serializers
from core.models import User, Hospital, AboutMe, Location, LocationMaker, MoneyDonate
import requests


class HospitalSerializer(serializers.ModelSerializer):
    donated_money = serializers.SerializerMethodField()

    class Meta:
        model = Hospital
        fields = ('id', 'name', 'picture', 'address', 'donated_money', 'tel', 'bank_account_number', 'bank_account_name', 'bank_name')

    def get_donated_money(self, obj):
        total = 0
        transactions = MoneyDonate.objects.filter(hospital_id=obj.id, approve_status=True)
        for transaction in transactions:
            total += transaction.amount
        return total

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
        fields = ('name', 'picture', 'address', 'tel', 'bank_account_number', 'bank_account_name', 'bank_name')

    def validate(self, data):
        hospital = Hospital(**data)

        tel = data.get('tel')
        errors = dict()

        if len(tel) < 9 or len(tel) > 10:
            errors['tel'] = 'หมายเลขโทรศัพทร์ 9-10 ตัว'

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
        fields = ('username', 'password', 'letter', 'email', 'first_name', 'last_name', 'tel')

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
    position = serializers.SerializerMethodField(read_only=True, required=False)

    class Meta:
        model = Location
        fields = ('hospital_id', 'position')

    def get_position(self, obj):
        """Get location"""
        data = {
            'lat': float(obj.latitude),
            'lng': float(obj.longitude)
        }
        return data

class getLocationMakerSerializer(serializers.ModelSerializer):
    position = serializers.SerializerMethodField(read_only=True, required=False)

    class Meta:
        model = LocationMaker
        fields = ('maker_id', 'position')

    def get_position(self, obj):
        """Get location"""
        data = {
            'lat': float(obj.latitude),
            'lng': float(obj.longitude)
        }
        return data


class AboutMeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutMe
        fields = ('id', 'description')
