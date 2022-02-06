
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'name', 'author', 'price', 'publisher')
        extra_kwargs = {"auther": {"write_only": True}}