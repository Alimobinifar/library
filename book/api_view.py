from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import BookSerializer, BookByCatSerializer
from .models import Book, Category, Author
from django.db.models import Q


class ManageBooks(APIView): #register and show data from/on database with api
    def get(self, reqeust):
        qs = Book.objects.all()
        ser_data = BookSerializer(qs, many=True)
        return Response(ser_data.data)

    def post(self, request):
        data = BookSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response({"message": "registered on db was success..."})
        else:
            return Response({"Error": "please send validated data "})


class BookById(APIView):
    def get(self, reqeust):
        book_id = reqeust.GET.get("q")
        qs = Book.objects.filter(id=book_id)
        ser_data = BookSerializer(qs, many=True)
        return Response(ser_data.data)


class BookByCat(APIView):

    def post(self, request):
        ser_data=BookByCatSerializer(data=request.data)
        if ser_data.is_valid():
            qs = Book.objects.filter(cat__title=ser_data.validated_data["cat"])
            return Response({qs.values("name")})

