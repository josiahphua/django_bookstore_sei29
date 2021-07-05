from django.contrib import admin
from books.models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn')

admin.site.register(Book, BookAdmin)