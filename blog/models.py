from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, name="title")
    body = models.TextField(name="body")
    date = models.DateTimeField()

    def __str__(self):
        return self.title