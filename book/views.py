from django.shortcuts import render, redirect
from django.views import View
from .models import Book, Category
from django.db.models import Q
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from .serializer import BookSerializer


class Home(View):

    def get(self, request):
        min_price = request.GET.get("q")
        max_price = request.GET.get("q")
        if min_price is None or max_price is None or min_price is '' or max_price is '':
            qs = Category.objects.filter(parent_id=None)
            qs2 = Book.objects.filter()
        else:
            qs = Category.objects.filter(parent_id=None)
            qs2 = Book.objects.filter(price__gt=min_price, price__lte=max_price)

        context = {'name': qs, 'book': qs2}
        return render(request, 'home.html', context)

    template_name = 'home.html'


class BookDetail(View):

    def get(self, request, cat_name):

        try:
            category = Category.objects.get(title=cat_name)
            q_filter = Q(cat__parent__title=cat_name) | Q(cat__title=cat_name)

            if category.parent is None:
                qs = Book.objects.filter(q_filter)

            else:
                qs = Book.objects.filter(cat__title=cat_name)

        except :
            'Error in internal servers '

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



# @api_view(["GET","POST"])
# def BookName(request):
#     if request.method == "GET":
#         qs = Book.objects.values('name')
#         data = {"name": qs}
#         return Response(data)
#     else:
#         n = request.data['name']
#         print(n)
#         return Response({"name":n})

@api_view()
def books(request):
    qs = Book.objects.all()
    ser_data = BookSerializer(qs, many=True)
    return Response(ser_data.data)


@api_view()
def book(request, name):
    try:
        qs = Book.objects.filter(name__contains=name)
    except qs.DoesNotExist:
        return Response({"Error": "This user is not exist"})
    ser_data = BookSerializer(qs, many=True)
    return Response(ser_data.data)


































