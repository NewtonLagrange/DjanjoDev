from django.conf.urls import url
from . import views

app_name = 'QC'

urlpatterns = [
    url(r'^$', views.questions, name='questions'),
    url(r'^vote/(\d+)$', views.vote, name='vote'),
    url(r'^score/(\d+)$', views.score, name='score')
]
