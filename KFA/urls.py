from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:kfa_id>/', views.KFA_detail),
    path('create_KFA/', views.KFACreate.as_view()),
    path('update_KFA/<int:pk>/', views.KFAUpdate.as_view()),
    # path('create_review/', views.REVIEWCreate.as_view()),
    # path('update_review/<int:pk>/', views.REVIEWUpdate.as_view()),
]
