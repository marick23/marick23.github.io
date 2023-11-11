from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:kfa_id>/', views.KFA_detail),
]
