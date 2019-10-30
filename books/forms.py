from django import forms
from .models import Book, Review


class add_book(forms.ModelForm):

	class Meta:
            model = Book
            fields = ('name','author','price','type','image')
            labels = {
            'name': 'Book Name',
            'author': 'Book Author',
            'price': 'Price of the book',
            'type': 'Book Genre',
            'image': 'Cover page Image'
            }

class review_book(forms.ModelForm):

      class Meta:
            model = Review
            fields = ('content',)