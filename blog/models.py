from django.db import models
from django.contrib import admin
from account.models import *
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=300)
    author = models.ForeignKey('account.UserProfile', related_name='posts', on_delete=models.CASCADE)
    users_likes = models.ManyToManyField('account.UserProfile', blank=True, related_name='posts_liked')

    def __str__(self):
        return '{} by {}'.format(self.title, self.author)


class Comment(models.Model):
    text = models.TextField(max_length=300)
    author = models.ForeignKey('account.UserProfile', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.text)