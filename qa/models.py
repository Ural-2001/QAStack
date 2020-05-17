from django.db import models
from account.models import UserProfile

# Create your models here.


class Theme(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)


class Question(models.Model):
    theme = models.ForeignKey(Theme, related_name='questions', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=400)
    author = models.ForeignKey(UserProfile, related_name='questions', on_delete=models.CASCADE)
    # answers = models.ManyToManyField(Answer, blank=True, related_name='question')

    def __str__(self):
        return '{}'.format(self.title)


class Answer(models.Model):
    text = models.TextField(max_length=400)
    author = models.ForeignKey(UserProfile, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, blank=True, related_name='question', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.text[0:10])

