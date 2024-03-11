from django.urls import path 

from . import views

urlpatterns = [
    path('', views.AdList.as_view(), name='home'),
    path('<int:ad_id>/', views.ad_detail, name='ad_detail'),
]