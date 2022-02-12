from django.contrib import admin
from django.urls import path, include
from book.views import Home, BookDetail, ShowBook, Search, books, book
from book.api_view import ManageBooks, BookById, BookByCat

urlpatterns = [
    path('book-cat-list/<str:cat_name>/', BookDetail.as_view(), name='book-cat-list'),
    path('book-detail/<str:book_name>/', ShowBook.as_view(), name='show_book'),
    path('book-name', books),
    path('book-filter/<str:name>', book),
    path('manage-books/', ManageBooks.as_view()),
    path('book/', BookById.as_view()),
    path('book-by-cat/', BookByCat.as_view()),
]