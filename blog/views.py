from django.shortcuts import render
from . import models as blog_model


def BlogList(request):
    context = {"posts": blog_model.Post.objects.all()}
    return render(request, "blog/all-posts.html", context)


def blog(request, post_id):
    post_data = blog_model.Post.objects.get(pk=post_id)
    context = {}
    data = []
    image = ""

    try:
        image = post_data.cover.url.split('/static/')[1]
    except Exception as e:
        print(e)
    
    data.append({
        'title':post_data.title,
        'image':image
    })

    context.update({"post": data[0]})
    return render(request, "blog/blog.html", context=context)

