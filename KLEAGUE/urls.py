from django.urls import path
from . import views

urlpatterns = [
    path('', views.KLEAGUE_list, name='KLEAGUE_list'),
    path('<int:kleague_id>/', views.KLEAGUE_detail),
    path('category/<str:slug>/', views.category_page),
    path('create_KLEAGUE/', views.KLEAGUECreate.as_view()),
    path('update_KLEAGUE/<int:pk>/', views.KLEAGUEUpdate.as_view()),
    path('KLEAGUE_detail/<int:kleague_id>/', views.KLEAGUE_detail, name='KLEAGUE_detail'),
]
