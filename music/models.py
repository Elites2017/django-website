from django.db import models
from django.core.urlresolvers import reverse


class Album(models.Model):
    artist = models.CharField(max_length=256, name="artist")
    title = models.CharField(max_length=256, name="title")
    genre = models.CharField(max_length=256, name="genre")
    logo = models.CharField(max_length=256, name="logo")

    def __str__(self):
        return 'artist: {} in {}'.format(self.artist, self.title)

    def get_absolute_url(self):
        return reverse('music:add-album', kwargs={'pk': self.pk})


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file_type = models.CharField(max_length=5)

    def __str__(self):
        return 'title: {}, album: {}'.format(self.title, self.album)
