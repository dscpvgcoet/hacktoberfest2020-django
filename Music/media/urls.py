"""Music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .views import UserRegistrationView, AddAlbum, AddSong
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('album_detail/<int:pk>', views.album_detail, name='albumdetail'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('add_album/', AddAlbum.as_view(), name='add_album'),
    path('add_song/', AddSong.as_view(), name='add_song'),
]
