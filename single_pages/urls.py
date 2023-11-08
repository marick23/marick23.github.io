from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('company/', views.company),
    path('search/', views.search),
]