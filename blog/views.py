from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import DeleteView

from account.models import UserProfile
from blog.models import *
from .forms import *


def all_posts(request):
    specific_posts2 = Post.objects.filter(Q(title__contains='post') & Q(text__startswith='2'))
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(title__icontains=search_query)
    else:
        posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts, 'specific_posts2': specific_posts2})


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
