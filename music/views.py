from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Album


'''
from django.shortcuts import render, get_object_or_404


def index(request):
    albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums': albums})


def detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    songs = album.song_set.all()
    return render(request, 'music/detail.html', {'album': album, 'songs': songs})
'''


class MusicIndex(ListView):
    template_name = "music/index.html"
    context_object_name = "albums"

    def get_queryset(self):
        return Album.objects.all()


class MusicDetail(DetailView):
    model = Album
    # pk_url_kwarg = "album_id"
    template_name = "music/detail.html"


class AlbumCreate(CreateView):
    model = Album
    fields = ['title', 'artist', 'genre', 'logo']
