
from django.db import models
from django.contrib.auth.models import User
from book.models import Book


class FinalBasket(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField()



class ShoppingBasket(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    item = models.ForeignKey(Book, on_delete=models.PROTECT)
    date = models.DateTimeField()
    count = models.IntegerField()
    basket = models.ForeignKey(FinalBasket, models.PROTECT, null=True)
    state_choices = [
        ('ok', 'خرید نهایی شده '),
        ('pending', 'در انتظار پرداخت'),
        ('cancelled', 'انصراف از خرید')
    ]
    status = models.CharField(
        max_length=15,
        choices=state_choices,
        default='pending'
    )
