from django.shortcuts import render, reverse, redirect
from hashlib import sha1
from .models import Book, User


# Create your views here.
def index(request):
    """ 首页 """
    return render(request, 'BookTest/index.html', {'username': request.session.get('username')})


def login(request):
    """ 登陆 """
    if request.method == 'GET':
        return render(request, 'BookTest/login.html', )

    elif request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd').encode('utf8')
        s = sha1()
        s.update(pwd)
        pwd = s.hexdigest()

        names = User.objects.values('name')
        print(names)
        for name in names:

            if username in name['name']:
                db_pwd = User.objects.get(name=username).pwd

                if pwd == db_pwd:
                    request.session['username'] = username
                    return redirect(reverse('BookTest:index'))

        else:
            return redirect(reverse('BookTest:login'))


def register(request):
    """ 注册 """
    if request.method == 'GET':
        return render(request, 'BookTest/register.html')

    elif request.method == 'POST':
        # TODO username要唯一, 加判断
        username = request.POST.get('username')
        pwd = request.POST.get('pwd').encode('utf8')
        # 加密密码
        s = sha1()
        s.update(pwd)
        pwd = s.hexdigest()
        user = User()
        user.name = username
        user.pwd = pwd
        user.save()
        return redirect(reverse('BookTest:login'))


def logout(request):
    """ 退出 """
    request.session.pop('username')
    return redirect(reverse('BookTest:index'))


def book(request):
    book_ = Book.objects.all()
    return render(request, 'BookTest/book.html', context={'books': book_})


def book_detail(request, num):
    book_ = Book.objects.get(pk=int(num))
    print(book_)
    return render(request, 'BookTest/book_detail.html', context={'book': book_})


def delete(request, num):
    Book.objects.get(pk=int(num)).delete()
    return redirect(reverse('BookTest:book'))


def add_book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        hero_name = request.POST.get('hero_name')
        content = request.POST.get('content')
        book_ = Book()
        book_.name = name
        book_.hero_name = hero_name
        book_.content = content
        book_.save()
        return redirect(reverse('BookTest:book'))

    else:
        return render(request, 'BookTest/add_book.html')
