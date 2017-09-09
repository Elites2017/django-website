from django.conf.urls import url
from . import apps, views

app_name = apps.MusicConfig.name

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<album_id>\d+)$', views.detail, name="detail"),
]
