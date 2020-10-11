from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
# Create your views here.
def index(request):
    # return HttpResponse("<h2 align=center> Welcome to Music App </h2>")
    albums = Album.objects.all()
    return render(request,"home.html",{'albums':albums})