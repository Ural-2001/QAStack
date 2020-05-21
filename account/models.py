from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from image_cropping import ImageRatioField
from blog.models import *


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='account/avatars/%Y/%m/%d/', blank=True)
    master = models.BooleanField(default=False)
    date_of_birth = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return '{}'.format(self.user.username)


class Message(models.Model):
    who = models.ForeignKey('account.UserProfile', related_name='send_mes', on_delete=models.CASCADE)
    to_whom = models.ForeignKey('account.UserProfile', related_name='receive_mes', on_delete=models.CASCADE)
    text = models.TextField(max_length=300)

    def __str__(self):
        return '{} to {}'.format(self.who, self.to_whom)


class Subscription(models.Model):
    who = models.ForeignKey('account.UserProfile', related_name='subscriptions', on_delete=models.CASCADE)
    on_whom = models.ForeignKey('account.UserProfile', related_name='subscribers', on_delete=models.CASCADE)

    def __str__(self):
        return '{} follows {}'.format(self.who, self.on_whom)


class Bucket(models.Model):
    saved_post = models.ForeignKey('blog.Post', related_name='posts', on_delete=models.CASCADE)


class Thank(models.Model):
    who = models.ForeignKey('account.UserProfile', related_name='thanks', on_delete=models.CASCADE)
    to_whom = models.ForeignKey('account.UserProfile', related_name='thanked', on_delete=models.CASCADE)
