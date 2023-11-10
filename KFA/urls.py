from django.urls import path
from . import views
from .views import KFA_detail

urlpatterns = [
    path('', views.KFAList.as_view()),
    path('<int:pk>/', views.KFADetail.as_view()),
    path('kfa/<int:kfa_id>/', KFA_detail, name='KFA_detail'),
]
