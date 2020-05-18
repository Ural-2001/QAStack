from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import TemplateView, DeleteView, CreateView
from blog.models import *
from blog.forms import *
from qa.forms import AnswerForm
from qa.models import *

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
    questions = Question.objects.filter(author=user)
    return render(request, 'account/profile.html', {'posts': posts, 'questions': questions})


class DeletePost(DeleteView):
    def get(self, request, *args, **kwargs):
        user = UserProfile.objects.get(user=request.user)
        post = Post.objects.get(id=self.kwargs.get('id'))
        if Post.objects.filter(author=user, id=post.id).exists():
            Post.objects.filter(author=user, id=post.id).delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class AddPost(CreateView):
    def post(self, request, *args, **kwargs):
        user = UserProfile.objects.get(user=request.user)
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(title=form.cleaned_data['title'], text=form.cleaned_data['text'], author=user)
        print(form.is_valid())
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
