from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AnswerForm(forms.Form):
    text = forms.CharField()

class QuestionForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField()

