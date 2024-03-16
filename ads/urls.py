from django.urls import path 

from . import views


urlpatterns = [
    path('', views.AdList.as_view(), name='home'),
    path('<int:ad_id>/', views.ad_detail, name='ad_detail'),
    path('create_ad/', views.create_ad, name='create_ad'),
    path('edit_ad/<int:ad_id>/', views.edit_ad, name='edit_ad'),
    path('delete/<int:ad_id>/', views.delete_ad, name='delete_ad' ),
    path('about/', views.about_view, name='about'),
]

