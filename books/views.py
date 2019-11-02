from django.shortcuts import render, redirect
from django.template import loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import add_book, review_book
from .models import Book, Review
from django.db.models import Q
from django.contrib import messages

@login_required(login_url='/accounts/login/')
def index(request):
    your_books = Book.objects.filter(added_by_user=request.user)
    reviewed_books = Review.objects.filter(user=request.user)
    rcdns = Book.objects.none()
    for your_book in your_books:
        match = Book.objects.filter(Q(author__icontains=your_book.author) | Q(type__icontains=your_book.type))
        rcdns = rcdns | match
    for any_book in reviewed_books:
        match1 = Book.objects.filter(Q(author__icontains=any_book.book.author) | Q(type__icontains=any_book.book.type))
        rcdns = rcdns | match1
    return render(request, 'books/dashboard.html', {'your_books': your_books, 'rcdns': rcdns})

@login_required(login_url='/accounts/login/')
def addbook(request):
    if request.method == 'POST':
        form = add_book(request.POST)
        if form.is_valid():
            fs= form.save(commit=False)
            fs.added_by_user = request.user
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
    reviews = Review.objects.filter(book=book_id)
    try:
        this_book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404('This book does not exist')
    if request.method =='POST':
        review_form = review_book(request.POST)
        if review_form.is_valid():
            content = request.POST.get('content')
            review = Review.objects.create(book=this_book, user=request.user, content=content)
            review.save()
            return HttpResponseRedirect(request.path)
    else:
        review_form = review_book()
    return render(request, 'books/details.html', {'this_book': this_book, 'reviews': reviews, 'review_form': review_form})

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
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, 'books/searcher.html')