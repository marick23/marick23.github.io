from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.single_ask_page),
    path('', views.index),
    path('create_ask/', views.AskCreate.as_view()),
    path('update_ask/<int:pk>/', views.AskUpdate.as_view()),
]