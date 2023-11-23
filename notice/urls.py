from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.single_notice_page),
    path('', views.index),
    path('create_notice/', views.NoticeCreate.as_view()),
    path('update_notice/<int:pk>/', views.NoticeUpdate.as_view()),

]