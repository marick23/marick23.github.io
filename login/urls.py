from django.urls import path
from .import views

urlpatterns = [
    path('joinus/', views.memberjoin),
    path('', views.index),
]