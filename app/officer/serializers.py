from django.shortcuts import get_object_or_404
from rest_framework import serializers
from posts.serializers import NeedSerializer
from accounts.serializers import HospitalSerializer
from core.models import Donator, MoneyDonate, Need, Hospital


class OfficerDonatorSerializer(serializers.ModelSerializer):
    need_id = serializers.IntegerField(write_only=True)
    need = NeedSerializer(required=False)

    class Meta:
        model = Donator
        fields = ('id', 'need_id', 'need', 'first_name', 'last_name', 'amount', 'email', 'tel', 'approve_status', 'created')
        extra_kwargs = {
            'id': {'read_only': True},
            'created': {'read_only': True},
            'need': {'read_only': True}
        }

    def update(self, instance, validated_data):
        need = get_object_or_404(Need.objects.all(), id=instance.need_id)
        instance.need_id = validated_data.get('need_id', instance.need_id)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.tel = validated_data.get('tel', instance.tel)
        if validated_data.get('approve_status') == instance.approve_status:
            instance.approve_status = validated_data.get('approve_status', instance.approve_status)
            instance.save()
            return instance
        else:
            if validated_data.get('approve_status'):
                current_need = need.amount
                left = current_need - instance.amount
                if left <= 0:
                    need.amount = 0
                    need.status = True
                else:
                    need.status = False
                    need.amount = left
                instance.approve_status = validated_data.get('approve_status', instance.approve_status)
                need.save()
            else:
                current_need = need.amount
                reform = current_need + instance.amount
                if reform >= need.base_amount:
                    need.amount = need.base_amount
                    need.status = False
                else:
                    need.status = False
                    need.amount = reform
                instance.approve_status = validated_data.get('approve_status', instance.approve_status)
                need.save()

            instance.save()
            return instance


class OfficerMoneyDonateSerializer(serializers.ModelSerializer):
    hospital = HospitalSerializer(required=False, read_only=True)
    hospital_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = MoneyDonate
        fields = ('id', 'hospital_id', 'hospital', 'first_name', 'last_name', 'receipt', 'amount', 'approve_status', 'created')
        extra_kwargs = {
            'id': {'read_only': True},
            'created': {'read_only': True}
        }

    def update(self, instance, validated_data):
        hospital = get_object_or_404(Hospital.objects.all(), id=instance.hospital_id)
        instance.hospital_id = validated_data.get('hospital_id', instance.hospital_id)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.receipt = validated_data.get('receipt', instance.receipt)
        instance.amount = validated_data.get('amount', instance.amount)
        if validated_data.get('approve_status') == instance.approve_status:
            instance.approve_status = validated_data.get('approve_status', instance.approve_status)
            instance.save()
            return instance
        else:
            total_donate_now = hospital.donated_money
            if validated_data.get('approve_status'):
                hospital.donated_money = total_donate_now + instance.amount
                instance.approve_status = validated_data.get('approve_status', instance.approve_status)
                hospital.save()
            else:
                hospital.donated_money = total_donate_now - instance.amount
                instance.approve_status = validated_data.get('approve_status', instance.approve_status)
                hospital.save()

            instance.save()
            return instance
