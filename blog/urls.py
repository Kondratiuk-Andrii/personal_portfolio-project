from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),
    path('<slug:blog_slug>/', blog_detail, name='blog_detail')
]
