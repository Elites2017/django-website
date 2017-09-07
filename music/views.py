from django.shortcuts import render
from .models import Album


def index(request):
    albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums': albums})


def detail(request, album_id):
    return render(request, 'music/detail.html', {'album_id': album_id})
