from rest_framework import serializers

from core.models import Need
from accounts.serializers import HospitalSerializer


class NeedSerializer(serializers.ModelSerializer):
    hospital_id = serializers.IntegerField(write_only=True)
    hospital = HospitalSerializer(required=False)

    class Meta:
        model = Need
        fields = ('id', 'hospital_id', 'hospital', 'title', 'description', 'picture', 'amount', 'status', 'created')
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
