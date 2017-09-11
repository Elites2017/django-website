from django.conf.urls import url
from . import apps, views

app_name = apps.MusicConfig.name

urlpatterns = [
    url(r'^$', views.MusicIndex.as_view(), name="index"),
    url(r'^(?P<pk>\d+)$', views.MusicDetail.as_view(), name="detail"),
]
