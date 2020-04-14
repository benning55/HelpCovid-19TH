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
from core.models import Need, Donator, MoneyDonate, User, Categorie, PopUp, ProductMaker
from util import serializers


def sum_donation(id):
    """ Sum donate amount by category"""
    box = 0
    queryset = Donator.objects.all().filter(need__category_id=id, approve_status=True)
    for donator in queryset:
        box += donator.amount
    return box


def get_total_money():
    """ get all money donate"""
    box = 0
    queryset = MoneyDonate.objects.all().filter(approve_status=True)
    for money_donate in queryset:
        box += money_donate.amount
    return box


@api_view(['GET', ])
@permission_classes([AllowAny, ])
def get_chart(request, *args, **kwargs):
    """ Get Donator and All Money"""
    if request.method == "GET":
        data = {
            'total_category1': sum_donation(1),
            'total_category2': sum_donation(2),
            'total_category3': sum_donation(3),
            'total_category4': sum_donation(4)
        }
        return Response({
            'data': data,
            'total_money': get_total_money()
        }, status=status.HTTP_200_OK)


@api_view(['GET', ])
@permission_classes([AllowAny, ])
def get_pop_up(request, *args, **kwargs):
    """ Get pop up data """
    if request.method == "GET":
        queryset = PopUp.objects.all()
        serializer = serializers.PopUpSerializer(queryset, many=True)
        return Response({
            'data': serializer.data,
            'total_money': get_total_money()
        }, status=status.HTTP_200_OK)


@api_view(['GET', ])
@permission_classes([AllowAny, ])
def get_product_maker(request, *args, **kwargs):
    if request.method == "GET":
        queryset = ProductMaker.objects.all()
        serializer = serializers.ProductMakerSerializer(queryset, many=True)
        return Response({
            'data': serializer.data
        }, status=status.HTTP_200_OK)
