from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views

app_name = 'BookTest'
urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^book/$', views.book, name='book'),
    url(r'^(\d+)/$', views.book_detail, name='book_detail'),
    url(r'^delete/(\d+)$', views.delete, name='delete'),
    url(r'^add/$', views.add_book, name='add_book'),
    url(r'^favicon\.ico$', RedirectView.as_view(url=r'static/img/favicon.ico')),
    url(r'^$', views.index, name='index'),

]
