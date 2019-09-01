from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render

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




# Create your views here.
