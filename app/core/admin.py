from django.contrib import admin
from core import models
# Register your models here.


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
    list_filter = ['is_active']
    list_per_page = 10

    search_fields = ['username', 'hospital_name']


class NeedAdmin(admin.ModelAdmin):
    list_display = ['id', 'hospital', 'title', 'description', 'amount', 'status', 'created']
    list_display_links = ['id', 'title']
    ordering = ['-created']
    list_filter = ['status']
    list_per_page = 10

    search_fields = ['title', 'hospital_name']
    inlines = [DonatorInLine]


class DonatorAdmin(admin.ModelAdmin):
    list_display = ['id', 'need', 'first_name', 'last_name', 'email', 'tel', 'amount', 'approve_status', 'created']
    ordering = ['-created']
    list_display_links = ['id', 'need']
    list_filter = ['approve_status']
    list_per_page = 10

    search_fields = ['first_name', 'need_title']


class MoneyDonateAdmin(admin.ModelAdmin):
    list_display = ['id', 'hospital', 'first_name', 'last_name', 'amount', 'approve_status', 'created']
    ordering = ['-created']
    list_display_links = ['id', 'hospital']
    list_filter = ['approve_status']
    list_per_page = 10

    search_fields = ['first_name', 'hospital_name']

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Hospital, HospitalAdmin)
admin.site.register(models.Need, NeedAdmin)
admin.site.register(models.Donator, DonatorAdmin)
admin.site.register(models.MoneyDonate, MoneyDonateAdmin)
admin.site.register(models.EmailStaff)
