from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:kleague_id>/', views.KLEAGUE_detail),
]
