from django.http import Http404
from django.shortcuts import render
from .models import Album


def index(request):
    albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums': albums})


def detail(request, album_id):
    try:
        album = Album.objects.get(id=album_id)
        return render(request, 'music/detail.html', {'album': album})
    except Album.DoesNotExist:
        raise Http404("Album does not exist!")
