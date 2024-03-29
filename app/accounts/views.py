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
from core.management.commands.gentoken import get_position
from core.models import User, Hospital, EmailStaff, RegisterToken, AboutMe, Location, LocationMaker

from accounts import serializers

Timeline = namedtuple('Timeline', ('hospital', 'user'))


def token_complete(new_user, tokens):
    current_token = RegisterToken.objects.get(token=tokens)
    current_token.status = True
    current_token.register = new_user
    current_token.save()


def create_location(hospital):
    locate = get_position(hospital.name)
    if locate is None:
        pass
    else:
        Location.objects.update_or_create(
            hospital_id=hospital.id,
            latitude=locate[0],
            longitude=locate[1]
        )


def new_hospital_notify(hospital):
    """
    Send an notify email to admin everytime that have order
    """
    admin_email = []
    emails = EmailStaff.objects.all()
    for email in emails:
        admin_email.append(email.email)
    message = render_to_string('new_hospital.html', {
        'hospital': hospital,
    })
    send_mail(
        'มีความช่วยเหลือต้องการ!',
        message,
        'no-reply@covid19th.org',
        admin_email,
        html_message=message,
        fail_silently=False
    )


@api_view(['POST', ])
@permission_classes([AllowAny, ])
@parser_classes([MultiPartParser])
def register(request, format=None):
    """
    Register for Officer the account and Hospital
    """
    if request.method == 'POST':
        data = request.data
        try:
            hospital = {
                'name': data['name'],
                'picture': request.FILES['picture'],
                'address': data['address'],
                'tel': data['hospital_tel'],
                'bank_account_number': data['bank_account_number'],
                'bank_account_name': data['bank_account_name'],
                'bank_name': data['bank_name']
            }
            user = {
                'username': data['username'],
                'letter': request.FILES['letter'],
                'email': data['email'],
                'password': data['password'],
                'first_name': data['first_name'],
                'last_name': data['last_name'],
                'tel': data['user_tel']
            }
        except:
            hospital = {
                'name': data['name'],
                'picture': None,
                'address': data['address'],
                'tel': data['hospital_tel'],
                'bank_account_number': data['bank_account_number'],
                'bank_account_name': data['bank_account_name'],
                'bank_name': data['bank_name']
            }
            user = {
                'username': data['username'],
                'letter': None,
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
                tel=hospital['tel'],
                bank_account_number=hospital['bank_account_number'],
                bank_account_name=hospital['bank_account_name'],
                bank_name=hospital['bank_name']
            )
            new_user = User.objects.create(
                hospital_id=new_hospital.id,
                username=user['username'],
                letter=user['letter'],
                email=user['email'],
                first_name=user['first_name'],
                last_name=user['last_name'],
                tel=user['tel']
            )
            new_user.set_password(user['password'])
            new_user.save()
            new_hospital_notify(new_hospital)
            create_location(new_hospital)
            token_complete(new_user, data['token'])
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class HospitalApiView(APIView):
    """
    Show all hospital in system
    """
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        """
        Get all hospital
        """
        pk = self.kwargs.get('pk')
        queryset = Hospital.objects.all().filter(approve=True).order_by('-id')
        if pk is None:
            serializer = serializers.HospitalSerializer(queryset, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        else:
            hospital = get_object_or_404(queryset, pk=pk)
            user = User.objects.all().filter(hospital_id=hospital.id)
            serializer = serializers.UserSerializer(user, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def get_user(request, *args, **kwargs):
    """Get admin basic information"""
    user = request.user
    queryset = User.objects.all().filter(pk=user.id)
    serializer = serializers.UserSerializer(queryset, many=True)
    return Response({'data': serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET', ])
@permission_classes([AllowAny, ])
def get_location(request, *args, **kwargs):
    """Get admin basic information"""
    pk = kwargs.get('pk')
    queryset = Location.objects.all().filter(hospital__approve=True)
    queryset2 = LocationMaker.objects.all()
    if pk is None:
        serializer = serializers.getLocationSerializer(queryset, many=True)
        serializer2 = serializers.getLocationMakerSerializer(queryset2, many=True)
        result = serializer.data+serializer2.data
        return Response({'data': result}, status=status.HTTP_200_OK)
    else:
        queryset = queryset.filter(pk=pk)
        serializer = serializers.getLocationSerializer(queryset, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST', ])
@permission_classes([AllowAny, ])
def get_token(request, *args, **kwargs):
    """Get admin basic information"""
    if request.method == "POST":
        data = request.data
        queryset = RegisterToken.objects.all()
        queryset = queryset.filter(token=data['token'])
        queryset = queryset.filter(status=False)
        if queryset.count() > 0:
            return Response({'success': 'โทเค่นนี้ยังสามารถใช้งานได้'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'token นี้ได้ถูกใช้งานไปแล้วหรือไม่มีอยู่จริงโปรดติดต่อเจ้าหน้าที่เพื่อขอ token'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
@permission_classes([AllowAny, ])
def aboutme(request):
    """Show description about me"""
    about_me = AboutMe.objects.all()
    serializer = serializers.AboutMeSerializer(about_me, many=True)
    return Response({'data': serializer.data}, status=status.HTTP_200_OK)

