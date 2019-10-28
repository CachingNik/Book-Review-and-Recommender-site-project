from django.shortcuts import render, redirect
from django.template import loader
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import add_book
from .models import Book

@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'books/dashboard.html')

@login_required(login_url='/accounts/login/')
def addbook(request):
    if request.method == 'POST':
        form = add_book(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books:index')
    else:
        form = add_book()
    return render(request, 'books/addbook.html', {'form': form})