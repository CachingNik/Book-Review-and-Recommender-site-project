from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

app_names = 'accounts'

urlpatterns = [
	url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', views.signup_view, name='signup'),
]