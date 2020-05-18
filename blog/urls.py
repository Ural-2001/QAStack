from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from account import views as account_views
from .views import *
from account.views import *

urlpatterns = [
    path('post/<int:id>/', post_page, name='post_page'),
    path('add_comment/<int:pk>/', add_comment, name='add_comment'),
]
