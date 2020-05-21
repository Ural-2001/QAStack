from django.contrib import admin
from .models import *
from image_cropping import ImageCroppingMixin


# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#     fields = ['user', 'photo', ]

# admin.site.register(UserProfile)
admin.site.register(Subscription)
admin.site.register(Bucket)
admin.site.register(Message)
admin.site.register(Thank)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'master', 'date_of_birth')
    list_filter = ('date_of_birth',)

