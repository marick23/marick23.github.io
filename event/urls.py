from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.Event_detail),
    path('', views.index),
]