from django.shortcuts import render
from qa.models import *

# Create your views here.

def index(request):
    themes = Theme.objects.all()
    return render(request, 'Homepage.html', {'themes': themes})
