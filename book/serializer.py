
from rest_framework import serializers
from .models import Book, Category

# this class is based on old model of serializing
class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    author = serializers.CharField()
    price = serializers.IntegerField()
    cat = serializers.CharField()



# # Top class based on Model serializer with using extra kwargs
# class BookSerializer(serializers.ModelSerializer):
#     cat = serializers.StringRelatedField()
#     class Meta:
#         model = Book
#         fields = ("id", "name", "author", "price", "cat", "uu")
#         extra_kwargs = {"price": {"write_only": True}}


# class BookByCat(serializers.ModelSerializer):
#     cat = serializers.CharField()


class BookByCatSerializer(serializers.Serializer):
    cat = serializers.CharField()
