from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, exceptions
from collections import namedtuple
from core.models import Need, Donator
from posts import serializers


@api_view(['GET', 'POST'])
@permission_classes([AllowAny, ])
def get_all_need(request, *args, **kwargs):
    """Get all the need"""
    if request.method == "GET":
        queryset = Need.objects.all().order_by('-id')
        # print(queryset)
        pk = kwargs.get('pk')
        if pk is None:
            serializer = serializers.NeedSerializer(queryset, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            queryset = queryset.filter(pk=pk)
            serializer = serializers.NeedSerializer(queryset, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == "POST":
        data = request.data
        hospital = data['hospital_id']
        queryset = Need.objects.all().filter(hospital_id=hospital)
        serializer = serializers.NeedSerializer(queryset, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST', 'PUT', ])
@permission_classes([IsAuthenticated, ])
@parser_classes([MultiPartParser])
def add_need(request, *args, **kwargs):
    """ Create new need """
    if request.method == "POST":
        user = request.user
        data = request.data
        try:
            payload = {
                'hospital_id': user.hospital.id,
                'title': data['title'],
                'description': data['description'],
                'picture': request.FILES['picture'],
                'amount': data['amount']
            }
        except:
            payload = {
                'hospital_id': user.hospital.id,
                'title': data['title'],
                'description': data['description'],
                'picture': None,
                'amount': data['amount']
            }
        serializer = serializers.NeedSerializer(data=payload)
        if serializer.is_valid():
            need = Need.objects.create(
                hospital_id=payload['hospital_id'],
                title=payload['title'],
                description=payload['description'],
                picture=payload['picture'],
                amount=payload['amount']
            )
            queryset = Need.objects.all().filter(pk=need.pk)
            show = serializers.NeedSerializer(queryset, many=True)
            return Response({'data': show.data}, status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        user = request.user
        data = request.data
        pk = kwargs.get('pk')
        if pk is None:
            return Response({'error': 'need an ID to update'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            hospital_id = user.hospital.id
            need = get_object_or_404(Need.objects.all(), pk=pk)
            if hospital_id != need.hospital.id:
                return Response({'error': 'You don''t have authorization'}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                serializer = serializers.NeedSerializer(instance=need, data=data, partial=True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data, status.HTTP_200_OK)
                return Response({"error": "cannot update"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', ])
@permission_classes([AllowAny, ])
def donate_need(request, *args, **kwargs):
    """ Donate for hospital need """
    if request.method == "GET":
        """ Get all donate record """
        queryset = Donator.objects.all().filter(approve_status=True)
        serialzer = serializers.DonatorSerializer(queryset, many=True)
        return Response({'data': serialzer.data}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        data = request.data
        payload = {
            'need_id': data['need_id'],
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'amount': data['amount'],
            'email': data['email'],
            'tel': data['tel'],
        }

        serializer = serializers.DonatorSerializer(data=payload)
        if serializer.is_valid(raise_exception=True):
            donate = Donator.objects.create(
                need_id=payload['need_id'],
                first_name=payload['first_name'],
                last_name=payload['last_name'],
                amount=payload['amount'],
                email=payload['email'],
                tel=payload['tel']
            )
            query = Donator.objects.all().filter(pk=donate.id)
            show = serializers.DonatorSerializer(query, many=True)
            return Response({'data': show.data}, status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
