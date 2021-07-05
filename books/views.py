from books.models import Book
from books.forms import BookForm
from django.shortcuts import render

# Create your views here.
def books_index(request):
    form = BookForm()

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()


    books = Book.objects.all()
    context = { "booksList": books, "form" : form}
    return render(request, "books/index.html", context)
