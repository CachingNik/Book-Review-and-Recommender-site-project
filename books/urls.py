from django.urls import re_path
from django.contrib import admin
from . import views

app_name = 'books'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^add/$', views.addbook, name='addbook'),
    re_path(r'^all/$', views.allbooks, name='allbooks'),
    re_path(r'^(?P<book_id>[0-9]+)/$', views.details, name='details'),
    re_path(r'^search/$', views.searcher, name='searcher')
]