from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=255, name="artist")
    title = models.CharField(max_length=255, name="title")
    genre = models.CharField(max_length=255, name="genre")
    logo = models.TextField(name="logo")

    def __str__(self):
        return 'artist = {}, title = {}, genre = {}, logo = {}'.format(self.artist, self.title, self.genre, self.logo)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file_type = models.CharField(max_length=5)
