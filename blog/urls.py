from django.contrib import admin
from django.urls import path, include
from . import views 


urlpatterns = [
    path('', views.BlogList),
	path('blog/<int:id>', views.all_blogs, name="all-blogs"),
	path('categories', views.categories, name='categories')
]
