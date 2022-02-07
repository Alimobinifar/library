
from rest_framework import serializers
from .models import Book, Author, Category


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('name', 'author', 'price', 'publisher')
        extra_kwargs = {"auther": {"write_only": True}}


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'parent')