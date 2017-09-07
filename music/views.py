from django.shortcuts import render


def index(request):
    return render(request, 'music/index.html')


def detail(request, album_id):
    return render(request, 'music/detail.html', {'album_id': album_id})
