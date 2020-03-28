from django.urls import path
from rest_framework.routers import DefaultRouter

from accounts import views

urlpatterns = [
    path('register/', views.register)
]
