from django.shortcuts import render
from . import models as blog_model


def BlogList(request):
    context = {"posts": blog_model.Post.objects.all()}
    return render(request, "blog/all-posts.html", context)


def blog(request, post_id):
    post_data = blog_model.Post.objects.get(pk=post_id)
    print(post_data.cover.url)
    context = {"post": post_data}

    return render(request, "blog/blog.html", context)

