from django.shortcuts import render
from . import models as blog_model


def BlogList(request):
    context = {"posts": blog_model.Post.objects.all()}
    return render(request, "blog/all-posts.html", context)


def blog(request, post_id):
    context = {"post": blog_model.Post.objects.get(pk=post_id)}

    return render(request, "blog/blog.html", context)

