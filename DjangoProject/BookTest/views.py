from django.shortcuts import render
from django.http import HttpResponseRedirect
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


def delete(request, num):
    Book.objects.get(pk=int(num)).delete()
    book_ = Book.objects.all()
    return render(request, 'BookTest/book.html', context={'books': book_})


def add_book(request):

    if request.POST.get('name'):
        name = request.POST.get('name')
        hero_name = request.POST.get('hero_name')
        content = request.POST.get('content')
        book_ = Book()
        book_.name = name
        book_.hero_name = hero_name
        book_.content = content
        book_.save()
        return HttpResponseRedirect('/book/book/')

    else:
        return render(request, 'BookTest/add_book.html')
