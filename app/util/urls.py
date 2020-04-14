from django.urls import path
from rest_framework.routers import DefaultRouter

from util import views

router = DefaultRouter()

urlpatterns = [
    path('chart/', views.get_chart),
    path('popup/', views.get_pop_up),
    path('maker/', views.get_product_maker)
]
