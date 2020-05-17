from django.shortcuts import render
from .models import *

# Create your views here.


def themes():
    themes = Theme.objects.all()
    return (themes)