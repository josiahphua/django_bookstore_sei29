from django.shortcuts import render

# Create your views here.
def books_index(request):
    return render(request, "books/index.html")
