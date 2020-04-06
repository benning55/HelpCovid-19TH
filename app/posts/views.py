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
from core.models import Need, Donator, MoneyDonate, User, Categorie
from posts import serializers


def new_donation_notify(donate):
    """
    Send an notify email to admin everytime that have order
    """
    hospital_id = donate.need.hospital.id
    user = User.objects.get(hospital_id=hospital_id)
    emails = [user.email]
    message = render_to_string('donate_mail.html', {
        'donate': donate,
    })
    send_mail(
        'มีการบริจาคเกิดขึ้น!',
        message,
        'no-reply@covid19th.org',
        emails,
        html_message=message,
        fail_silently=False
    )


def new_donation_money_notify(money_donate):
    """
    Send an notify email to admin everytime that have order
    """
    hospital_id = money_donate.hospital.id
    user = User.objects.get(hospital_id=hospital_id)
    emails = [user.email]
    message = render_to_string('moneydonate_mail.html', {
        'donate': money_donate,
    })
    send_mail(
        'มีการบริจาคเงินเกิดขึ้น!',
        message,
        'no-reply@covid19th.org',
        emails,
        html_message=message,
        fail_silently=False
    )

@api_view(['GET', 'POST'])
@permission_classes([AllowAny, ])
def get_all_need(request, *args, **kwargs):
    """Get all the need"""
    if request.method == "GET":
        queryset = Need.objects.all().order_by('-amount')
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
        pic = data['picture']
        print(data)
        if pic == 'null':
            payload = {
                'hospital_id': data['hospital_id'],
                'picture': None,
                'title': data['title'],
                'category_id': data['category_id'],
                'description': data['description'],
                'amount': data['amount']
            }
            serializer = serializers.NeedSerializer(data=payload)
        else:
            serializer = serializers.NeedSerializer(data=data)
        if serializer.is_valid():
            need = serializer.create(validated_data=serializer.validated_data)
            queryset = Need.objects.all().filter(pk=need.pk)
            show = serializers.NeedSerializer(queryset, many=True)
            return Response({'data': show.data}, status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        user = request.user
        data = request.data
        pk = kwargs.get('pk')
        print(data)
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


@api_view(['GET', 'POST',])
@permission_classes([AllowAny, ])
def donate_need(request, *args, **kwargs):
    """ Donate for hospital need """
    if request.method == "GET":
        """ Get all donate record or by need id"""
        pk = kwargs.get('pk')
        if pk is None:
            queryset = Donator.objects.all()
            serializer = serializers.DonatorSerializer(queryset, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            queryset = Donator.objects.all().filter(need_id=pk)
            serializer = serializers.DonatorSerializer(queryset, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        """Create new donation"""
        data = request.data

        serializer = serializers.DonatorSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            donate = serializer.create(validated_data=serializer.validated_data)
            query = Donator.objects.all().filter(pk=donate.id)
            new_donation_notify(donate)
            show = serializers.DonatorSerializer(query, many=True)
            return Response({'data': show.data}, status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST',])
@permission_classes([AllowAny, ])
@parser_classes([MultiPartParser])
def donate_money(request, *args, **kwargs):
    """ Donate money for hospital """
    if request.method == "GET":
        """ Get all donate money record or by hospital id"""
        pk = kwargs.get('pk')
        if pk is None:
            queryset = MoneyDonate.objects.all().filter(approve_status=True)
            serializer = serializers.MoneyDonateSerializer(queryset, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            queryset = MoneyDonate.objects.all().filter(hospital_id=pk, approve_status=True)
            serializer = serializers.MoneyDonateSerializer(queryset, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        """Create new money donation"""
        data = request.data
        serializer = serializers.MoneyDonateSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            money_donate = serializer.create(validated_data=serializer.validated_data)
            new_donation_money_notify(money_donate)
            query = MoneyDonate.objects.all().filter(pk=money_donate.id)
            show = serializers.MoneyDonateSerializer(query, many=True)
            return Response({'data': show.data}, status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
@permission_classes([AllowAny, ])
def show_categories(request):
    """ Api to load all categories """
    queryset = Categorie.objects.all()
    serializer = serializers.CategorySerializer(queryset, many=True)
    return Response({'data': serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST', ])
@permission_classes([AllowAny, ])
def get_search(request):
    """ Api to load all categories """
    data = request.data
    queryset = Need.objects.all().filter(title__icontains=data['title']).order_by('-amount')
    serializer = serializers.NeedSerializer(queryset, many=True)
    return Response({'data': serializer.data}, status=status.HTTP_200_OK)
