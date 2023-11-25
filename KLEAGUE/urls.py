from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:kleague_id>/', views.KLEAGUE_detail),
    path('create_KLEAGUE/', views.KLEAGUECreate.as_view()),
    path('update_KLEAGUE/<int:pk>/', views.KLEAGUEUpdate.as_view()),
]
