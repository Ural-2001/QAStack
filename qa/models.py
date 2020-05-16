from django.db import models
from account.models import UserProfile

# Create your models here.


class Theme(models.Model):
    name = models.CharField(max_length=100)


class Comment(models.Model):
    text = models.TextField(max_length=400)
    author = models.ForeignKey(UserProfile, related_name='comments', on_delete=models.CASCADE)


class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=400)
    author = models.ForeignKey(UserProfile, related_name='questions', on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment, blank=True, related_name='question')
