from django.http import request
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
# from django.views.generic import ListView, DetailView
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Album, Song
from .forms import SignUpForm, AlbumForm, SongForm
# Create your views here.


def index(request):
    # return HttpResponse("<h2 align=center> Welcome to Music App </h2>")
    albums = Album.objects.all()

    return render(request, "home.html", {'albums': albums})


def album_detail(request, pk):

    songs = Song.objects.filter(album__in=Album.objects.filter(id=pk))
    albums = Album.objects.filter(id=pk)
    return render(request, "album_detail.html", {'songs': songs, 'albums': albums})


class UserRegistrationView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class AddAlbum(generic.CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('index')


class AddSong(generic.CreateView):
    model = Song
    form_class = SongForm
    template_name = 'add_song.html'
    success_url = reverse_lazy('index')
