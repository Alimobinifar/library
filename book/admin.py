from django.contrib import admin

from book.models import Author, Category, Book, Publisher

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Publisher)
