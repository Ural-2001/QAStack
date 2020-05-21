from django.shortcuts import render
# from django.shortcuts import render_to_response
from django.template import RequestContext

from qa.models import *

# Create your views here.

def index(request):
    themes = Theme.objects.all()
    return render(request, 'Homepage.html', {'themes': themes})

def e_handler404(request, exception):
    context = RequestContext(request)
    response = render(None, '404.html', context)
    response.status_code = 404
    return response

def e_handler500(request):
    return render(request,'500.html')
