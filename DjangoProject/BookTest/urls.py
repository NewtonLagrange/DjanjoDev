from django.conf.urls import url
from .views import index, book, book_detail, test

urlpatterns = [
    url(r'^index/$', index),
    url(r'^index/book/$', book),
    url(r'^index/book/(\d+)/$', book_detail),
    url(r'', test)
]