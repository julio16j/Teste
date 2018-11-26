from django.conf.urls import url

from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    #127.0.0.1/polls
    path('/<question_id>/', views.detail, name="detail"),
    #127.0.0.1/polls/1
    path('/results/<question_id>/', views.results, name="result"),
    # 127.0.0.1/polls/1/results
    path('/vote/<question_id>/', views.vote, name="vote"),
    #127.0.0.1/polls/1/vote
]