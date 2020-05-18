from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from account import views as account_views
from .views import *

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('delete_post/<int:id>', DeletePost.as_view(), name='delete_post'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('', include('blog.urls')),
]
