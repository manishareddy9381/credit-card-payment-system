from django.urls import path
from .views import MakePaymentView, TransactionHistoryView

urlpatterns = [
    path('make-payment/', MakePaymentView.as_view(), name='make-payment'),
    path('history/', TransactionHistoryView.as_view(), name='history'),
]