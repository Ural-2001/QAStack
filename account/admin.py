from django.contrib import admin
from .models import *
from image_cropping import ImageCroppingMixin


# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#     fields = ['user', 'photo', ]

admin.site.register(UserProfile)