from django.conf.urls import url
from django.views.generic import ListView, DetailView
from blog.models import Post
from . import apps

app_name = apps.BlogConfig.name

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:20],
                                template_name="blog/index.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name="blog/single.html"), name="single"),
]
