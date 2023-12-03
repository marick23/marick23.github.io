from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:kleague_id>/', views.KLEAGUE_detail),
    path('category/<str:slug>/', views.category_page),
    path('create_KLEAGUE/', views.KLEAGUECreate.as_view()),
    path('update_KLEAGUE/<int:pk>/', views.KLEAGUEUpdate.as_view()),
    path('KLEAGUE_detail/<int:kleague_id>/', views.KLEAGUE_detail, name='KLEAGUE_detail'),
    path('<int:kleague_id>/create_review/', views.create_review, name='create_review'),
    path('update_review/<int:pk>/', views.REVIEWUpdate.as_view(), name='update_review'),
]
