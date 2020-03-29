from django.shortcuts import get_object_or_404
from rest_framework import serializers

from core.models import Need, Donator, User
from accounts.serializers import HospitalSerializer


class NeedSerializer(serializers.ModelSerializer):
    hospital_id = serializers.IntegerField(write_only=True)
    hospital = HospitalSerializer(required=False)
    user = serializers.SerializerMethodField(read_only=True, required=False)
    class Meta:
        model = Need
        fields = ('id', 'hospital_id', 'hospital', 'title', 'description', 'picture', 'amount', 'status', 'created', 'user')
        extra_kwargs = {
            'id': {'read_only': True},
            'status': {'read_only': True},
            'created': {'read_only': True},
            'hospital': {'read_only': True}
        }

    def update(self, instance, validated_data):
        instance.hospital_id = validated_data.get('hospital_id', instance.hospital_id)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.picture = validated_data.get('picture', instance.picture)
        instance.amount = validated_data.get('amount', instance.amount)

        instance.save()
        return instance

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


class DonatorSerializer(serializers.ModelSerializer):
    need_id = serializers.IntegerField(write_only=True)
    need = NeedSerializer(required=False)

    class Meta:
        model = Donator
        fields = ('id', 'need_id', 'need', 'first_name', 'last_name', 'amount', 'email', 'tel', 'approve_status', 'created')
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
