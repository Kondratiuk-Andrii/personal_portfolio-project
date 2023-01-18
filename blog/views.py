from django.shortcuts import render
from .models import *


def home(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/home.html', context={'blogs': blogs})


def blog_detail(request, blog_slug):
    post = Blog.objects.get(slug=blog_slug)
    return render(request, 'blog/blog_detail.html', context={'post': post})
