from django.urls import path
from rest_framework.routers import DefaultRouter

from officer import views

router = DefaultRouter()

urlpatterns = [
    path('officer-donate/', views.officer_donation),
    path('officer-donate/<int:pk>/', views.officer_donation),
    path('officer-donate-money/', views.officer_donation_money),
    path('officer-donate-money/<int:pk>/', views.officer_donation_money)
]
