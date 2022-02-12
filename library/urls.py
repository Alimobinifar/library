
from django.contrib import admin
from django.urls import path, include
from book.views import Home, BookDetail, ShowBook, Search, books, book
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views





urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', Home.as_view(), name='home'),
    path('', include('book.urls')),
    path('book-search', Search.as_view(), name='search'),
    path('price-filter', Home.as_view(), name='filter'),
    path('history', include('history.urls')),
    path('generate-token/', views.obtain_auth_token),

    path('', include('user.urls')),
    path('', include('BascektShop.urls'))

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
