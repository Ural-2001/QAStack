from django.conf import settings
from django.db import models
from image_cropping import ImageRatioField
from blog.models import Post


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='account/avatars/%Y/%m/%d/', blank=True)
    avatar = ImageRatioField('photo', '106x100')
    master = models.BooleanField

    def __str__(self):
        return '{}'.format(self.user.username)


class Subscription(models.Model):
    who = models.ForeignKey(UserProfile, related_name='subscriptions', on_delete=models.CASCADE)
    on_whom = models.ForeignKey(UserProfile, related_name='subscribers', on_delete=models.CASCADE)


class Bucket(models.Model):
    saved_post = models.ForeignKey(Post, related_name='posts', on_delete=models.CASCADE)

