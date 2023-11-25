from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.Event_detail),
    path('', views.index),
    path('create_event/', views.EventCreate.as_view()),
    path('update_event/<int:pk>/', views.EventUpdate.as_view()),
]