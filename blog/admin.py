from django.contrib import admin
from .models import *

# Register your models here.


# @admin.register(Post)
# class Post(admin.ModelAdmin):
#     fields = ['user', 'photo', ]

admin.site.register(Post)