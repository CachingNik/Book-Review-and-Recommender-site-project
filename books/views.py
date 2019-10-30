from django.shortcuts import render, redirect
from django.template import loader
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import add_book
from .models import Book
from django.db.models import Q
from django.contrib import messages

@login_required(login_url='/accounts/login/')
def index(request):
    all_books = Book.objects.all()
    return render(request, 'books/dashboard.html', {'all_books': all_books})

@login_required(login_url='/accounts/login/')
def addbook(request):
    if request.method == 'POST':
        form = add_book(request.POST)
        if form.is_valid():
            fs= form.save(commit=False)
            fs.added_by_user = request.user.username
            fs.save()
            return redirect('books:index')
    else:
        form = add_book()
        form.added_by_user = request.user
    return render(request, 'books/addbook.html', {'form': form})

def allbooks(request):
	all_books = Book.objects.all()
	return render(request, 'books/allbooks.html', {'all_books': all_books})

@login_required(login_url='/accounts/login/')
def details(request, book_id):
    try:
        this_book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404('This book does not exist')
    return render(request, 'books/details.html', {'this_book': this_book})

def searcher(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = Book.objects.filter(Q(name__icontains=srch) | Q(author__icontains=srch))

            if match:
                return render(request, 'books/searcher.html', {'items': match})
            else:
                messages.error(request, 'No result found!!')

        else:
            return redirect('books:index')

    return render(request, 'books/searcher.html')