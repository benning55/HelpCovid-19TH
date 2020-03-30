from collections import namedtuple

from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from core.models import Donator, MoneyDonate
from officer import serializers


@api_view(['GET', 'PUT', ])
@permission_classes([IsAuthenticated, ])
def officer_donation(request, *args, **kwargs):
    """
    all donation that need to be aprrove
    """
    if request.method == "GET":
        pk = kwargs.get('pk')
        user = request.user
        if pk is None:
            queryset = Donator.objects.all().filter(need__hospital_id=user.hospital_id).order_by('-created')
            serializer = serializers.OfficerDonatorSerializer(queryset, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            queryset = Donator.objects.all().filter(need_id=pk).order_by('-created')
            serializer = serializers.OfficerDonatorSerializer(queryset, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == "POST":
        data = request.data
        user = request.user
        queryset = Donator.objects.all().filter(need_hospital_id=user.hospital_id, approve_status=data['approve_status'])
        serializer = serializers.OfficerDonatorSerializer(queryset, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        user = request.user
        data = request.data
        donator = get_object_or_404(Donator.objects.all(), pk=data['id'])
        if user.hospital_id != donator.need.hospital_id:
            return Response({"error": 'You don''t have authorize'}, status=status.HTTP_401_UNAUTHORIZED)
        payload = {
            'approve_status': data['approve_status']
        }
        serializer = serializers.OfficerDonatorSerializer(instance=donator, data=payload, partial=True)
        if serializer.is_valid(raise_exception=True):
            test = serializer.save()
        return Response({"update": serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'PUT', ])
@permission_classes([IsAuthenticated, ])
def officer_donation_money(request, *args, **kwargs):
    """
    all money that need to be approve
    """
    if request.method == "GET":
        pk = kwargs.get('pk')
        user = request.user
        if pk is None:
            queryset = MoneyDonate.objects.all().filter(hospital_id=user.hospital_id).order_by('-created')
            serializer = serializers.OfficerMoneyDonateSerializer(queryset, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            queryset = MoneyDonate.objects.all().filter(hospital_id=pk).order_by('-created')
            serializer = serializers.OfficerMoneyDonateSerializer(queryset, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == "POST":
        data = request.data
        user = request.user
        queryset = MoneyDonate.objects.all().filter(hospital_id=user.hospital_id, approve_status=data['approve_status'])
        serializer = serializers.OfficerMoneyDonateSerializer(queryset, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        user = request.user
        data = request.data
        moneydonate = get_object_or_404(MoneyDonate.objects.all(), pk=data['id'])
        if user.hospital_id != moneydonate.hospital_id:
            return Response({"error": 'You don''t have authorize'}, status=status.HTTP_401_UNAUTHORIZED)
        payload = {
            'approve_status': data['approve_status']
        }
        serializer = serializers.OfficerMoneyDonateSerializer(instance=moneydonate, data=payload, partial=True)
        if serializer.is_valid(raise_exception=True):
            test = serializer.save()
        return Response({"update": serializer.data}, status=status.HTTP_200_OK)
