from django.shortcuts import render
from .models import Question, Choice
# Create your views here.


def questions(request):
    """ 问题界面: 展示所有问题 """
    questions_ = Question.objects.all()
    return render(request, 'questions.html', context={'questions': questions_})


def vote(request, ques_id):
    """ 投票界面 """
    question = Question.objects.get(pk=ques_id)
    choices = question.choice_set.all()
    return render(request, 'vote.html', context={'ques_id': ques_id, 'choices': choices})


def score(request, ques_id):
    """ 投票结果 """
    choice_id = request.POST.get('choice')
    choice = Choice.objects.get(pk=choice_id)
    choice.num += 1
    choice.save()
    question = Question.objects.get(pk=ques_id)
    choices = question.choice_set.all()

    return render(request, 'score.html', context={'choices': choices, 'question': question})
