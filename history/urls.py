from django.urls import path
from history.views import ShowHistory, HistoryDetail


urlpatterns = [
    path('history', ShowHistory.as_view(), name='history'),
    path('history-detail', HistoryDetail.as_view(), name='history-detail'),
]