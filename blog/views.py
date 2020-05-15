from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import DeleteView

from account.models import UserProfile
from blog.models import Post



