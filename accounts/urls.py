from django.urls import re_path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

app_names = 'accounts'

urlpatterns = [
	re_path(r'^login/$', views.login_view, name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^signup/$', views.signup_view, name='signup'),
]