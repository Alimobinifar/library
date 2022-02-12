from rest_framework import serializers
from .models import ShoppingBasket


class ShoppingBasketrerializer(serializers.Serializer):
    id = serializers.CharField()
    user = serializers.CharField(source='user.id')
    item = serializers.CharField()
    date = serializers.CharField()
    count = serializers.IntegerField()
    status = serializers.CharField()
    basket = serializers.CharField(source='basket.id')



#show all final baskets#
class FinalBasketSerializer(serializers.Serializer):
    user = serializers.CharField(source='user.username')
    date = serializers.DateTimeField()

