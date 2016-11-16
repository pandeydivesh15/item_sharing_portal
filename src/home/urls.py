from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index_page, name="welcome"),
    url(r'^search/$', views.query_result, name="search"),
    url(r'^aboutus/$', views.about_us, name="aboutus"),
    url(r'^feedback/$', views.feedback, name="feedback"),
    url(r'^faq/$', views.faq, name="faq"),
    url(r'^category/(?P<id>\d+)$', views.category_result, name="category"),
    url(r'^seechats/$', views.see_chats, name="see_chats")
]
