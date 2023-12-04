from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.OOTD_detail),
    path('<int:pk>/', views.OOTD_detail, name='OOTD_detail'),
    path('<int:pk>/new_comment/', views.new_comment, name='new_comment'), # 댓글 구현 url
    path('', views.ootd_list, name='ootd_list'),
    # path('', views.index),
    path('create_ootd/', views.OOTDCreate.as_view()),
    path('update_ootd/<int:pk>/', views.OOTDUpdate.as_view()),
]