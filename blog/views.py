from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import DeleteView

from account.models import UserProfile
from blog.models import *
from .forms import *


def post_page(request, id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'post.html', {'post': post, 'comments': comments})


def add_comment(request, pk):
    user = UserProfile.objects.get(user=request.user)
    post = Post.objects.get(id=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        Comment.objects.create(text=form.cleaned_data['text'], author=user, post=post)
    print(form.is_valid())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
