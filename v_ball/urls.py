from django.urls import path
from django.conf.urls import url
from . import views



urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('register/', views.register, name = 'register'),
    path('success/', views.success, name = 'success'),
    path('delete_players/', views.delete_players, name = 'delete_players'),
    path('delete/<id>', views.delete, name="delete"),
    path('edit_player/<id>', views.edit_player, name="edit_player"),
    path('mix_teams/', views.mix_teams, name= "mix_teams"),
]