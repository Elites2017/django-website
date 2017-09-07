from django.shortcuts import render
from .models import Album


def index(request):
    albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums': albums})


def detail(request, album_id):
    album = Album.objects.filter(id=album_id)[0]
    return render(request, 'music/detail.html', {'album': album})
