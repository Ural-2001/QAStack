"""QAStack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path

from . import settings
from account import views as account_views

from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', account_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('', include('pages.urls')),
    path('', include('account.urls')),
    path('', include('qa.urls')),

    re_path(r'^media/(?P<path>.)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.)$', serve, {'document_root': settings.STATIC_ROOT}),
]


handler404 = 'pages.views.e_handler404'
handler500 = 'pages.views.e_handler500'