from django.shortcuts import render, redirect
from django.template import loader
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def index(request):
	return render(request, 'books/dashboard.html')