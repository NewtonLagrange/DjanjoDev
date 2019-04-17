from django.conf.urls import url
from .views import index, book, book_detail, test

app_name = 'BookTest'
urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^index/book/$', book, name='book'),
    url(r'^index/book/(\d+)/$', book_detail, name='book_detail'),
    url(r'', test)
]