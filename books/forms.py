from django import forms
from django.forms import models
from books.models import Book

class BookForm(models.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'