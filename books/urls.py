from django.urls import path
from books.views import *

app_name = "books" #books:books_index_page

urlpatterns = [
    path("", books_index, name="books_index_page")    
]
