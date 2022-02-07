from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import BookSerializer, CategorySerializer
from .models import Book, Category, Author
from django.db.models import Q


class ShowAllBooks(APIView): #register and show data from/on database with api

    def get(self, reqeust):
        qs = Book.objects.all()
        ser_data = BookSerializer(qs, many=True)
        return Response(ser_data.data)


    def post(self, request):
        data = BookSerializer(data=request.data)
        if data.is_valid():
            data.save()
            # print(data["auther"])
            # qs = Book(name=data['name'], pages=None, author_id=data['author'], price=data['price'], cat=None, img=None, publisher_id=data['publisher'])
            # qs.save()
            return Response({"message": "registered on db was success..."})
        else:
            return Response({"Error": "please send validated data "})

    # def delete(self, request):
    #     data = request.data
    #     Book.objects.filter(id=data['id']).delete()


class ShowBooksByCategory(APIView):

    def get(self, request):
        data = request.data
        try:
            category = Category.objects.get(title=data['cat'])
            q_filter = Q(cat__parent__title=data['cat']) | Q(cat__title=['cat'])
            if category.parent is None:
                qs = Book.objects.filter(q_filter)
                ser_data=CategorySerializer(qs, many=True)
                return Response(ser_data.data)
            else:
                qs = Book.objects.filter(cat__title=data['cat'])
                ser_data = CategorySerializer(qs, many=True)
                return Response(ser_data.data)
        except :
            'Error in internal servers '
