from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)$', views.begin_chat, name="chat_start"),
    url(r'^(?P<id>\d+)/send/$', views.recv_chat, name="chat_recieve"),
]
