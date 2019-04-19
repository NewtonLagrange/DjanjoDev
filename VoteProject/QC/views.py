from django.shortcuts import render
from .models import Question, Choice
from django.http.response import HttpResponseRedirect
# Create your views here.


def questions(request):
    """ 问题界面: 展示所有问题 """
    questions_ = Question.objects.all()
    return render(request, 'questions.html', context={'questions': questions_})


def vote(request, ques_id):
    """ 投票界面 """
    question = Question.objects.get(pk=ques_id)
    choices = question.choice_set.all()
    return render(request, 'vote.html', context={'question': question, 'choices': choices})


def score(request, ques_id):
    """ 投票结果 """
    choice_id = request.POST.get('choice')
    choice = Choice.objects.get(pk=choice_id)
    choice.num += 1
    choice.save()
    question = Question.objects.get(pk=ques_id)
    choices = question.choice_set.all()

    return render(request, 'score.html', context={'choices': choices, 'question': question})


def add_question(request):
    if request.method == 'POST':
        name = request.POST['name']
        question = Question(name=name)
        question.save()
        return HttpResponseRedirect('/questions/')

    else:
        return render(request, 'add_question.html')


def delete_question(ques_id):
    question = Question.objects.get(pk=ques_id)
    question.delete()
    return HttpResponseRedirect('/questions/')


def add_choice(request, ques_id):
    if request.method == 'POST':
        choice = Choice()
        choice.name = request.POST['name']
        choice.ques = Question.objects.get(pk=ques_id)
        choice.save()
        choices = Choice.objects.all()
        return HttpResponseRedirect('/questions/vote/' + str(ques_id), {'ques_id': ques_id, 'choices': choices})

    else:
        return render(request, 'add_choice.html', context={'ques_id': ques_id})


