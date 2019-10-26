from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

app_name = 'books'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]
