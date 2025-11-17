from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
]
