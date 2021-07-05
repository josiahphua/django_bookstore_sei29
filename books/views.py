from books.models import Book
from django.shortcuts import render

# Create your views here.
def books_index(request):

    books = Book.objects.all()
    
    context = { "booksList": books}
    return render(request, "books/index.html", context)
