from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)$', views.begin_chat, name="chat_start"),
]
