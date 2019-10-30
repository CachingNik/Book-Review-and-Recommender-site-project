from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    image = models.CharField(max_length=300)
    added_by_user = models.ForeignKey(User)

    def __str__(self):
    	return self.name + '-' + self.author


class Review(models.Model):
	book = models.ForeignKey(Book)
	user = models.ForeignKey(User)
	content = models.TextField(max_length=500)
	time_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{}-{}'.format(self.book.name + '(' + self.book.author + ')', str(self.user.username))

# Create your models here.