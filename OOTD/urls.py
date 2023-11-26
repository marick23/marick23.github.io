from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.OOTD_detail),
    path('', views.ootd_list, name='ootd_list'),
    path('', views.index),
    path('create_ootd/', views.OOTDCreate.as_view()),
    path('update_ootd/<int:pk>/', views.OOTDUpdate.as_view()),
]