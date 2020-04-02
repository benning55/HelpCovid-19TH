from django.urls import path
from rest_framework.routers import DefaultRouter

from posts import views

router = DefaultRouter()

urlpatterns = [
    path('need/', views.get_all_need),
    path('need/<int:pk>/', views.get_all_need),
    path('create-need/', views.add_need),
    path('create-need/<int:pk>/', views.add_need),
    path('donate/', views.donate_need),
    path('donate/<int:pk>/', views.donate_need),
    path('search/', views.get_search),
    path('category/', views.show_categories),
    path('money-donate/', views.donate_money),
    path('money-donate/<int:pk>/', views.donate_money)
]
