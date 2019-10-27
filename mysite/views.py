from django.shortcuts import render, redirect
from django.template import loader
from django.http import Http404

def home(request):
    return render(request, 'home.html')