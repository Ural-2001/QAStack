from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from account import views as account_views
from .views import *

urlpatterns = [
    path('question_themes/', question_themes, name='question_themes'),
    path('theme/<int:id>/', question_list, name='theme'),
    path('question/<int:id>/', question, name='question'),
    path('add_answer/<int:pk>/', add_answer, name='add_answer'),
]
