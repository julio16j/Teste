from django.conf.urls import url

from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    #127.0.0.1/polls
    path('/envia/<lat>/<long>/', views.envia, name="envia"),
    # 127.0.0.1/polls/envia/3/3/
    path('/get', views.get, name="get"),
    # 127.0.0.1/polls/envia/3/3/
]