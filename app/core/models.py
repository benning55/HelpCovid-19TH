import os
import datetime
import uuid

from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.template.loader import render_to_string


def mail_to_hospital(user):
    """ Send email that hospital staff is activate"""
    email = []
    user_email = user.email
    email.append(user_email)
    message = render_to_string('mail_hospital.html', {
        'status': 'activate',
        'user': user
    })
    send_mail(
        'Your covid19-help request ',
        message,
        'no-reply@covid19th.org',
        email,
        html_message=message,
        fail_silently=False
    )


def hospital_image(instance, filename):
    """Generate file path for hospital"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/hospital/', filename)


def need_image(instance, filename):
    """Generate file path for need"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/need/', filename)


def receipt_image(instance, filename):
    """Generate file path for need"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/receipt/', filename)


class UserManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, username, email, password=None):
        """Create new user profile"""
        if not username:
            raise ValueError('User must have a username')
        if not email:
            raise ValueError('User must have an email')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password=None):
        """Create and save a new superuser with given details"""
        user = self.create_user(username, email, password)

        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class Hospital(models.Model):
    """Hospital model"""
    name = models.CharField(max_length=255, unique=True)
    picture = models.ImageField(upload_to=hospital_image, null=True, blank=True)
    address = models.TextField()
    tel = models.CharField(max_length=10)
    donated_money = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    bank_account_number = models.CharField(max_length=20)
    bank_account_name = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
    approve = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """ Cahnge approve state """
        queryset = Hospital.objects.all().filter(name=self.name)
        if queryset.count() < 1:
            super(Hospital, self).save(*args, **kwargs)
        else:
            if self.approve:
                user = User.objects.all().filter(hospital__name=self.name)[0]
                user.is_active = True
                user.save()
                mail_to_hospital(user)
            else:
                user = User.objects.all().filter(hospital__name=self.name)[0]
                user.is_active = False
                user.save()
            super(Hospital, self).save(*args, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model"""
    hospital = models.OneToOneField(
        Hospital,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    tel = models.CharField(max_length=10, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()


class Need(models.Model):
    """Need of hospital"""
    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to=need_image, null=True, blank=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    base_amount = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.datetime.now, editable=False)

    def __str__(self):
        return f'{self.hospital.name}, {self.title}'


class Donator(models.Model):
    """ Donator model """
    need = models.ForeignKey(
        Need,
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    approve_status = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.datetime.now, editable=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class MoneyDonate(models.Model):
    """ Money Donate Model """
    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=10, blank=True, null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    receipt = models.ImageField(upload_to=receipt_image)
    time_transfer = models.DateTimeField(blank=True, null=True)
    approve_status = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.datetime.now, editable=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class EmailStaff(models.Model):
    """ Email that send to staff """
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.email


class RegisterToken(models.Model):
    """ Token to match up to register"""
    token = models.CharField(max_length=10)
    status = models.BooleanField(default=False)
    register = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
