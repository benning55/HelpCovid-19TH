from django.urls import path
from rest_framework.routers import DefaultRouter

from accounts import views

router = DefaultRouter()
router.register('hospital', views.HospitalApiView.as_view(), base_name='hospital_viewset')

urlpatterns = [
    path('register/', views.register),
    path('hospital/', views.HospitalApiView.as_view()),
    path('hospital/<int:pk>/', views.HospitalApiView.as_view())
]
