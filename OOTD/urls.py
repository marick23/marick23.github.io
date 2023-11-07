from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.OOTD_detail),
    path('', views.index),
]