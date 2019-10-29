from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'books'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.addbook, name='addbook'),
    url(r'^all/$', views.allbooks, name='allbooks'),
    url(r'^(?P<book_id>[0-9]+)/$', views.details, name='details'),
]