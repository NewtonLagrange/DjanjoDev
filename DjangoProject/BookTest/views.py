from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


# Create your views here.
def index(request):
    return HttpResponse('首页')


def detail(request, num):
    book = Book.objects.get(pk=int(num)).name
    print(book)
    return HttpResponse('首页'+num+book)
