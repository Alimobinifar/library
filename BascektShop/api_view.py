from django.contrib.auth.models import User
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ShoppingBasketrerializer, FinalBasketSerializer
from . models import ShoppingBasket, FinalBasket


class ShoppBasket(APIView):

    def get(self, request):
        if request.user.is_authenticated:
            user_id = request.user.id
            print(user_id)
            qs = ShoppingBasket.objects.filter(user_id=user_id)
            ser_data = ShoppingBasketrerializer(qs, many=True)
            return Response(ser_data.data)



class FinalShoppBasket(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            user_id = request.user.id
            qs = FinalBasket.objects.filter(user_id=user_id)
            ser_data = FinalBasketSerializer(qs, many=True)
            return Response(ser_data.data)


class FinalBasketDetail(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            final_basket_id = request.GET.get("final-basket-id")
            qs = ShoppingBasket.objects.filter(basket_id=final_basket_id)
            ser_data = ShoppingBasketrerializer(qs, many=True)
            return Response(ser_data.data)


