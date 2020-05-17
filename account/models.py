from django.conf import settings
from django.db import models
from image_cropping import ImageRatioField


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='account/avatars/%Y/%m/%d/', blank=True)
    avatar = ImageRatioField('photo', '106x100')
    master = models.BooleanField

    def __str__(self):
        return '{}'.format(self.user.username)
