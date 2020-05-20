from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from image_cropping import ImageRatioField
from blog.models import *


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='account/avatars/%Y/%m/%d/', blank=True)
    avatar = ImageRatioField('photo', '106x100')
    master = models.BooleanField
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.user.username)


class Subscription(models.Model):
    who = models.ForeignKey('account.UserProfile', related_name='subscriptions', on_delete=models.CASCADE)
    on_whom = models.ForeignKey('account.UserProfile', related_name='subscribers', on_delete=models.CASCADE)

    def __str__(self):
        return '{} follows {}'.format(self.who, self.on_whom)


class Bucket(models.Model):
    saved_post = models.ForeignKey('blog.Post', related_name='posts', on_delete=models.CASCADE)

