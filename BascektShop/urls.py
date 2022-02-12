from django.urls import path
from BascektShop.views import AddToBasket, ShowBasket, CancellOrder, ReactiveOrder, Pay
from.api_view import ShoppBasket, FinalShoppBasket, FinalBasketDetail


urlpatterns = [
    path('add-to-basket', AddToBasket.as_view(), name='add'),
    path('show-basket', ShowBasket.as_view(), name='show-basket'),
    path('cancellorder', CancellOrder.as_view(), name='cancellorder'),
    path('reactiveorder', ReactiveOrder.as_view(), name='reactiveorder'),
    path('pay', Pay.as_view(), name='pay'),
    path('shopping-basket', ShoppBasket.as_view()),
    path('final-shop-basket', FinalShoppBasket.as_view()),
    path('final-basket-detail', FinalBasketDetail.as_view())
]
