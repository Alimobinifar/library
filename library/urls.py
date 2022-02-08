from _ast import Add

from django.contrib import admin
from django.urls import path
from book.views import Home, BookDetail, ShowBook, Search, books, book
from BascektShop.views import AddToBasket, ShowBasket, CancellOrder, ReactiveOrder, Pay
from book.api_view import ShowAllBooks, BookById, BookByCat
from history.views import ShowHistory, HistoryDetail
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('', Home.as_view()),
    path('book-cat-list/<str:cat_name>/', BookDetail.as_view(), name='book-cat-list'),
    path('book-detail/<str:book_name>/', ShowBook.as_view(), name='show_book'),
    path('book-search', Search.as_view(), name='search'),
    path('price-filter', Home.as_view(), name='filter'),
    path('add-to-basket', AddToBasket.as_view(), name='add'),
    path('show-basket', ShowBasket.as_view(), name='show-basket'),
    path('cancellorder', CancellOrder.as_view(),name='cancellorder'),
    path('reactiveorder', ReactiveOrder.as_view(), name='reactiveorder'),
    path('pay', Pay.as_view(), name='pay'),
    path('history', ShowHistory.as_view(), name='history'),
    path('history-detail', HistoryDetail.as_view(), name='history-detail'),
    path('book-name', books),
    path('book-filter/<str:name>', book),
    path('generate-token', views.obtain_auth_token),
    path('show-all-books/', ShowAllBooks.as_view()),
    path('book/', BookById.as_view()),
    path('book-by-cat', BookByCat.as_view())




]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
