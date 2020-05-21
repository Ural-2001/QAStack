from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView

from qa.forms import AnswerForm
from .models import *

from django.core.paginator import Paginator

# Create your views here.


def question_themes(request):
    search_query = request.GET.get('search', '')
    if search_query:
        themes_in_pag = Theme.objects.filter(name__icontains=search_query)
    else:
        themes_in_pag = Theme.objects.all()
    themes = Theme.objects.all()

    paginator = Paginator(themes_in_pag, 2)
    page = request.GET.get('page')
    themes_in_pag = paginator.get_page(page)
    return render(request, 'question_themes.html', {'themes': themes, 'themes_in_pag': themes_in_pag})


def question_list(request, id):
    theme = Theme.objects.get(id=id)
    questions = Question.objects.filter(theme=Theme.objects.get(id=id))
    return render(request, 'theme.html', {'questions': questions, 'theme': theme})


def question(request, id):
    question = Question.objects.get(id=id)
    answers = Answer.objects.filter(question=Question.objects.get(id=id))
    return render(request, 'question.html', {'answers': answers, 'question': question})


def add_answer(request, pk):
    user = UserProfile.objects.get(user=request.user)
    question = Question.objects.get(id=pk)
    form = AnswerForm(request.POST)
    if form.is_valid():
        Answer.objects.create(text=form.cleaned_data['text'], author=user, question=question)
    print(form.is_valid())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# class AddAnswer(CreateView):
    # def post(self, request, *args, **kwargs):
    #     user = UserProfile.objects.get(user=request.user)
    #     question = Question.objects.get(id=kwargs.get)
    #     form = AnswerForm(request.POST)
    #     if form.is_valid():
    #         Answer.objects.create(text=form.cleaned_data['text'], author=user, question=question)
    #     print(form.is_valid())
    #     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
