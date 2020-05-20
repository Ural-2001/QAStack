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

from .forms import *
from .models import UserProfile
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # user = User()
            # user_profile = UserProfile()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')

            # user.save()
            # user_profile.user = user
            # user_profile.save()
            # new_user = UserProfile.objects.create(user=request.user)
            # new_user.save()

            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})


def all_users(request):
    users = UserProfile.objects.all()
    return render(request, 'account/all_users.html', {'users': users})


def account_page(request, id):
    user = UserProfile.objects.get(id=id)
    posts = Post.objects.filter(author=user)
    questions = Question.objects.filter(author=user)
    return render(request, 'account/account_page.html', {'posts': posts, 'questions': questions, 'user': user})


@login_required()
def profile(request):
    # if UserProfile.objects.get(user=request.user).exists():
    #     user = UserProfile.objects.get(user=request.user)
    # else:
    #     user = UserProfile(user=request.user)
    #     user.save()
    try:
        user = UserProfile.objects.get(user=request.user)
    except Exception:
        user = UserProfile(user=request.user)
        user.save()
    posts = Post.objects.filter(author=user)
    questions = Question.objects.filter(author=user)
    subscriptions = Subscription.objects.filter(who=UserProfile.objects.get(user=request.user.id))
    subscribers = Subscription.objects.filter(on_whom=UserProfile.objects.get(user=request.user.id))
    return render(request, 'account/profile.html', {'posts': posts,
                                                    'questions': questions,
                                                    'subscriptions': subscriptions,
                                                    'subscribers': subscribers,
                                                    'user': user})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = UserProfileEditForm(instance=UserProfile.objects.get(user=request.user),
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = UserProfileEditForm(instance=UserProfile.objects.get(user=request.user))
    return render(request, 'account/edit.html',
                  {'user_form': user_form, 'profile_form': profile_form})


def follow(request, id):
    who = UserProfile.objects.get(user=request.user.id)
    on_whom = UserProfile.objects.get(id=id)
    if not Subscription.objects.filter(who=who, on_whom=on_whom).exists():
        sub = Subscription(who=who, on_whom=on_whom)
        sub.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def unfollow(request, id):
    who = UserProfile.objects.get(user=request.user)
    on_whom = UserProfile.objects.get(id=id)
    if Subscription.objects.filter(who=who, on_whom=on_whom).exists():
        Subscription.objects.filter(who=who, on_whom=on_whom).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


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
