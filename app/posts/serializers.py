from django.shortcuts import get_object_or_404
from rest_framework import serializers

from core.models import Need, Donator, User, MoneyDonate
from accounts.serializers import HospitalSerializer


class NeedSerializer(serializers.ModelSerializer):
    hospital_id = serializers.IntegerField(write_only=True)
    hospital = HospitalSerializer(required=False)
    category_id = serializers.IntegerField(write_only=True)
    user = serializers.SerializerMethodField(read_only=True, required=False)
    total_donation = serializers.SerializerMethodField(read_only=True, required=False)

    class Meta:
        model = Need
        fields = ('id', 'hospital_id', 'hospital', 'title', 'category_id', 'description', 'picture', 'amount', 'base_amount', 'status', 'created', 'user', 'total_donation')
        extra_kwargs = {
            'id': {'read_only': True},
            'status': {'read_only': True},
            'created': {'read_only': True},
            'hospital': {'read_only': True},
            'base_amount': {'read_only': True}
        }

    def update(self, instance, validated_data):
        instance.hospital_id = validated_data.get('hospital_id', instance.hospital_id)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.picture = validated_data.get('picture', instance.picture)
        instance.base_amount = validated_data.get('amount', instance.amount)

        if instance.amount < instance.base_amount:
            instance.status = False
        else:
            instance.status = True

        instance.save()
        return instance

    def create(self, validated_data):
        need = Need.objects.create(
            hospital_id=validated_data.get('hospital_id'),
            category_id=validated_data.get('category_id'),
            title=validated_data.get('title'),
            description=validated_data.get('description'),
            picture=validated_data.get('picture'),
            amount=validated_data.get('amount'),
            base_amount=validated_data.get('amount')
        )

        return need

    def get_user(self, obj):
        hospital_id = obj.hospital_id
        users = User.objects.all().filter(hospital_id=hospital_id)
        pick = users.first()
        payload = {
            'first_name': pick.first_name,
            'last_name': pick.last_name,
            'tel': pick.tel,
            'email': pick.email
        }

        return payload

    def get_total_donation(self, obj):
        donation = Donator.objects.all().filter(need_id=obj.id, approve_status=True)
        total_amount = 0
        for amount in donation:
            total_amount += amount.amount
        return total_amount


class DonatorSerializer(serializers.ModelSerializer):
    need_id = serializers.IntegerField(write_only=True)
    need = NeedSerializer(required=False)

    class Meta:
        model = Donator
        fields = ('id', 'need_id', 'need', 'first_name', 'last_name', 'company_name', 'tax_id', 'amount', 'email', 'tel', 'approve_status', 'created')
        extra_kwargs = {
            'id': {'read_only': True},
            'approve_status': {'read_only': True},
            'created': {'read_only': True},
            'need': {'read_only': True}
        }

    def validate(self, data):
        donator = Donator(**data)

        tel = data.get('tel')
        errors = dict()

        if len(tel) < 9 or len(tel) > 10:
            errors['tel'] = 'The tel number must be 10 number'

        if errors:
            raise serializers.ValidationError(errors)

        return data

    def create(self, validated_data):
        donator = Donator.objects.create(
            need_id=validated_data.get('need_id'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            company_name=validated_data.get('company_name', None),
            tax_id=validated_data.get('tax_id', None),
            amount=validated_data.get('amount'),
            email=validated_data.get('email', None),
            tel=validated_data.get('tel')
        )

        return donator


class MoneyDonateSerializer(serializers.ModelSerializer):
    hospital = HospitalSerializer(required=False, read_only=True)
    hospital_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = MoneyDonate
        fields = ('id', 'hospital_id', 'hospital', 'first_name', 'last_name', 'company_name', 'tax_id', 'receipt', 'amount', 'email', 'tel', 'approve_status', 'created')
        extra_kwargs = {
            'id': {'read_only': True},
            'approve_status': {'read_only': True},
            'created': {'read_only': True}
        }

    def create(self, validated_data):
        donator = MoneyDonate.objects.create(
            hospital_id=validated_data.get('hospital_id'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            company_name=validated_data.get('company_name', None),
            tax_id=validated_data.get('tax_id', None),
            receipt=validated_data.get('receipt'),
            amount=validated_data.get('amount'),
            email=validated_data.get('email', None),
            tel=validated_data.get('tel', None)
        )

        return donator
