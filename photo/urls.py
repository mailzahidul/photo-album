from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('viewphoto/', views.viewphoto, name='viewphoto'),
    path('addphoto/', views.addphoto, name='addphoto'),
]