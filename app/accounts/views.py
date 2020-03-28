from collections import namedtuple

from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from core.models import User, Hospital, EmailStaff

from accounts import serializers

Timeline = namedtuple('Timeline', ('hospital', 'user'))


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
                'back_account_name': data['back_account_name'],
                'bank_name': data['bank_name']
            }
            user = {
                'username': data['username'],
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
                'back_account_name': data['back_account_name'],
                'bank_name': data['bank_name']
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
                tel=hospital['tel'],
                bank_account_number=hospital['bank_account_number'],
                back_account_name=hospital['back_account_name'],
                bank_name=hospital['bank_name']
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
            # new_hospital_notify(new_hospital)
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
