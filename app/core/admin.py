from django.contrib import admin
from core import models
# Register your models here.


admin.site.register(models.User)
admin.site.register(models.Hospital)
admin.site.register(models.Need)
admin.site.register(models.Donator)
admin.site.register(models.MoneyDonate)
