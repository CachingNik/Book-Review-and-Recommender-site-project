from django.shortcuts import render, redirect
from django.template import loader
from django.http import Http404, HttpResponse

def index(request):
	return HttpResponse('Welcome. Hold On!! Site under construction, Come back later.')