from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.BlogList),
	path('<int:post_id>', views.blog, name='blog')
]