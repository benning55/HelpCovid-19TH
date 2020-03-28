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


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Hospital, HospitalAdmin)
admin.site.register(models.Need)
admin.site.register(models.Donator)
admin.site.register(models.MoneyDonate)
admin.site.register(models.EmailStaff)
