import os
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.contrib import admin, messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import path
from core.management.commands.gentoken import token_generator
from accounts.form import SuperUserForm
from core import models
# Register your models here.


def add_spreadsheet(queryset):
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)

    client = gspread.authorize(creds)

    sheet = client.open("Tokens Register").sheet1

    register_token = queryset

    for index, tokens in enumerate(queryset):
        try:
            insert_token = [tokens.token]
        except:
            insert_token = [tokens.token]
        sheet.insert_row(insert_token, index + 2)


class UserInLine(admin.StackedInline):
    model = models.User
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False


class HospitalInLine(admin.StackedInline):
    model = models.Hospital
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False


class NeedInLine(admin.StackedInline):
    model = models.Need
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False


class DonatorInLine(admin.StackedInline):
    model = models.Donator
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False


class HospitalAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'tel', 'donated_money', 'approve']
    list_display_links = ['id', 'name']
    list_editable = ['approve']
    list_filter = ['approve']
    list_per_page = 10

    search_fields = ['name']
    inlines = [UserInLine]


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'hospital', 'username', 'first_name', 'last_name', 'email', 'tel', 'is_active']
    list_display_links = ['id', 'username']
    list_filter = ['is_active', 'is_superuser']
    list_per_page = 10

    search_fields = ['username']

    change_list_template = 'superuser_list.html'

    def has_add_permission(self, request):
        return False

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('add-super/', self.add_super),
        ]
        return my_urls + urls

    def add_super(self, request):
        if request.method == 'POST':
            super_user_form = SuperUserForm(request.POST)
            if super_user_form.is_valid():
                username = super_user_form.cleaned_data['username']
                email = super_user_form.cleaned_data['email']
                tel = super_user_form.cleaned_data['tel']
                password = super_user_form.cleaned_data['password']

                super_user = models.User.objects.create_superuser(
                   username=username,
                   email=email,
                   password=password
                )
                super_user.tel = tel
                super_user.is_active = False
                super_user.save()
                messages.success(request, 'การสมัครของคุณเรียบร้อยแล้วรอการยืนยันจาก superadmin')
                return HttpResponseRedirect("../")
        else:
            super_user_form = SuperUserForm()
        return render(request, 'super_admin.html', {'form': super_user_form})


class NeedAdmin(admin.ModelAdmin):
    list_display = ['id', 'hospital', 'title', 'description', 'amount', 'status', 'created']
    list_display_links = ['id', 'title']
    ordering = ['-created']
    list_filter = ['status']
    list_per_page = 10

    search_fields = ['title', 'hospital__name']
    inlines = [DonatorInLine]


class DonatorAdmin(admin.ModelAdmin):
    list_display = ['id', 'need', 'first_name', 'last_name', 'email', 'tel', 'amount', 'approve_status', 'created']
    ordering = ['-created']
    list_editable = ['approve_status']
    list_display_links = ['id', 'need']
    list_filter = ['approve_status']
    list_per_page = 10

    search_fields = ['first_name', 'need__title']


class MoneyDonateAdmin(admin.ModelAdmin):
    list_display = ['id', 'hospital', 'first_name', 'last_name', 'amount', 'approve_status', 'created']
    ordering = ['-created']
    list_editable = ['approve_status']
    list_display_links = ['id', 'hospital']
    list_filter = ['approve_status']
    list_per_page = 10

    search_fields = ['first_name', 'hospital__name']


class RegisterTokenAdmin(admin.ModelAdmin):
    list_display = ['token', 'status', 'register']
    ordering = ['-created']
    list_display_links = ['token', 'register']
    list_filter = ['status']
    list_per_page = 10

    change_list_template = 'token_register.html'

    search_fields = ['token']

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('look-token/', self.look_token),
            path('add_token/', self.add_token),
            path('look-yes/', self.look_yes),
            path('look-no/', self.look_no)
        ]
        return my_urls + urls

    def look_token(self, request):
        """ Add all token to spreadsheet"""
        register_token = models.RegisterToken.objects.all()
        response = HttpResponse(content_type='text/csv')

        writer = csv.writer(response)
        writer.writerow(['token', 'status', 'username'])

        for token in register_token.values_list('token', 'status', 'register__username'):
            writer.writerow(token)

        response['Content-Disposition'] = 'attachment; filename="token.csv"'
        return response

    def look_yes(self, request):
        """ เพิ่มโทเคนที่ใช้ใน spreadsheet """
        register_token = models.RegisterToken.objects.all().filter(status=True)
        response = HttpResponse(content_type='text/csv')

        writer = csv.writer(response)
        writer.writerow(['token', 'status', 'username'])

        for token in register_token.values_list('token', 'status', 'register__username'):
            writer.writerow(token)

        response['Content-Disposition'] = 'attachment; filename="token.csv"'
        return response

    def look_no(self, request):
        """ เพิ่มโทเคนที่ไม่ใช้ใน spreadsheet """
        register_token = models.RegisterToken.objects.all().filter(status=False)
        response = HttpResponse(content_type='text/csv')

        writer = csv.writer(response)
        writer.writerow(['token', 'status', 'username'])

        for token in register_token.values_list('token', 'status', 'register__username'):
            writer.writerow(token)

        response['Content-Disposition'] = 'attachment; filename="token.csv"'
        return response

    def add_token(self, request):
        """ Take how many token that be generate """
        if request.method == "POST":
            amount = request.POST.get("num", "")
            int_amount = int(amount)
            for _ in range(int_amount):
                token = token_generator()
                models.RegisterToken.objects.create(
                    token=token
                )
            messages.success(request, f'Token จำนวน {int_amount} อันได้ถูกสร้างขึ้น')
        return HttpResponseRedirect("../")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['-id']
    list_display_links = ['id', 'name']
    list_per_page = 10

    search_fields = ['name']


class PopUpAdmin(admin.ModelAdmin):
    list_display = ['id', 'picture', 'description']
    list_display_links = ['id']
    ordering = ['-id']
    list_per_page = 10


class ProductMakerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'picture', 'company', 'tel']
    ordering = ['-id']
    list_display_links = ['id', 'title']

    search_fields = ['title']

    list_per_page = 10


class LocationAdmin(admin.ModelAdmin):
    list_display = ['hospital_id', 'latitude', 'longitude']
    list_per_page = 10

    search_fields = ['hospital__name']


class LocationMakerAdmin(admin.ModelAdmin):
    list_display = ['maker_id', 'latitude', 'longitude']
    list_per_page = 10

    search_fields = ['maker__company']


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Hospital, HospitalAdmin)
admin.site.register(models.Need, NeedAdmin)
admin.site.register(models.Donator, DonatorAdmin)
admin.site.register(models.MoneyDonate, MoneyDonateAdmin)
admin.site.register(models.EmailStaff)
admin.site.register(models.RegisterToken, RegisterTokenAdmin)
admin.site.register(models.Categorie, CategoryAdmin)
admin.site.register(models.AboutMe)
admin.site.register(models.PopUp, PopUpAdmin)
admin.site.register(models.ProductMaker, ProductMakerAdmin)
admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.LocationMaker, LocationMakerAdmin)

