from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'books'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.addbook, name='addbook')
]