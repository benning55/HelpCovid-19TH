from rest_framework import serializers
from core.models import PopUp, ProductMaker


class PopUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = PopUp
        fields = ('id', 'picture', 'description')
        extra_kwargs = {
            'id': {'read_only': True},
            'picture': {'read_only': True},
            'description': {'read_only': True}
        }


class ProductMakerSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductMaker
        fields = ('id', 'title', 'description', 'picture', 'company', 'tel', 'email')
        extra_kwargs = {
            'id': {'read_only': True},
            'title': {'read_only': True},
            'picture': {'read_only': True},
            'description': {'read_only': True},
            'company': {'read_only': True},
            'tel': {'read_only': True},
            'email': {'read_only': True}
        }
