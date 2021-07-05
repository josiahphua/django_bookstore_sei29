from books.models import Book
from books.forms import BookForm
from django.shortcuts import redirect, render

# Create your views here.
def books_index(request):
    form = BookForm()

    if request.method == "POST":
        # files get stored in request.FILES
        # request.POST stored form body
        form = BookForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()


    books = Book.objects.all()
    context = { "booksList": books, "form" : form}
    return render(request, "books/index.html", context)


def books_show(request, id):
    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return redirect("books_index_page")
    
    context = {"book": book}
    return render(request, "books/show.html", context)