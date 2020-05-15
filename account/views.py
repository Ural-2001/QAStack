from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import TemplateView
from blog.models import *

from .forms import UserRegisterForm
from .models import UserProfile
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})



# class ProfileView(TemplateView):
#     template_name = 'account/profile.html'
#
#     def get(self, request, *args, **kwargs):
#         return render(request, 'account/profile.html')
#
#     def post(self, request, *args, ** kwargs):
#         pass


@login_required()
def profile(request):
    user = UserProfile.objects.get(user=request.user)
    posts = Post.objects.filter(author=user)
    return render(request, 'account/profile.html', {'posts': posts})
