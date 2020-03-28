from collections import namedtuple

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser
from rest_framework.permissions import AllowAny
from core.models import User, Hospital

from accounts import serializers

Timeline = namedtuple('Timeline', ('hospital', 'user'))


@api_view(['POST', ])
@permission_classes([AllowAny, ])
@parser_classes([MultiPartParser])
def register(request, format=None):
    """
    Register for Officer the account and Hospital
    """
    if request.method == 'POST':
        data = request.data
        hospital = {
            'name': data['name'],
            'picture': request.FILES['picture'],
            'address': data['address'],
            'tel': data['hospital_tel'],
        }
        user = {
            'username': data['username'],
            'email': data['email'],
            'password': data['password'],
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'tel': data['user_tel']
        }
        timeline = {
            'hospital': hospital,
            'user': user
        }
        serializer = serializers.RegisterSerializer(data=timeline)
        if serializer.is_valid():
            new_hospital = Hospital.objects.create(
                name=hospital['name'],
                picture=hospital['picture'],
                address=hospital['address'],
                tel=hospital['tel']
            )
            new_user = User.objects.create(
                hospital_id=new_hospital.id,
                username=user['username'],
                email=user['email'],
                first_name=user['first_name'],
                last_name=user['last_name'],
                tel=user['tel']
            )
            new_user.set_password(user['password'])
            new_user.save()
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
