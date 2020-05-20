from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from account import views as account_views
from .views import *

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('delete_post/<int:id>', DeletePost.as_view(), name='delete_post'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('all_users/', all_users, name='all_users'),
    path('account_page/<int:id>', account_page, name='account_page'),
    path('follow/<int:id>/', follow, name='follow'),
    path('unfollow/<int:id>/', unfollow, name='unfollow'),
    path('edit/', edit, name='edit'),
    path('', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

