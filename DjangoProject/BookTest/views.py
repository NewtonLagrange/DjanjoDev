from django.shortcuts import render
from .models import Book


# Create your views here.
def index(request):
    return render(request, 'BookTest/index.html')


def book(request):
    book_ = Book.objects.all()
    print(book_)
    return render(request, 'BookTest/book.html', context={'books': book_})


def book_detail(request, num):
    book_ = Book.objects.get(pk=int(num))
    print(book_)
    return render(request, 'BookTest/book_detail.html', context={'book': book_})


def test(request):
    return render(request, 'BookTest/index.html')
