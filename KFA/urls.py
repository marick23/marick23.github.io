from django.urls import path
from . import views
# from .views import KFA_detail

urlpatterns = [
    # path('', views.KFAList.as_view()),
    # path('<int:pk>/', views.KFADetail.as_view()),
    path('', views.index),
    path('<int:kfa_id>/', views.KFA_detail),
    # path('<int:kfa_id>/', views.KFA_detail),
]
