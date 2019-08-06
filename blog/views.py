from django.shortcuts import render
from django.contrib import messages
from . import models as blog_model


def BlogList(request):
    posts = blog_model.Post.objects.all()
    context = {"posts": ""}

    return render(
        request, "blog/all-posts.html", {"posts": blog_model.Post.objects.all()}
    )


def all_blogs(request, id):
    post_data = blog_model.Post.objects.get(id=id)
    data = []
    image = ""

    # exception handling
    try:
        image = post_data.cover.url.split("/static/")[1]
    except Exception as e:
        print(e)

    data.append(
        {
            "title": post_data.title,
            "image": image,
            "text": post_data.text,
            "author": post_data.author,
            "categories": post_data.category.all(),
            "published_date": post_data.published_date,
            "related_blogs": post_data.related_blogs.all(),
        }
    )
    context = {}
    context.update({"data": data[0]})

    return render(request, "blog/blog.html", context=context)


def categories(request):
    categories = blog_model.Category.objects.all()
    post_by_category = []
    for data in blog_model.Post.objects.all():
        print(data.category.all())
    for category in categories:
        temp = {
            "category": category,
            "posts": blog_model.Post.objects.filter(category=category),
        }

        post_by_category.append(temp)

    return render(request, "blog/categories.html", {"posts": post_by_category})

