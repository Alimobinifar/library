from django.shortcuts import render, redirect
from django.views import View
from BascektShop.models import ShoppingBasket, FinalBasket


class ShowHistory(View):
    def get(self, request):
        if request.user.is_authenticated:
            user_id = request.user
            qs = FinalBasket.objects.filter(user_id=user_id)
            ctx = {"data": qs}
            return render(request, 'history.html', ctx)
        else:
            return redirect('user_login')


class HistoryDetail(View):

    def get(self,request):
        basket_id = request.GET.get("q")
        qs = ShoppingBasket.objects.filter(basket_id=basket_id)
        ctx = {'data': qs}
        return render(request, 'history_detail.html', ctx)
