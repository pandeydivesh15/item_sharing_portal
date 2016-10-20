from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index_page, name="welcome"),
    url(r'^createPost/$', views.post_create_page, name="createpost"),
]
