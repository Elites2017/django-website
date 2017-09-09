from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=255, name="artist")
    title = models.CharField(max_length=255, name="title")
    genre = models.CharField(max_length=255, name="genre")
    logo = models.TextField(name="logo")

    def __str__(self):
        return 'artist: {} in {}'.format(self.artist, self.title)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file_type = models.CharField(max_length=5)

    def __str__(self):
        return 'title: {}, album: {}'.format(self.title, self.album)
