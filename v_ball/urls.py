from django.urls import path

from . import views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('register/', views.register, name = 'register'),
    path('success/', views.success, name = 'success'),
]