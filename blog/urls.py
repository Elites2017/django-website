from django.conf.urls import url
from django.views.generic import ListView
from blog.models import Post

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="blog/index.html")),
]
