from . import models as blog_model
from django.views.generic import ListView


class BlogList(ListView):
    model = blog_model.Post
    template_name = 'blog/all-posts.html'
    context_object_name = 'posts'
    queryset = blog_model.Post.objects.order_by("-id")
