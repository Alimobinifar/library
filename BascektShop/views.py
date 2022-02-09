import datetime
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import ShoppingBasket, FinalBasket
from book.models import Book


class AddToBasket(View):
    def get(self, request):
        if request.user.is_authenticated:
            book_id = request.GET.get("book_id")
            print(book_id)
            count = request.GET.get("count")
            print(count)
            qs = Book.objects.get(id=book_id)
            user_id = request.user
            # qs2 = Book.objects.filter(id=book_id)
            time = datetime.datetime.now()
            shopping_basket = ShoppingBasket(user=user_id, item=qs, date=time, count=count, status='pending')
            shopping_basket.save()
            return HttpResponse("Added SuccessFull")
        else:
            return redirect('user_login', )


class ShowBasket(View):
    def get(self, request):
        if request.user.is_authenticated:
            user_id = request.user
            qs = ShoppingBasket.objects.filter(user_id=user_id)
            ctx = {"data": qs}
            return render(request, 'Basket.html', ctx)
        else:
            return redirect('user_login')

class CancellOrder(View):
    def get(self, request):
        order_id = request.GET.get('q')
        qs = ShoppingBasket.objects.filter(id=order_id)
        if qs.get(id=order_id).status == 'pending':
            qs.update(status='cancelled')
            return HttpResponse("Cancelled SuccessFull")
        else:
            return HttpResponse("change status is not possible beacuse its status is : ok")


class ReactiveOrder(View):
    def get(self, request):
        order_id = request.GET.get('q')
        qs = ShoppingBasket.objects.filter(id=order_id)
        if qs.get(id=order_id).status == 'cancelled':
            qs.update(status='pending')
            return HttpResponse("Reactive SuccessFull")
        else:
            return HttpResponse("change status is not possible beacuse its status is : ok ")


class Pay(View):
    def get(self, request):
        user_id = request.user
        qs = ShoppingBasket.objects.filter(status='pending', user_id=user_id)
        date = datetime.datetime.now()
        user_basket = FinalBasket(user=user_id, date=date)
        user_basket.save()
        qs.update(status='ok', basket_id=user_basket)
        return HttpResponse("سفارشات شما ثبت شد و بزودی ارسال خواهند شد")
