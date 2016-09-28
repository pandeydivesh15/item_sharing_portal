from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index_page, name="index"),
    url(r'^signup/$', views.signup_page, name="signup"),
    url(r'^afterLogin/$', views.after_login, name="afterpost"),
    url(r'^createPost/$', views.post_create_page, name="createpost"),
]
