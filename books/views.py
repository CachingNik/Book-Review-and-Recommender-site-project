from django.shortcuts import render, redirect
from .models import Book
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

def index(request):
    all_books = Book.objects.all()
    template = loader.get_template('books/index.html')
    context = {'all_books': all_books}
    return HttpResponse(template.render(context, request))


def detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404('This book does not exist')
    return render(request, 'books/detail.html', {'book': book})

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username = username, password = raw_password)
			login(request, user)
			return redirect('/books')
	else:
		form = SignUpForm()
	return render(request, 'registration/signup.html', {'form': form})


# Create your views here.
