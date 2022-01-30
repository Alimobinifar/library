from django.contrib import admin
from django.urls import path
from book.views import Home, BookDetail, ShowBook, Search

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view()),
    path('book-cat-list/<str:cat_name>/', BookDetail.as_view(), name='book-cat-list'),
    path('book-detail/<str:book_name>/', ShowBook.as_view(), name='show_book'),
    path('book-search', Search.as_view(), name='search'),
    path('price-filter', Home.as_view(), name='filter')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
