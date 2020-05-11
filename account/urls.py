from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from account import views as account_views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', profile, name='profile'),
]
