from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.single_notice_page),
    path('', views.index),
]