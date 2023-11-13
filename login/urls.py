from django.urls import path
from .import views

urlpatterns = [
    path('memberjoin/', views.memberjoin),
    path('', views.index),
]