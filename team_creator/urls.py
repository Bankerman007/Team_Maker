"""team_creator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('v_ball.urls')),
    path('base/', include('v_ball.urls')),
    path('register/', include('v_ball.urls')),
    path('success/', include('v_ball.urls')),
    path('delete_players/', include('v_ball.urls')),
    path('delete/', include('v_ball.urls')),
    path('edit_player/', include('v_ball.urls')),
    path('mix_teams/', include('v_ball.urls')),
]

