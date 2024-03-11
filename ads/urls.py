from django.urls import path 

from . import views

urlpatterns = [
    path('', views.AdList.as_view(), name='home'),
    path('<int:ad_id>/', views.ad_detail, name='ad_detail'),
    path('create_ad/', views.create_ad, name='create_ad'),
    path('<int>/edit_ad/<int:ad_id>', views.edit_ad, name='edit_ad'),
]