from django.urls import path
from .views import PaymentResultView, RedirectPaymentView

app_name = 'payment'

urlpatterns = [
    path('checkout/', RedirectPaymentView.as_view(), name='checkout'),
    path('result/', PaymentResultView.as_view(), name='result'),
]
