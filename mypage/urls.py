from django.urls import path
from .import views

urlpatterns = [
    path('infor/', views.infor),
    path('', views.index),
]