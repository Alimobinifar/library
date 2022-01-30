from django.shortcuts import render
from django.views import View
from .models import Book, Category, Author
from django.db.models import Q


class Home(View):

    def get(self, request):
        min_price = request.GET.get("q")
        max_price = request.GET.get("q")
        if min_price is None or max_price is None or min_price is '' or max_price is '':
            qs = Category.objects.filter(parent_id=None)
            qs2 = Book.objects.filter()
        else:
            qs = Category.objects.filter(parent_id=None)
            qs2 = Book.objects.filter(price__gt=min_price, price__gte=max_price)

        context = {'name': qs, 'book': qs2}
        return render(request, 'home.html', context)

    template_name = 'home.html'


class BookDetail(View):

    def get(self, request, cat_name):
        category = Category.objects.get(title=cat_name)
        q_filter = Q(cat__parent__title=cat_name) | Q(cat__title=cat_name)

        if category.parent is None:
            qs = Book.objects.filter(q_filter)

        else:
            qs = Book.objects.filter(cat__title=cat_name)

        context = {'name': qs}
        return render(request, 'book_cat.html', context)


class ShowBook(View):

    def get(self, request, book_name):
        qs = Book.objects.filter(name=book_name)
        context = {'data': qs}
        return render(request, 'book_detail.html', context)


class Search(View):

    def get(self, request):
        search_value = request.GET.get("q", "")
        qs = Book.objects.filter(name__contains=search_value)
        ctx = {'data': qs}
        return render(request, 'search.html', ctx)


