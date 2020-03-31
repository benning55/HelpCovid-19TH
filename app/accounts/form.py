from django import forms
from core.models import User


class SuperUserForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    tel = forms.CharField(min_length=10)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    repassword = forms.CharField(max_length=255, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        repassword = cleaned_data.get(("repassword"))

        queryset_username = User.objects.all().filter(username=username)
        queryset_email = User.objects.all().filter(email=email)
        if queryset_username.count() > 0:
            raise forms.ValidationError(
                "username นี้ได้ถูกใช้งานไปแล้ว"
            )
        if queryset_email.count() > 0:
            raise forms.ValidationError(
                "email นี้ถูกใช้งานไปแล้ว"
            )
        if password != repassword:
            raise forms.ValidationError(
                "ยืนยันรหัสผ่านของท่านไม่ถูกต้องโปรดตรวจสอบอีกครั้ง"
            )
