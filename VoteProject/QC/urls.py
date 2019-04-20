from django.conf.urls import url
from . import views

app_name = 'QC'

urlpatterns = [
    url(r'^$', views.questions, name='questions'),
    url(r'^vote/(\d+)/$', views.vote, name='vote'),
    url(r'^score/(\d+)/$', views.score, name='score'),
    url(r'^add_question/$', views.add_question, name='add_question'),
    url(r'^edit_question/(\d+)/$', views.edit_question, name='edit_question'),
    url(r'^delete_question/(\d+)/$', views.delete_question, name='delete_question'),
    url(r'^add_choice/(\d+)/$', views.add_choice, name='add_choice'),
    url(r'^edit_choice/(\d+)/$', views.edit_choice, name='edit_choice'),
    url(r'^delete_choice/(\d+)/$', views.delete_choice, name='delete_choice'),
]
